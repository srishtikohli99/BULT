from django.urls import path

from . import views

urlpatterns = [
    path('onlinepoll/', views.index, name='index'),
    path('offlineres/<ans>', views.off_res, name='off_res'),
    path('thanks/', views.thanks),
    path('onlinepoll/<int:question_id>/', views.detail),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote),
]