from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse, JsonResponse
import json

@csrf_exempt
def send_image(request: HttpRequest):
    if request.method == "POST":

        data = json.loads(request.body.decode('utf-8'))
        print(data)

        return HttpResponse(status=200)

    else:
        return HttpResponse(status=400)

def test(request: HttpRequest):
    if request.method == "GET":

        print("hello")

        return HttpResponse(status=200)
    
    else:
        return HttpResponse(status=400)