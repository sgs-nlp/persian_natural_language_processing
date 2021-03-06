from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
                  path('applications/', include('statistical_pnc.urls')),
                  path('', views.home_page_view, name='home'),
                  path('about-me', views.about_me_page_view, name='about_me'),
                  path('contact-me', views.contact_me_page_view, name='contact_me'),
                  path('sample', views.sample_page_view, name='sample'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
