from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=300)
    id = models.AutoField(primary_key=True)
    date_published = models.DateTimeField(default=datetime.utcnow)
    expired = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_published']

    def __str__(self):
        return self.question


class Option(models.Model):
    option_title = models.CharField(max_length=100)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.option_title
