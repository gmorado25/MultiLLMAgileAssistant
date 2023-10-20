import json
from django.http import HttpResponse, HttpRequest, JsonResponse
from ..llm_communication import llm_manager
from ..llm_communication.llm_response import LLMResponse

def _parseModels(list: list[str]) -> list[str]:
    models = []
    if list is not None:
        for item in list:
            models.append(item['Name'])
    return models

def _packageLLMResults(results: list[LLMResponse]) -> list[dict[str, str]]:
    responses = []
    for result in results:
        responses.append(result.toDict())
    return responses

def getQueryResponses(request: HttpRequest) -> HttpResponse:
    data = request.data
    models_list = data.get('models')

    # get each of the models to query, the prompt, and the dataset
    models = _parseModels(models_list)
    system_prompt = data.get('prompt')
    user_input = data.get('data')

    # query each llm and construct a list of dicts containing the responses
    llm_results = llm_manager.query(system_prompt, user_input, models)
    response = _packageLLMResults(llm_results)
    return JsonResponse(response, safe=False)



# {
#     "models": [
#         {"Name": "GPT3.5"},
#         {"Name": "Bard"},
#         {"Name": "Claude"},
#         {"Name": "Test"}
#     ],
#     "prompt": "You are a helpful assistant who solves math problems. Write the following equation using algebraic symbols then show the steps to solve the problem:",
#     "data": "x^3 + 7 = 12"
# }