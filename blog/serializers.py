#!/usr/lib/env python
#-*-coding:UTF-8-*-

from rest_framework import serializers
from blog.models import *

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Article
        fields = ('title','content','user')
    '''   
    3.0版本已经不支持，用create(),update()代替
    def restore_object(self,attrs,instance=None):
        if instance:
            instance.title = attrs['title']
            instance.content = attrs['content']
            instance.user = attrs['user']
            return instance
        return Article(**attrs)
    '''
    def create(self, validated_data):
        return Article.objects.create(**validated_data)
    def update(self, instance, validated_data):
        return serializers.ModelSerializer.update(self, instance, validated_data)
    
class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    articles = serializers.HyperlinkedRelatedField(many=True, view_name='article-detail',read_only=True)
    
    class Meta:
        model = User
        fields = ('id','username','articles')
        #fields = '__all __'
        