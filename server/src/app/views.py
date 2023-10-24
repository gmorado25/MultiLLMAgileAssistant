from django.http import HttpRequest, JsonResponse
from .request_handlers import llm_request_handler as LLMRequestHandler
from rest_framework.decorators import api_view
from .models import Prompt
from .serializers import PromptSerializer
from rest_framework.response import Response
from rest_framework import status

# def process_request(request: HttpRequest) -> JsonResponse:
#     # Process the request here
#     data = {'response': 'Received the request successfully!'}
#     return JsonResponse(data)

@api_view(['GET','POST'])
def prompt_list(request):

    if request.method == 'GET':
        prompts = Prompt.objects.all()
        serializer = PromptSerializer(prompts, many=True)
        return JsonResponse({'prompts':serializer.data})
    
    if request.method == 'POST':
        serializer = PromptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def llm_output(request: HttpRequest) -> JsonResponse:
    return LLMRequestHandler.getQueryResponses(request)

@api_view(['GET', 'PUT', 'DELETE'])
def prompt_detail(request, id):

    try:
        prompt = Prompt.objects.get(pk=id)
    except Prompt.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PromptSerializer(prompt)
        return Response(serializer.data)
    elif request.method == 'POST':
        #serializer = PromptSerializer(drink,)
        pass
    elif request.method == 'DELETE':
        pass
    