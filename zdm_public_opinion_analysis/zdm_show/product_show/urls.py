from unicodedata import name
from django.contrib.admindocs.urls import urlpatterns
from django.urls import path
from . import views


urlpatterns = [
    path('', views.qipaoshui, name='qipaoshui')
]