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

class SendMessage(APIView):
    authentication_classes = []
    permission_classes = []
    

    def post(self,request):
        lis = ["919724946042","917698544197", "919409212945"]
        
       
        for i in lis:
                jsondata = {
            "messaging_product": "whatsapp",
            "to": i,
            "type": "template",
            "template": {
                "name": "hello_world",
                "language": {
                    "code": "en_US"
                }
            }
        }   
                headers = {
        
                    "Authorization":"Bearer EAAQhSS35gHsBALxDFuhQlLaetDrzkVLwGy5oBHHmM7ToLBKQvwRZA8KWbz4r8HrakVwmWbnChFo25dbXXZAk5R6wOiRDY1fH2dByloKZArTx5OkoaInsu91lIQ3DzXxB3axeQLXX5F7CBla9nnZBzZAlIjQqMZCEyyvMPzmHhjLhG1iCx9dEXhOyFNU7qfOmhUvrrSqNryeAZDZD"
                    ,
                    "Content-Type":"Application/json" 
        }
                
                x = requests.post( "https://graph.facebook.com/v16.0/110807025306438/messages", json = jsondata,headers=headers)
        return Response(x.json())


