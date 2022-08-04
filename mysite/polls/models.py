import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

#データベースのレイアウトを決めるやつみたい
#table:question
#|----------------------|
#|question_text|pub_date|
#|----------------------|
#|django楽しい  |2022/8/1|
#|----------------------|
#こんな感じちゃう？
#訂正
#オートインクリメントでidが付与されるらしい

class Question(models.Model):
    # ...
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')
    
    def __str__(self):
        return self.question_text
    
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text