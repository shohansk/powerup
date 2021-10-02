
from django.urls import path
from .views import *
urlpatterns = [
    
    path('articles/',article_list.as_view()),
  #  path('articles/<int:pk>/',article_details),
  path('articles/<int:id>/', ArticleDetails.as_view()),
]
