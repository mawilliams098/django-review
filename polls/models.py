from django.db import models

"""
Here, each model is represented by a class that subclasses django.db.models.Model. 
Each model has a number of class variables, each of which represents a database 
field in the model.
"""

# question_text and pub_date are used as column names in the DB
# first positional argumnet 'date published' used as human-readable name / documentation

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)