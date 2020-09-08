import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from requests import Response
from rest_framework import viewsets, mixins
from travelando import settings
import json


# Create your views here.
class SearchesProcessCentricView(View):
    def get(self, request):
        parameters = request.GET
        intent_name = parameters.get('intentName', None)

        status_code = 400
        response = {
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": ["Sorry, I'm not able to manage your request."]
                    }
                }
            ]
        }

        try:
            if intent_name == 'search':
                response = requests.get(f"http://{settings.SERVICE_BUSINESS_LOGIC_HOST}:{settings.SERVICE_BUSINESS_LOGIC_PORT}/{settings.SERVICE_BUSINESS_LOGIC}/search", parameters)
                status_code = response.status_code
                return JsonResponse(response.json(), safe=False, status=status_code)
        except:
            print('Error in business logic response')
            status_code = 500

        return JsonResponse(response, status=status_code)

