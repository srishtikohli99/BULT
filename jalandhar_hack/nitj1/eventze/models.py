from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class Event(models.Model):
    event_id = models.IntegerField(unique=True, validators=[MinValueValidator(1)])
    event_name = models.CharField(max_length=200)
    event_date = models.DateTimeField('Event Date')
    url = models.URLField()
    Choices = [('Upcoming', 'Upcoming'), ('Live', 'Live'),('Completed','Completed')]
    status = models.CharField(choices=Choices, default='U',max_length=10)
    def __str__(self):
        return self.event_name

class feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField(max_length=1000)

