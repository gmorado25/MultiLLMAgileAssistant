from typing import Any, Type

from .returning_thread import ReturningThread
from .abstract_endpoint import AbstractEndpoint
from .llm_response import LLMResponse

_instances: dict[str, AbstractEndpoint] = {}

""" -----------------------------------------------------------------------
Summary:
    Obtains an instance of the requested model and queries it with the
    given prompt and dataset.

Returns:
    Returns an LLMResponse object containing the model name and the 
    result.
----------------------------------------------------------------------- """ 
def _getResponse(prompt: str, dataset: str, model: str) -> LLMResponse:
        llm = _instances.get(model)
        output = llm.query(prompt, dataset)
        return LLMResponse(model, output)

""" -----------------------------------------------------------------------
Summary:
    Attempts the query the given llm with the prompt and user data.
    Returns the result or if an exception occurs it will return an error 
    as an LLMResponse.

Returns:
    Returns an LLMResponse object containing the model name and the 
    result.
----------------------------------------------------------------------- """ 
def _tryQuery(prompt: str, dataset: str, model: str) -> LLMResponse:
        try:
            return _getResponse(prompt, dataset, model)
        except Exception as error:
            msg = f"Error: cannot query LLM {model}." + \
                  "This can occur if the model has not been setup properly," + \
                  "or has been mispelled in the request. ->"
            print(msg, error, "\n\n")
            
            return LLMResponse(model, "An error has occured.")

""" -----------------------------------------------------------------------
Summary:
    Register and construct a new LLM endpoint with the LLM manager.

Args:
    name - the name of the model used to query it.
    model - the class type for the model.
    construction_args - arguments to pass to its construction.
----------------------------------------------------------------------- """ 
def registerModel(
        id: str, model: 
        Type[AbstractEndpoint], 
        model_kwargs: dict[str, Any]
    ):
    if (_instances.get(id) == None):
        _instances[id] = model(**model_kwargs)
    else:
        raise Exception(f"Model {id} is already registered.")

""" -----------------------------------------------------------------------
Summary:
    Returns a list of models currently set up in the manager.

Returns:
    Returns a list of strings for the names of available models.
----------------------------------------------------------------------- """ 
def getModels() -> list[str]:
    return list(_instances.keys())

""" -----------------------------------------------------------------------
Summary:
    Queries the requested llms with the given system prompt and dataset.
    Errors will be returned as the result for that model.

Parameters:
    prompt - the system prompt to give to the LLM.
    dataset - the user defined dataset to process.
    models - a list of the names of the models to be queried.

Returns:
    Returns an LLMResponse array containing query responses from each of 
    the requested LLMs.
----------------------------------------------------------------------- """ 
def query(prompt: str, dataset: str, models: list[str]) -> list[LLMResponse]:
    responses: list[LLMResponse] = []
    threads: list[ReturningThread] = []

    if (models is None):
        return[LLMResponse("Error", "No models are registered.")]
    
    for model in models:
        t = ReturningThread(target=_tryQuery, args=(prompt, dataset, model))
        threads.append(t)
        t.start()

    for thread in threads:
        result = thread.join()
        responses.append(result)

    return responses