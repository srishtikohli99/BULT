from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('seatmap/', views.seats, name='seats'),
    path('seats/',views.seatmap, name='seatmap'),
    path('<numb>',views.rtest, name='rtest'),
    path('adminpan/',views.adminpan, name='adminpan'),
]