from django.shortcuts import render
from django.http import HttpResponse
from ipware import get_client_ip
# Create your views here.
def index(request):
    ip, is_routable = get_client_ip(request)
    print(ip)
    return render(request, 'home/index.html')

def seats(request):
    return render(request, 'home/seats.html')

def seatmap(request):
    return render(request, 'home/seatmap.html')

def rtest(request,numb):
    return HttpResponse(numb)

