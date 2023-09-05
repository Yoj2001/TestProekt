from django.db import models
from django.utils import timezone
from datetime import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
\


    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    country_name = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.country_name
