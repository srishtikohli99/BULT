from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from eventze.models import Event
# Create your models here.

# class Event(models.Model):
#     event_id = models.IntegerField(unique=True, validators=[MinValueValidator(1)])
#     event_name = models.CharField(max_length=200)
#     event_date = models.DateTimeField('Event Date')
#     url = models.URLField()
#     def __str__(self):
#         return self.event_name

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE,default=1)
    #event_id = models.IntegerField()

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,blank=True)
    #question = models.CharField(max_length=200)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text