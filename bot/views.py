from django.shortcuts import render
from django.http import HttpResponse
import pywhatkit
import requests
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
        lis = ["919724946042","917698544197"]
        
        # pywhatkit.sendwhatmsg("+919998699658", "test", "11", "16")

        # a = request.data["mobile"],
        # print("==========>>>", a)
        # b = request.data["msg"]
        # # sendwhatmsg_instantly
        # print("==============>>>>", b)
        # print(request.data["hour"])
        # print(request.data["min"])

        # print("----------------------------------------------------------a")
        # pywhatkit.sendwhatmsg(request.data["mobile"], request.data["msg"],
        #                        request.data["hour"], request.data["min"])
        # print("----------------------------------------------------------b")
        for i in lis:
                jsondata = {
            "messaging_product": "whatsapp",
            "to": i,
            "type": "template",
            "template": {
                "name": "hi",
                "language": {
                    "code": "en_US"
                }
            }
        }   
                headers = {
        
                    "Authorization":"Bearer EAAQhSS35gHsBAHmPv5r3nOXVYyaOhagU6TEv4ZBms9iFegOkRNeefcjU7364AMiTghWZBGHffwJtfTiO9ZAlYtf5ZCnoSfZBfkZB6Ihgin18Qm7CI3r6mZCFVHksHIerGZBjkQfMdNoibUbZA0EpdHvM0hTgEMeEt2N179PjDt092j4qdeMaBRv0qGZAQfZAQKDS2U5UvQEiPWq6gZDZD"
                    ,
                    "Content-Type":"Application/json" 
        }
                
                x = requests.post( "https://graph.facebook.com/v16.0/110807025306438/messages", json = jsondata,headers=headers)
        return Response(x.json())


