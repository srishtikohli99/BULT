from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from polls.models import Question,Choice,Offline_Question,Offline_Response
from eventze.models import Event
from ipware import get_client_ip
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/page1.html', context)


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


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/indexx.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# Create your views here.

def thanks(request):
    # list = get_object_or_404 ( Choice, pk=choice_id)
    if request.method == 'POST':
        x = request.POST.get('choice')
        x = int(x)
        table = Choice.objects.all().values_list()
        for e in table:
            if int(e[0]) == x:
                print("match")
                print(e[0])
                t = Choice.objects.get(id=x)
                t.votes += 1
                t.save()

                # this will update only
            # print(e.vote)

        return render(request, 'polls/page3.html')
