from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question,Choice
from eventze.models import Event
# Create your views here.

def index(request):
    #return HttpResponse("Hello")
    event_list  = []#Event.objects.order_by('-pub_date')
    my_dict = {'insert_me':event_list}
    return render(request, 'polls/index.html', context=my_dict)