from io import TextIOWrapper
import json
from pathlib import Path
import os

from django.apps import AppConfig

from .llm_communication import llm_manager as LLMManager
from .llm_communication.test_model import MockInputModel
from .llm_communication.open_ai_models import GPT
from .llm_communication.google_models import ChatBison
from .llm_communication.anthropic_models import Claude2

class AppConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    config_path = "config/mock-config.json"

    def __setEnvironmentVariable(self, variable: dict[str, str]) -> None:
        """
        Summary:
            Sets an environment variable from the given JSON object.

        Args:
            variable (dict[str, str]) - the list of environment variables
                and their values to sett.
        
        Returns:
            N/A
        """ 
        for key, value in variable.items():
            os.environ[key] = value

    def __readAuthFile(self, file: TextIOWrapper) -> None:
        """
        Summary:
            Reads the given json file to parse each neccessary environment variable
            to be set up for authentication.

        Returns:
            N/A
        """ 
        try:
            credentials = json.load(file)
            for variable in credentials["environment_variables"]:
                self.__setEnvironmentVariable(variable)
        except Exception as error:
            print("Error reading authentication config:", error)

    def __setupAuth(self, path: str) -> None:
        """
        Summary:
            Initialization code to setup authentication for communications with
            the various LLMs in the system by reading the credentials config file.

        Args:
            path (str) - the path to the applcation config file.

        Returns:
            N/A
        """ 
        try:
            with open(path, "r") as credentialsFile:
                self.__readAuthFile(credentialsFile)
        except Exception as e:
            msg = f"Invalid credentials path -> {e}.\nPlease check " + \
                   "the environment variable 'PATH_AUTH_KEYS' " + \
                   "points to the location of the file storing " + \
                   "authentication variables."
            print(msg)

    def ready(self) -> None:
        """Called once the application is loaded."""
        root_dir = Path(__file__).resolve().parent.parent.parent
        path = root_dir.joinpath(self.config_path)

        try:
            self.__setupAuth(str(path))

            # avoid calling paid APIs for regular testing until we are ready for integration
            # use the test model for now; invoked with the same interface as the real ones
            
            # An example of registering a model with the manager. 
            # "id" is the tag used to identify and query the model later
            # "model" is the class type to construct
            # "model_kwargs" is a dictionary of arguments to conctrust the class with
            args = {
                "model_name": "test-model",
                "response": "Hello!"
            }
            LLMManager.registerModel(id="Test", model=MockInputModel, model_kwargs=args)

            #LLMManager.registerModel(id="GPT3.5", model=GPT, model_kwargs={"model_name": "gpt-3.5-turbo"})
            #LLMManager.registerModel(id="Bard", model=ChatBison, model_kwargs={"model_name": "chat-bison"})
            #LLMManager.registerModel(id="Claude", model=Claude2, model_kwargs={"model_name": "claude-2"})
            #LLMManager.registerModel(id="Llama", model=None, model_kwargs={"model_name": "llama"})

        except Exception as error:
            print(error)
        