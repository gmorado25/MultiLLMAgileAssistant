from io import TextIOWrapper
import json
import os
from server.multillm.llm_communication import Abstract_LLM_Model, OpenAIModels, GoogleModels, AnthropicModels, TestModel

_models: dict[str, Abstract_LLM_Model.Endpoint] = {}

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
        with open(os.environ["PATH_AUTH_KEYS"], "r") as credentialsFile:
            _readAuthFile(credentialsFile)
    except Exception as error:
        print("Invalid credentials path. Please check the environment variable 'PATH_AUTH_KEYS' points to the location of the file storing authentication variables.", error)
        credentialsFile.close()

""" -----------------------------------------------------------------------
Summary:
    Initialization code to setup each model available to the system.
    Establishes a dictionary mapping model names to the object responsible
    for communication with that LLM.

Returns:
    N/A
----------------------------------------------------------------------- """ 
def _setupModels() -> None:

    models = {
        "GPT3.5": OpenAIModels.GPT_3_5,
        "GPT4": OpenAIModels.GPT4,
        "Bard": GoogleModels.ChatBison,
        "Claude": AnthropicModels.Claude2
    }

    for name, model in models.items():
        try:
            _models[name] = model()
        except Exception as error:
            print(f"Error setting up LLM module {name}:", error)

    _models["Test"] = TestModel.MockInputModel("The answer is banana")

""" -----------------------------------------------------------------------
Summary:
    Queries the requested llms with the given system prompt and dataset.
    Errors will be returned as the response for that model.

Parameters:
    prompt - the system prompt to give to the LLM.
    dataset - the user defined dataset to process.
    models - a list of the names of the models to be queried.

Returns:
    Returns a dictionary mapping the name of the LLM with its recieved
    response parsed as a string.
----------------------------------------------------------------------- """ 
def query(prompt: str, dataset: str, models: list[str]) -> dict[str, str]:
    if (len(_models) == 0):
        _setupAuthentication()
        _setupModels()

    responses: dict[str, str] = {}
    for model in models:
        try:
            llm = _models.get(model)
            responses[model] = llm.query(prompt, dataset)
        except Exception as error:
            responses[model] = error

    return responses