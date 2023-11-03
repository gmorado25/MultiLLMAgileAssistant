from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from ..llm_communication import llm_manager
from ..llm_communication.llm_response import LLMResponse

""" -----------------------------------------------------------------------
Summary:
    APIView to handler generation requests. Takes an Http POST request
    with a JSON message body with the following format:
    
    {
        "models": ["Model_1", "Model_2", "Model_3"],
        "prompt": "Put the system prompt here",
        "data": "Put the user input here"
    }

    where the models is a list of the model names to query (The list of
    available models can be retrieved from the url '../models/').

    The returned response will be a json array of each of the llm's
    responses in the form:

    [
        {
            "model": "Model1",
            "response": "The reponse generated by querying Model_1"
        },
        {
            "model": "Model2",
            "response": "The reponse generated by querying Model_2"
        },
        
        ...
    ]
----------------------------------------------------------------------- """ 
class LLMRequestHandler(APIView):

    def __packageLLMResults(self, results: list[LLMResponse]) -> list[dict[str, str]]:
        responses = []
        for result in results:
            responses.append(result.toDict())
        return responses

    def post(self, request: Request, format=None) -> Response:
        data = request.data
        models = data.get('models')

        # get each of the models to query, the prompt, and the dataset
        system_prompt = data.get('prompt')
        user_input = data.get('data')

        # query each llm and construct a list of dicts containing the responses
        results = llm_manager.query(system_prompt, user_input, models)
        response = self.__packageLLMResults(results)
        print(response)
        return Response(response)

# {
#     "models": ["Test", "GPT3.5", "GPT4", "Llama", "Bard", "Claude", "Test"],
#     "prompt": "You are a helpful assistant who solves math problems. Write the following equation using algebraic symbols then show the steps to solve the problem:",
#     "data": "x^3 + 7 = 12"
# }