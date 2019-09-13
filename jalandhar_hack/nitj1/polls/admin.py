from django.contrib import admin
from .models import Question,Choice
from eventze.models import Event
admin.site.site_header = "Auditorium Administration"
admin.site.register(Question)
admin.site.register(Event)
admin.site.register(Choice)
# Register your models here.
