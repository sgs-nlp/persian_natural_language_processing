from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

from .controller import *


def index_view(request: HttpRequest):
    res = index_default_data()
    return render(
        request,
        'ai_index.html',
        context=res,
    )


def preprocessing_view(request: HttpRequest):
    res = prerequisites()
    return JsonResponse(res)


def classification_view(request: HttpRequest):
    content = request.POST['content_text_for_classify']
    titr = request.POST['titr_text_for_classify']
    res = classification_result(content, titr)
    return JsonResponse(res)


def classification_feedback_view(request: HttpRequest):
    classification_feedback_view(news_id=request.POST['news_pk'], category_id=request.POST['category_radios'])
    return JsonResponse({})
