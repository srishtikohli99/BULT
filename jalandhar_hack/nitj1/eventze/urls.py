from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.index, name='index'),
    path('feedback/',views.feed, name='feedback'),
    path('live/',views.live, name='live'),
]