import datetime

from django.db import models
from django.utils import timezone

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

    # django uses __str__() methods in the admin site... useful to have a readable return
    def __str__(self):  
        return self.question_text


    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Finally, note a relationship is defined, using ForeignKey. 
# That tells Django each Choice is related to a single Question.
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text