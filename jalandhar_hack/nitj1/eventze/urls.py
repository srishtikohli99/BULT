from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.index, name='index'),
    path('feed/',views.feed, name='feed'),
    path('live/',views.live, name='live'),
    path('events/',views.display, name='display'),

]