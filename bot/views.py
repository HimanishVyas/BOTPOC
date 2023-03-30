from django.shortcuts import render
from django.http import HttpResponse
import pywhatkit
from rest_framework.views import APIView
from rest_framework.response import Response
from bot.models import mssg
from rest_framework.decorators import authentication_classes
import datetime
# Create your views here.

class home(APIView):
    authentication_classes = []
    permission_classes = []
    # if request.method == 'post':
    #     number = request.POST['number']
    #     msg = request.POST['msg']
    #     hour = request.POST['hour']
    #     min = request.POST['min']
    #     print("===============>>>>", number)

    #     a = mssg.objects.create(number = number, msg = msg, hour = hour, min = min)

    #     a.save()

    def get(self,request):

        
        # pywhatkit.sendwhatmsg("+919998699658", "test", "11", "16")

        a = request.data["mobile"],
        print("==========>>>", a)
        b = request.data["msg"]
        # sendwhatmsg_instantly
        print("==============>>>>", b)
        print(request.data["hour"])
        print(request.data["min"])

        print("----------------------------------------------------------a")
        pywhatkit.sendwhatmsg(request.data["mobile"], request.data["msg"],
                               request.data["hour"], request.data["min"])
        print("----------------------------------------------------------b")
        return Response("done ...")


