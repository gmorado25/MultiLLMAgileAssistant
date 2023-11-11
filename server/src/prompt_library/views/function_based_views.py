from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from prompt_library.models import Format, Prompt
from prompt_library.serializers import FormatSerializer, PromptSerializer

@api_view(['GET','POST'])
def prompt_list(request: Request, format=None) -> Response:

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
def prompt_detail(request: Request, id: int, format=None) -> Response:

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
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        prompt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@api_view(['GET'])
def format_list(request: Request, format=None) -> Response:
    formats = Format.objects.all().values('title')
    return Response([i['title'] for i in formats])
    
