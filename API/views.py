from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import json
# Create your views here.


class RecentLinkView(APIView):

    def get(self, request):
        output = {
            "slackUsername": "Bernadette Chukwuedo",
            "backend": True,
            "age": 17,
            "bio": "I am a backend developer, I love technology and also love getting to know people"
        }
        return HttpResponse(json.dumps(output), content_type='application/json')
