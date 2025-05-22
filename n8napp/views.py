from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
import json
from django.http import HttpResponse
import requests
from .serializers import InputSerializer

# Create your views here.


class SendRequest(APIView):
    def post(self,req):
        print("hi")
        input_data= {
            "First Name": "bobby bun",
            "Last Name": "TA",
            "Email": "boby00@gmail.com",
            "Budget": "1000+",
            "Message": "hey"
        }
        
        # serializer= InputSerializer(data=input_data)
        webhook_url = "https://arjunomia.app.n8n.cloud/webhook/77dd9080-6c7e-40a0-8435-7ba64d176874"
        headers = {'Content-Type': 'application/json'}
                
        # if serializer.is_valid():
        #         print(serializer.validated_data)
        #         print(serializer.data)
                # res= requests.post('', json=serializer.data)

        try:
            response = requests.post(webhook_url, headers=headers, data=json.dumps(input_data))
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            return HttpResponse("n8n workflow triggered successfully!")
        except requests.exceptions.RequestException as e:
            return HttpResponse(f"Error triggering n8n workflow: {e}", status=500)
        
        
        
        
        