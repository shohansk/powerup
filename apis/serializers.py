from rest_framework import fields, serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token


class ArticleSerializer(serializers.ModelSerializer):

    class  Meta:
       model = Article
       fields = ['id','tittle','description']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']

        extra_kwargs = {'password':{
            'write_only':True,
            'required':True
        }
        }
       
    def create(self, validated_data):

        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user