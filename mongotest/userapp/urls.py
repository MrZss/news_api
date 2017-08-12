#coding=utf-8
from django.conf.urls import url
from postapi.views import *

urlpatterns = [
    url(r'^userapi/$', PostList.as_view()),
    url(r'^userapi/(\w+)', PostDetail.as_view()),


    # url(r'^psot/(?P<pk>[0-9]+)/$', views.snippet_detail),
]