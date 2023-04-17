import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes
import os
import dotenv
dotenv.load_dotenv()
# Create your views here.

class SendMessage(APIView):
    authentication_classes = []
    permission_classes = []
    

    def post(self,request):
        data = request.data 
        lis = data['number']       
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
        
                    "Authorization":os.getenv("Token"),
                    "Content-Type":"Application/json" 
                }
                
                x = requests.post( os.getenv("FACEBOOK_API"), json = jsondata,headers=headers)
        return Response(x.json())


