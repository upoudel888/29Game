from django.http import HttpResponse,JsonResponse
from django.http import  HttpResponse,HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
import json
from . import utils



def home(request):
    return HttpResponse("This is the home page")

@csrf_exempt
def hi(request):
    if(request.method == 'GET'):
        return JsonResponse({"value":"hello"})

    # this sends 405 status code if any requests other than GET is made
    return HttpResponseNotAllowed(["GET"]) 


@csrf_exempt
def bid(request):
    if(request.method == 'POST'):
        data = json.loads(request.body)
        bid_response = utils.predictBidValue(data)
        return JsonResponse(bid_response)
    return HttpResponseNotAllowed(["POST"])

@csrf_exempt
def chooseTrump(request):
    if(request.method == "POST"):
        data = json.loads(request.body)
        trump_choice = utils.predictTrump(data)
        return JsonResponse(trump_choice)
    return HttpResponseNotAllowed(['POST'])

@csrf_exempt
def play(request):
    if(request.method == "POST"):
        data = json.loads(request.body)
        play_response = utils.predictPlay(data)
        return JsonResponse(play_response)
    return HttpResponseNotAllowed(['POST'])