from django.db import models

# Create your models here.
class Article(models.Model):
    tittle = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.tittle
    