from django.http import JsonResponse

def process_request(request):
    # Process the request here
    data = {'response': 'Received the request successfully!'}
    return JsonResponse(data)
