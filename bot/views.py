import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes
import os
import dotenv
dotenv.read_dotenv()
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
        
                    "Authorization":"Bearer EAAQhSS35gHsBAEgL054iYThXO8Q4cLixvIVTc9AwiXhKFFGBc2YZCvpu6yT7dkSt7GrDJoKj6aFhH793YkMXZBh5N6HHdcYsItPkLdT9hQx5VVdmyoT5coS1HF5yfL4rVjm1bd9g8d1ZBr54e7DTMFKLt325ZCPWBIBbGXBm4QQZCJBtn35hrZAK38TOC31ZBSzCytWiHWyDwZDZD"
                    ,
                    "Content-Type":"Application/json" 
        }
                
                x = requests.post( os.getenv("FACEBOOK_API"), json = jsondata,headers=headers)
        return Response(x.json())


