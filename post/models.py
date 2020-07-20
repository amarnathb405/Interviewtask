from django.db import models
from vote.models import VoteModel
from django.contrib.auth.models import User


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ImageField(upload_to='images/')
    Description = models.CharField(max_length=120)

    def __str__(self):
        return self.Description


class ArticleReview(VoteModel, models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_date= models.DateField(auto_now_add=True)





