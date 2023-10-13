from django.shortcuts import render
from django.http import JsonResponse
from django import *

def process_request(request):
    # Process the request here
    data = {'response': 'Received the request successfully!'}
    return JsonResponse(data)

