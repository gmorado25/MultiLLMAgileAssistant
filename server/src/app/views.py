from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django_nextjs.render import render_nextjs_page_sync

from django.http import HttpRequest
from .models import Prompt
from .serializers import PromptSerializer
from .llm_communication import llm_manager

def syncNextJS(request: HttpRequest) -> Response:
    return render_nextjs_page_sync(request)

@api_view(['GET'])
def llm_list(request: HttpRequest) -> Response:
    return Response(llm_manager.getModels())

@api_view(['GET','POST'])
def prompt_list(request: HttpRequest, format=None) -> Response:

    if request.method == 'GET':
        prompts = Prompt.objects.all()
        serializer = PromptSerializer(prompts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PromptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@api_view(['GET', 'PUT', 'DELETE'])
def prompt_detail(request: HttpRequest, id: int, format=None) -> Response:

    try:
        prompt = Prompt.objects.get(pk=id)
    except Prompt.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PromptSerializer(prompt)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PromptSerializer(prompt, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        prompt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
