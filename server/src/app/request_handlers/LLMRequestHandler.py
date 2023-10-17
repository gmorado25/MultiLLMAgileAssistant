from django.http import HttpResponse, HttpRequest, JsonResponse
from ..llm_communication import LLMManager

def getQueryResponses(request: HttpRequest) -> HttpResponse:
    system_prompt = "You are a helpful assistant who solves math problems. Write the following equation using algebraic symbols then show the steps to solve the problem:"
    user_input = "x^3 + 7 = 12"
    llms = ["Test"]
    responses = LLMManager.query(system_prompt, user_input, llms)
    return JsonResponse(responses)