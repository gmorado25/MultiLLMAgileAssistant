from django.http import HttpResponse, HttpRequest

def getQueryResponses(request: HttpRequest) -> HttpResponse:
    return HttpResponse("hello world")