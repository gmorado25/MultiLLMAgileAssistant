import json, requests
from requests.auth import HTTPBasicAuth

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

token = 'ATATT3xFfGF0i9GV4lt-5sc5ew5jQm-KFYBtSPCHVtbwgulYm_uSvsntKN1tVnGqZrvcqfKFLnUXtMuS9yaBMR4cP_24hArPBacCAr_IU6JN2mn0I-15Lf7qL1OXid-HJoRP83S7NnvthF8OZLUpH9qai0zygvckXyQgyqZOiuAuMQ9Tg7eY9Xk=862FC402'

@api_view(['POST'])
def getResource(request: Request) -> Response:

    request_url = request.data.get('url')
    request_headers = request.data.get('header')
    request_email = request.data.get('email')

    if (
        request_url is None or
        request_headers is None or
        request_email is None
    ):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    authentication = HTTPBasicAuth(request_email, token)
    jira_response = requests.request(
        method="GET", 
        url=request_url, 
        headers=request_headers,
        auth=authentication
    )

    return Response(jira_response.text)