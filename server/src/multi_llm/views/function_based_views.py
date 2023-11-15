from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from multi_llm.util import llm_manager

@api_view(['GET'])
def models(request: Request, format=None) -> Response:
    return Response(llm_manager.getModels())