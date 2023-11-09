from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpRequest
from multi_llm.util import llm_manager

@api_view(['GET'])
def models(request: HttpRequest) -> Response:
    return Response(llm_manager.getModels())