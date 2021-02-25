from django.db import models

# Create your models here.

class Question(models.Model):
    # Each variable represents a field in a database.
    question_text = models.CharField(max_length=200)
    # all fields first optional argument is an alternative human-readable name
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    # Each choice is related to a single question.
    # This relationship between Choice and Question class is formed
    # using ForeignKey.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)