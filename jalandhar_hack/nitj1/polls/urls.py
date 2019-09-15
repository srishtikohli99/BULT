from django.urls import path

from . import views

urlpatterns = [
    path('events/', views.index, name='index'),
    path('offlineres/<ans>', views.off_res, name='off_res'),
]