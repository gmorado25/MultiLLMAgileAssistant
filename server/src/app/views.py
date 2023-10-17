from django.http import HttpResponse, HttpRequest, JsonResponse
from .request_handlers import LLMRequestHandler

def process_request(request: HttpRequest) -> JsonResponse:
    # Process the request here
    data = {'response': 'Received the request successfully!'}
    return JsonResponse(data)

def llm_output(request: HttpRequest) -> HttpResponse:
    return LLMRequestHandler.getQueryResponses(request)