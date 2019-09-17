from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from django.shortcuts import render
import pyrebase
#from django.shortcuts import render
# import firebase_admin
from firebase import firebase
# from firebase_admin import credentials
# from firebase_admin import db
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from webpush import send_user_notification
import json
from datetime import datetime
from .trans import servstart
config = {
'apiKey': "KmA3IPZjdcV6gn0wHF1t0DSJGSg9iAexvJl8HMow",
'authDomain': "smart-audi.firebaseio.com",
'databaseURL': " https://smart-audi.firebaseio.com/",
'projectId': "smart-audi",
'storageBucket': "smart-audi.appspot.com",
'messagingSenderId': "246323352532"
}
# firebase = pyrebase.initialize_app(config)
# database=firebase.database()


def index(request):
    print("emergency")

    my_dict = {'insert_me': 'Rahul'}

    return render(request, 'emergency/template.html', context=my_dict)

def testing1(request):
    servstart()
    return

def testing2(request, trancript):
    fire = firebase.FirebaseApplication('https://smart-audi.firebaseio.com/', None)
    data = {str(datetime.now().microsecond): trancript}
    snap = fire.patch('/speech_to_text/', data)
    result = fire.get('/speech_to_text/', None)
    print(result)
    return HttpResponse("Hel")

def virt(request):

    return HttpResponse("Virtual Handraise Invoked")
def test(request):
    my_dict = {'insert_me': 'Srishti'}
    fire = firebase.FirebaseApplication('https://smart-audi.firebaseio.com/', None)
    result = fire.get('/speech_to_text',None)
    print(result)
    # # #data = {'emergency': True, 'seated': False, 'x': 1, 'y': 1}
    # s = result.append('ppk')
    data = {str(datetime.now().microsecond):'mizu'}
    snap = fire.patch('/speech_to_text',data)
    # # print("Rahul")
    # # #firebase.get_async('/seats/A3', snap, callback=callback_get)
    # result = fire.get('/speech_to_text', None)
    # print(result)
    return render(request, 'emergency/template.html', context=my_dict)
# Create your views here.

# @require_POST
# @csrf_exempt
# def send_push(request):
#     try:
#         body = request.body
#         data = json.loads(body)
#
#         if 'head' not in data or 'body' not in data or 'id' not in data:
#             return JsonResponse(status=400, data={"message": "Invalid data format"})
#
#         user_id = data['id']
#         user = get_object_or_404(User, pk=user_id)
#         payload = {'head': data['head'], 'body': data['body']}
#         send_user_notification(user=user, payload=payload, ttl=1000)
#
#         return JsonResponse(status=200, data={"message": "Web push successful"})
#     except TypeError:
#         return JsonResponse(status=500, data={"message": "An error occurred"})
