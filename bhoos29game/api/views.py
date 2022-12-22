from django.shortcuts import render
from django.http import HttpResponse


import json
from http import HTTPStatus
from django.http import JsonResponse, HttpResponse,HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.decorators import api_view

@csrf_exempt
@api_view(['GET'])
def hi(request):
    print("Sending back hello")
    response_data =json.dumps({"value":"hello"})
    return Response(response_data)

def home(request):
    return HttpResponse("This is the home page")

