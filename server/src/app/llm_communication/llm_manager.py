import json, os
from io import TextIOWrapper
from typing import Type
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
def query(prompt: str, dataset: str, models: list[str]) -> LLMResponse:
    responses: list[LLMResponse] = []
    for model in models:
        try:
            llm = _instances.get(model)
            output = llm.query(prompt, dataset)
            result = LLMResponse(model, output)
            responses.append(result)
        except Exception as error:
            print(f"Error in LLM {model}:", error)
            result = LLMResponse(model, "An error has occured.")
            responses.append(result)

    return responses