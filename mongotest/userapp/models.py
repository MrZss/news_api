#coding=utf-8
from __future__ import unicode_literals
from mongoengine import *
import random
from django.db import models
#
#connect('Post',host='127.0.0.1',port=27017)
connect('lxqcxcy', host='127.0.0.1', port=27017)


# Create your models here.
class User(Document):
    _id = ObjectIdField()
    title = StringField()
    # # url = scrapy.Field()  # 帖子的网页链接
    author = StringField()  # 帖子的作者
    post_time = StringField()  # 发表时间
    mainimg_url = StringField()
    summary = StringField() #概述
    tag = StringField() #标签
    post_from =  StringField()
    content = StringField()  # 帖子的内容
    meta = {'collection': 'User'}