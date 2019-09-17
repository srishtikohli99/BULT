from django.urls import path

from . import views

urlpatterns = [
    path('*/', views.index, name='index'),
    path('',views.test, name='test'),
    path('#/',views.virt, name='virt'),
    path('testing1/',views.testing1, name='testing1'),

]