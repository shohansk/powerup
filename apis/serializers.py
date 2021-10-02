from rest_framework import fields, serializers
from .models import *


class ArticleSerializer(serializers.ModelSerializer):

    class  Meta:
       model = Article
       fields = ['id','tittle','description']
       
