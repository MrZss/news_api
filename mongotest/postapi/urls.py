#coding=utf-8
from django.conf.urls import url
from postapi.views import *

urlpatterns = [
    url(r'^postapi/$', PostList.as_view()),
    url(r'^postapi/(\w+)', PostDetail.as_view()),


    # url(r'^psot/(?P<pk>[0-9]+)/$', views.snippet_detail),
]