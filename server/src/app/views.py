from django.http import HttpRequest, JsonResponse
from .request_handlers import llm_request_handler as LLMRequestHandler
from rest_framework.decorators import api_view

def process_request(request: HttpRequest) -> JsonResponse:
    # Process the request here
    data = {'response': 'Received the request successfully!'}
    return JsonResponse(data)

@api_view(['POST'])
def llm_output(request: HttpRequest) -> JsonResponse:
    return LLMRequestHandler.getQueryResponses(request)