import json, os
from io import TextIOWrapper
from typing import Type
from threading import Thread

from .returning_thread import ReturningThread
from .abstract_endpoint import AbstractEndpoint
from .llm_response import LLMResponse

_instances: dict[str, AbstractEndpoint] = {}

""" -----------------------------------------------------------------------
Summary:
    Sets an environment variable from the given JSON object.

Returns:
    N/A
----------------------------------------------------------------------- """ 
def _setEnvironmentVariable(variable: dict[str, str]) -> None:
    # loop neccessary because object is a dict, but each
    # object passed in has only a single value
    for key, value in variable.items():
        os.environ[key] = value

""" -----------------------------------------------------------------------
Summary:
    Reads the given json file to parse each neccessary environment variable
    to be set up for authentication.

Returns:
    N/A
----------------------------------------------------------------------- """ 
def _readAuthFile(file: TextIOWrapper) -> None:
    try:
        credentials = json.load(file)
        for variable in credentials["environment_variables"]:
            _setEnvironmentVariable(variable)
    except Exception as error:
        print("Error reading authentication config:", error)

""" -----------------------------------------------------------------------
Summary:
    Initialization code to setup authentication for communications with
    the various LLMs in the system by reading the credentials config file.

Returns:
    N/A
----------------------------------------------------------------------- """ 
def _setupAuthentication() -> None:
    try:
        path = os.environ["PATH_AUTH_KEYS"]
        with open(path, "r") as credentialsFile:
            _readAuthFile(credentialsFile)
    except Exception as e:
        err = e.__str__()
        msg = f"Invalid credentials path -> {e}.\nPlease check" + \
            " the environment variable 'PATH_AUTH_KEYS'" + \
            " points to the location of the file storing" + \
            " authentication variables."
        print(msg)

""" -----------------------------------------------------------------------
Summary:
    Initialization code to setup each model available to the system.
    Establishes a dictionary mapping model names to the object responsible
    for communication with that LLM.

Returns:
    N/A
----------------------------------------------------------------------- """ 
def _setupModels(models: dict[str, Type[AbstractEndpoint]]) -> None:
    for name, model in models.items():
        try:
            _instances[name] = model()
        except Exception as error:
            print(f"Cannot set up LLM module {name}:", error)

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
    Returns a list of models currently set up in the manager.

Returns:
    Returns a list of strings for the names of available models.
----------------------------------------------------------------------- """ 
def getModels() -> list[str]:
    return list(_instances.keys())

""" -----------------------------------------------------------------------
Summary:
    Initializes each instance of the llm endpoints and sets up
    authorization from configuration. Must be called before the first time
    a service is queried.

Returns:
    N/A
----------------------------------------------------------------------- """ 
def init(models: dict[str, Type[AbstractEndpoint]]) -> None:
    if (len(_instances) == 0):
        _setupAuthentication()
        _setupModels(models)

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

    for model in models:
        t = ReturningThread(target=_tryQuery, args=(prompt, dataset, model))
        threads.append(t)
        t.start()

    for thread in threads:
        result = thread.join()
        responses.append(result)

    return responses