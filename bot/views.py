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
        
                    "Authorization":"Bearer EAAQhSS35gHsBAEdXUTbSiGIoB8JNmPJ3WKfMsH8eJTnlT07UAqA3gxz8ZB2nlriz6XDBCm0fqmqeo1csaCxxJ6XfaZCPtnQZCwmf2XNIQNElXxZCmZBxkGJUDx9qZCv9OQL8w8eDdkELXoiohSnrI5U3nK46oG1GOZAM2SoxcZBiKoeadzcG6DFCGdIeBuHpQzEMoEEeqUzQWgZDZD"
                    ,
                    "Content-Type":"Application/json" 
        }
                
                x = requests.post( os.getenv("FACEBOOK_API"), json = jsondata,headers=headers)
        return Response(x.json())


