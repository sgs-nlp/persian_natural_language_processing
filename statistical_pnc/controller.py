import logging
from pathlib import Path
from scipy.spatial.distance import cosine
from random import sample

from nvd.converter import bag_of_word2one_hot

from .dataset2database import add2database
from .models import *
from django.conf import settings


def prerequisites():
    logging.info('Started storing dataset in the database.')
    from extra_settings.models import File
    file_name = 'HamshahriData.xlsx'
    from_which_row = 3704
    up_to_which_row = 5000
    file = File(file_name)
    if not file.is_complate(from_which_row, up_to_which_row):
        file.save(file_path=Path('staticfiles', file_name))
        res, header = file.load(to_be_continued=False, from_which_row=from_which_row,
                                up_to_which_row=up_to_which_row)
        add2database(file_name=file_name, part_of_data=res, part_of_data_header=header)
        file.save(complate=True, from_which_row=from_which_row, up_to_which_row=up_to_which_row)
    logging.info('Data storage in the database is complete.')


class NewsClassification:
    def __init__(self, number_of_train_data=0.85, dm=1, vector_size=300, negative=5, hs=0, min_count=2, sample=0,
                 workers=None, alpha=0.025, min_alpha=0.001, epochs=30):
        # 0 < number_of_train_data < 1
        self.number_of_train_data = number_of_train_data
        # 0 < number_of_test_data < 1
        self.number_of_test_data = 1 - number_of_train_data
        self.dm = dm
        self.vector_size = vector_size
        self.negative = negative
        self.hs = hs
        self.min_count = min_count
        self.sample = sample
        self.workers = workers if workers is not None else multiprocessing.cpu_count()
        self.alpha = alpha
        self.min_alpha = min_alpha
        self.epochs = epochs

    def _data_preparation(self):
        from gensim.models.doc2vec import TaggedDocument
        from .models import News

        news = News.objects.all()
        documents = []
        categories = {}
        for n in news:
            _words = n.words_tokenize.all()
            words = []
            for wrd in _words:
                words.append(str(wrd.pk))
            if n.category is None:
                tag = '-1'
                categories['-1'] = '-1'
            else:
                tag = str(n.category_id)
                categories[n.category.title] = n.category_id
            documents.append(TaggedDocument(words, [tag]))
        self._tagged_documents = documents
        self._categories = categories

    _tagged_documents = None

    @property
    def tagged_documents(self):
        if self._tagged_documents is None:
            self._data_preparation()
        return self._tagged_documents

    _x_data = None

    @property
    def x_data(self):
        if self._x_data is None:
            documents = utils.shuffle(self.tagged_documents)
            self._y_data, self._x_data = \
                zip(*[(doc.tags[0], self.gmodel.infer_vector(doc.words, steps=20)) for doc in documents])
        return self._x_data

    _y_data = None

    @property
    def y_data(self):
        if self._y_data is None:
            documents = utils.shuffle(self.tagged_documents)
            self._y_data, self._x_data = \
                zip(*[(doc.tags[0], self.gmodel.infer_vector(doc.words, steps=20)) for doc in documents])
        return self._y_data

    _categories = None

    @property
    def categories(self):
        if self._categories is None:
            self._data_preparation()
        return self._categories

    categories_list = None
    categories_list_pk = None

    def _clist(self):
        self.categories_list = categories_list(vector=True)
        self.categories_list_pk = self.categories_list.keys()

    news_for_classification = None

    def performance(self):
        data = News.objects.filter(category__isnull=False).all()
        data_len = len(data) - 1
        data_test_len = round(data_len / 6)
        test_ary_list = sample(range(1, data_len), data_test_len)
        _data = []
        for i in test_ary_list:
            _data.append(data[i])
        data_for_test = _data
        y_test = []
        predicted = []
        for itm in data_for_test:
            y_test.append(itm.category.pk)
            predicted.append(self._classification(itm).pk)
        from nvd.measure import true_or_false, precision, recall, accuracy
        false_negative, true_positive, true_negative, false_positive = true_or_false(predicted, y_test,
                                                                                     self.categories_list_pk)
        _precision = precision(true_positive, false_positive)
        _recall = recall(false_negative, true_positive)
        _accuracy = accuracy(false_negative, true_positive, true_negative, false_positive)
        return _precision, _recall, _accuracy

    def classification(self, content: str, titr: str = None):
        self.news_for_classification = news2db(
            content_string=content,
            titr_string=titr,
        )
        if self.news_for_classification.category is not None:
            return self.news_for_classification.category
        news = self.news_for_classification.vector
        news_word = self.news_for_classification.words
        len_news = len(news)
        sswcs = StatisticalWordCategory.objects.all()
        categories = Category.objects.all()

        maximum = -1
        top_cat = None
        for cat in categories:
            c_swcs = sswcs.filter(docs_frequency_stdev__gt=0).filter(category=cat).all()

            # minimum_number_of_sample_repetitions_per_category
            m_per_c = self.minimum_number_of_sample_repetitions * len(News.objects.filter(category=cat).all())

            cat_score = 0
            w_c = 1
            kwords = []
            for swc in c_swcs:
                true_word = news_word.filter(pk=swc.word_id).first()
                if true_word is not None:
                    if true_word.string == 'گروه' or true_word.string == 'شرایط' or true_word.string == 'آغاز':
                        stopword2db(word=true_word)
                    stp = StopWord.objects.filter(word_id=swc.word_id).first()
                    if stp is None:
                        tag = settings.TAGGER.tag([true_word.string])
                        if tag[0][1] == 'V' or tag[0][1] == 'ADV' or tag[0][1] == 'PR' or tag[0][1] == 'PRO' \
                                or tag[0][1] == 'AJ' or tag[0][1] == 'NUM' or tag[0][1] == 'AJe' or tag[0][1] == 'RES':
                            continue

                        m_per_c_swc = len(swc.all_docs_frequency)
                        if m_per_c_swc >= m_per_c:
                            # print(m_per_c_swc, m_per_c)
                            if swc.word_id <= len_news:
                                w_c += 1
                                dist = self._dist(
                                    swc.docs_frequency_mean,
                                    news[swc.word_id],
                                    swc.docs_frequency_stdev
                                )
                                if dist == 1:
                                    kwords.append(tag)
                                # print(cat.title, swc.word, dist)
                                cat_score += dist
            print(cat_score, cat, kwords)
            if cat_score > maximum:
                maximum = cat_score
                top_cat = cat
        return top_cat

    @staticmethod
    def _dist(a, b, variance):
        if a - variance < b < a + variance:
            return 1
        return 0


def feedback(news_id: int, category_id: int) -> News:
    from .models import statistical_word_category2db, word2db
    from nvd.pre_processing import tokenizer
    from nvd.extractor import Keywords
    news = News.objects.filter(pk=news_id).first()
    if news is None:
        return None
    category = Category.objects.filter(pk=category_id).first()
    if category is None:
        return None
    doc = tokenizer(news.string)
    kwrds = Keywords(fre=True)
    keywords = kwrds.by_frequency(document=doc, stopword=1, sents=1)
    for keyword in keywords:
        word = word2db(keyword['word'])
        statistical_word_category2db(word, category, docs_frequency=keyword['frequency'])
    return news
