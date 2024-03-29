from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.index, name='index'),
    path('feed/',views.feed, name='feed'),
    path('live/',views.live, name='live'),
    path('events/',views.display, name='display'),
    path('transcribe/',views.transcribe, name='transcribe'),
    path('feedbacks/',views.senti, name='senti'),
    path('seatcontrol/',views.seatcontrol,name='seatcontrol'),
]