from django.shortcuts import render,HttpResponse

from .models import *
from .serializers import *
from rest_framework.views import APIView

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import mixins, status
from rest_framework import viewsets
# Create your views here.

'''
  
  Lets do some code

'''


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer




'''

class ArticleViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin ,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
   

'''

'''
 


def index(request):
    return HttpResponse("it is working")

class article_list(APIView):

   
    def get(self, request, ):
        articles = Article.objects.all()
        serializers = ArticleSerializer(articles, many=True)
        return Response(serializers.data)

       
    def post(self, request, format=None):
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status =status.HTTP_201_CREATED)
        return Response(serializer.errors , status =status.HTTP_400_BAD_REQUEST)





class ArticleDetails(APIView):

    def get_object(self, id):
        try:
            return Article.objects.get(id=id)


        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self,request,id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors , status =status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''


