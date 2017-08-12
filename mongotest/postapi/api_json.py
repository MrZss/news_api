#coding=utf-8
import json

def jsonfuns(posts):
    posts_json= []
    i=0
    for post in posts:
        _id=str(post._id)
        data = {
                'i':i,
                '_id':_id,
                'title':post.title,
                'author':post.author,
                'post_time':post.post_time,
                'mainimg_url':post.mainimg_url,
                'summary':post.summary,
                'tag':post.tag
                }
        posts_json.append(data)
        i=i+1

    return posts_json


def jsonfun(post):
    posts_json= []
    _id=str(post._id)
    data = {
            '_id':_id,
            'title':post.title,
            'author':post.author,
            'post_time':post.post_time,
            'mainimg_url':post.mainimg_url,
            'summary':post.summary,
            'tag':post.tag,
            'post_from':post.post_from,
            'content':post.content
            }
    posts_json.append(data)

    return posts_json




