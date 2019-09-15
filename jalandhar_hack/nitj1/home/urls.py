from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('seats/', views.seats, name='seats'),
    path('seatmap/',views.seatmap, name='seatmap'),
    path('<numb>',views.rtest, name='rtest'),
]