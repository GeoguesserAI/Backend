from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse, JsonResponse
from GeoguesserAI.scripts.guess import *
import json

@csrf_exempt
def send_image(request: HttpRequest):
    if request.method == "POST":

        data = json.loads(request.body.decode('utf-8'))

        return HttpResponse(status=200)

    else:
        return HttpResponse(status=400)

def random_guess(request: HttpRequest):
    if request.method == "POST":

        data = json.loads(request.body.decode('utf-8'))
        lat = -1.45217
        long = 21.28040

        guess = Guess()
        guess.create_guess(data['url'], lat, long)
        
        response = guess.make_guess()
        if response == True:
            print("Guess Success!")
            return HttpResponse(status=200)
        else:
            print("Guess Unsuccessful!")
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=400)

@csrf_exempt
def test_response(request: HttpRequest):
    if request.method == "GET":

        print("hello")

        return HttpResponse(status=200)
    
    else:
        return HttpResponse(status=400)