from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class Event(models.Model):
    event_id = models.IntegerField(unique=True, validators=[MinValueValidator(1)])
    event_name = models.CharField(max_length=200)
    event_date = models.DateTimeField('Event Date')
    url = models.URLField()
    def __str__(self):
        return self.event_name
