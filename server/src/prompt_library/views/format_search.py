from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from prompt_library.models import Format
from prompt_library.serializers import FormatSerializer

class FormatSearch(APIView):

    def get(self, request: Request, format=None) -> Response:
        query = request.query_params.get("format") or ""
        
        if (query is None or query == ""):
             return Response(status=status.HTTP_404_NOT_FOUND)
        
        try:
            formats = Format.objects.filter(title=query)

            # exact match --> should never be more than 1
            if (formats.count() > 1):
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            format = formats.first()

        except Format.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = FormatSerializer(format)
        return Response(serializer.data)
