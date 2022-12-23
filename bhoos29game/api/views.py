from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

import json
from django.http import  HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import utils


def home(request):
    return HttpResponse("This is the home page")

@csrf_exempt
@api_view(['GET'])
def hi(request):
    return JsonResponse({"value":"hello"})


@csrf_exempt
@api_view(['POST','GET'])
def bid(request):
    bid_response = utils.predictBidValue(request.data)
    return JsonResponse(bid_response)

@api_view(['POST','GET'])
def chooseTrump(request):
    trump_choice = utils.predictTrump(request.data)
    return JsonResponse(trump_choice)

@api_view(['POST','GET'])
def play(request):
    play_response = utils.predictPlay(request.data)
    return JsonResponse(play_response)