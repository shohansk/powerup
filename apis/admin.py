from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register(Article)

@admin.register(Article)

class ArticleModel(admin.ModelAdmin):
    list_filter=('tittle','description')
    list_display=('tittle','description')


