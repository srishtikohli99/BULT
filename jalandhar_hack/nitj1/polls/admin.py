from django.contrib import admin
from .models import Question,Choice,Offline_Question,Offline_Response
from eventze.models import Event
admin.site.site_header = "Auditorium Administration"
admin.site.register(Question)
admin.site.register(Event)
admin.site.register(Choice)
admin.site.register(Offline_Question)
admin.site.register(Offline_Response)
# Register your models here.
