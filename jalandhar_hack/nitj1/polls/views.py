from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question,Choice,Offline_Question,Offline_Response
from eventze.models import Event
from ipware import get_client_ip
# Create your views here.

def index(request):
    #return HttpResponse("Hello")
    event_list  = []#Event.objects.order_by('-pub_date')
    my_dict = {'insert_me':event_list}
    return render(request, 'polls/index.html', context=my_dict)


def off_res(request, ans):
    ques = Offline_Question.objects.values_list('question_id','status','A','B','C','D')
    #print(ques[0][0])
    #q = Offline_Question.objects.filter(status='I')
    #print(q)
    q=None
    for i in ques:
        if i[1]=='A':
            q=i[0]
            a=i[2]
            b=i[3]
            c=i[4]
            d=i[5]
    obje = Offline_Question.objects.filter(question_id=q).first()
    print(obje)
    ip, is_routable = get_client_ip(request)
    #print(type(q))
    print("hahah")
    anses = Offline_Response.objects.values_list('client_ip','question')
    temp_list = []
    for ttt in anses:
        temp_list.append(list(ttt))
    print(temp_list)
    print(type(ip))
    if q == None:
        return HttpResponse('No active question available')
    else:
        for ti in temp_list:
            #print(type(ti[]))
            if ti[0] == ip and str(ti[1]) == str(q):
                print("Great")
                return HttpResponse("Your Response Already exist")

        ores = Offline_Response()
        ores.client_ip = ip
        ores.question = obje


        if ans == 'A':
            ores.Value = a
            #Offline_Response.objects.create('question'=q,'client_ip'=ip,'Value'=a)
        elif ans =='B':
            ores.Value = b
            #foo = Offline_Response.objects.create('question' = q, 'client_ip' = ip, 'Value' = b)
        elif ans == 'C':
            ores.Value = c
            #foo = Offline_Response.objects.create('question' = q, 'client_ip' = ip, 'Value' = c)
        elif ans == 'D':
            ores.Value = d
            #foo = Offline_Response.objects.create('question' = q, 'client_ip' = ip, 'Value' = d)
        ores.save()





    return HttpResponse(ans)