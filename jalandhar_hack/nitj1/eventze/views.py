from django.shortcuts import render
from django.http import HttpResponse
from eventze.forms import formfeed

#from forms import FormName
def index(request):
    return HttpResponse("Hello")

def feed(request):
    form = formfeed()
    if request.method == 'POST':
        form=formfeed(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
            # print("Name"+form.cleaned_data['name'])
            # print("Email"+form.cleaned_data['email'])
            # print("Feedback"+form.cleaned_data['feedback'])


    return render(request,'eventze/feed.html',{'form':form})
def live(request):

    return render(request,'eventze/live.html')

def display(request):

    return render(request,'eventze/display.html')




# Create your views here.
