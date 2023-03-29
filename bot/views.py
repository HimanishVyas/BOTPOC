from django.shortcuts import render
from django.http import HttpResponse
import pywhatkit
from rest_framework.views import APIView
from rest_framework.response import Response
from bot.models import mssg
# Create your views here.

class home(APIView):
    # if request.method == 'post':
    #     number = request.POST['number']
    #     msg = request.POST['msg']
    #     hour = request.POST['hour']
    #     min = request.POST['min']
    #     print("===============>>>>", number)

    #     a = mssg.objects.create(number = number, msg = msg, hour = hour, min = min)

    #     a.save()
    def get(self,request):
        print("----------------------------------------------------------a")
        pywhatkit.sendwhatmsg(request.data["mobile"], request.data["msg"], request.data["hour"], request.data["min"])
        print("----------------------------------------------------------b")
        return Response("done ...")


