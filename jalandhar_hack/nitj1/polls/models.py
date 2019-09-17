from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from eventze.models import Event
import datetime
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

class Offline_Question(models.Model):

    question_text = models.CharField(max_length=200)
    question_id = models.IntegerField(primary_key=True)
    publish_date = models.DateField()
    A = models.CharField(default='',max_length=200)
    B = models.CharField(default='',max_length=200)
    C = models.CharField(default='',max_length=200)
    D = models.CharField(default='',max_length=200)
    Choices = [('A', 'Active'), ('I', 'Inactive')]
    status = models.CharField(choices=Choices, default='I',max_length=10)

    #Choices = [(A,'A'),(B,'B'),(C,'C'),(D,'D')]
    answer={'A':A, 'B':B, 'C':C, 'D':D}

    def __str__(self):
        #l=[self.question_text,self.question_id]
        return str(self.question_id)

class Offline_Response(models.Model):
    question = models.ForeignKey(Offline_Question, on_delete=models.CASCADE, blank=True)
    client_ip = models.CharField(max_length=200)
    Value=models.CharField(max_length=200)

    def __str__(self):
        s=self.client_ip+','+str(self.question)
        return str(s)