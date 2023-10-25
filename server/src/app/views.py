from django.http import HttpRequest, JsonResponse
from .models import Prompt
from .serializers import PromptSerializer
from .llm_communication import llm_manager
import re
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django_nextjs.render import render_nextjs_page_sync

def syncNextJS(request: HttpRequest) -> Response:
    return render_nextjs_page_sync(request)

@api_view(['GET'])
def llm_list(request: HttpRequest) -> Response:
    return Response(llm_manager.getModels())

@api_view(['GET','POST'])
def prompt_list(request: HttpRequest) -> Response:

    if request.method == 'GET':
        prompts = Prompt.objects.all()
        serializer = PromptSerializer(prompts, many=True)
        return JsonResponse({'prompts':serializer.data})
    
    elif request.method == 'POST':
        serializer = PromptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'PUT', 'DELETE'])
def prompt_id(request: HttpRequest, id) -> Response:

    try:
        prompt = Prompt.objects.get(pk=id)
    except Prompt.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PromptSerializer(prompt)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        #serializer = PromptSerializer(drink,)
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@api_view(['GET'])
def prompt_attributes(request: HttpRequest, attributes: str) -> Response:
    role = ""
    phase = ""

    # attempt to split multiple attributes passed in
    params = attributes.split("&")

    #must be valid 'role' or 'sdlc_phase'
    for item in params:
        if (re.search("^sdlc_phase=", item)):
            phase = item.split("=")[1]
        elif (re.search("^role=", item)):
            role = item.split("=")[1]
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        prompts = Prompt.objects.filter(role__icontains=role, sdlc_phase__icontains=phase)
    except Prompt.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = PromptSerializer(prompts, many=True)
    return JsonResponse({'prompts':serializer.data})
