# coding=utf-8
from bson import json_util, ObjectId
import json
from postapi.models import Post
import random
from postapi.serializers import PostSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response

from api_json import jsonfun,jsonfuns


class PostList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()
        # ser = jsonfuns(posts=posts)

        a=[]

        for i in range(0,3):

            num=random.randrange(0,19)
            b=posts[num]
            a.append(b)
        ser = jsonfuns(posts=a)




        return Response(ser)

    def post(self, request, format=None):
        ser = PostSerializer(request.DATA)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

class PostDetail(APIView):
    def get(self,request,num,format=None):
        num=num.encode("UTF-8")
        # object_id=ObjectId(num)
        post=Post.objects.get(_id=num)
        ser= jsonfun(post=post)
        return Response(ser)



