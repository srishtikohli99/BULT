from django.shortcuts import render
from django.http import HttpResponse
from eventze.forms import formfeed
from eventze.models import Event, feedback
from aylienapiclient import textapi
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
#from forms import FormName
def index(request):
    return HttpResponse("Hello")

def thanka(request):
    return render(request,'eventze/feedthank.html')
def feed(request):
    form = formfeed()
    if request.method == 'POST':
        form=formfeed(request.POST)
        print(form)
        if form.is_valid():
            # client = textapi.Client("42f857c1", "14a7ac2d47989ded74c0f1f49522cfdc")
            # sentiment = client.Sentiment({'text':})
            #print(form)
            form.save(commit = True)

            return thanka(request)
            # print("Name"+form.cleaned_data['name'])
            # print("Email"+form.cleaned_data['email'])
            # print("Feedback"+form.cleaned_data['feedback'])


    return render(request,'eventze/feed.html',{'form':form})
def live(request):
    table=Event.objects.all().values_list()
    url = 'https://www.youtube.com/watch?v=VOLKJJvfAbg'
    for e in table:
        print(e)
        if e[5]=='Live':
            url=e[4]
            break
    co = url[-11:]
    vid = 'https://www.youtube-nocookie.com/embed/'+co
    lc = 'https://www.youtube.com/live_chat?v='+co+'&amp;embed_domain=192.168.1.100'


    return render(request,'eventze/live.html',{'vid':vid,'lc':lc})
def transcribe(request):

    return render(request, 'eventze/transcribe.html')
def display(request):

    query_results = Event.objects.all()

    #print(query_results[0].event_id)

    return render(request,'eventze/display.html',{'query_results':query_results})

def check_admin(user):
   return user.is_superuser


#@method_decorator(user_passes_test(lambda u: u.is_superuser))
#@staff_member_required
@user_passes_test(lambda u:u.is_staff, login_url='/home/')
def senti(request):

    client = textapi.Client("42f857c1", "14a7ac2d47989ded74c0f1f49522cfdc")
    # feedo = feedback.objects.values_list('feedback')
    # query_results = feedback.objects.all()
    # #sentiment = client.Sentiment({'text': })
    # l=[]
    # tot = len(feedo)
    # for i in range(tot):
    #     st = str(feedo[i][0])
    #     sentiment = client.Sentiment({'text':st})
    #     l.append(sentiment['polarity'])
    #     #l[query_results[i].feedback_id]=sentiment['polarity']
    # d={'sentu':l,'query_results':query_results,'tot':tot}
    # print(d)
    #
    # #return HttpResponse('running')
    # return render(request,'eventze/senti.html',d)

    table=feedback.objects.all().values_list()
    for e in table:
        print(e)
        if e[4]=="":
            print("match")
            #sentiment analysis
            sentiment = client.Sentiment({'text': str(e[3])})
            t= feedback.objects.get(feedback_id=int(e[0]))
            t.sentim=sentiment['polarity']
            t.save()

    query_results = feedback.objects.all()

    return render(request,'eventze/senti.html', {'query_results':query_results})




def subm(request):
    client = textapi.Client("42f857c1", "14a7ac2d47989ded74c0f1f49522cfdc")

    if request.method == 'POST':
        form = feedback(request.POST)
        form.save()

@user_passes_test(lambda u:u.is_staff, login_url='/home/')
def seatcontrol(request):

    return render(request,'eventze/seatmapfinal.html')






# Create your views here.
