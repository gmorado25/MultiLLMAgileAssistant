from io import TextIOWrapper
import json, os, sys

from pathlib import Path
from django.apps import AppConfig
from server.src.app.llm_communication import llm_manager as LLMManager
from server.src.multillm.settings import CONFIG_DIR

class AppConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

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

    def __registerModelsFromConfig() -> None:
        """Load LLM model configuration from file"""
        with open(CONFIG_DIR) as model_config:
            models = json.load(model_config)
            for model in models:
                id = model['id']
                model_class = getattr(sys.modules[__name__], model['class'])
                kwargs = model['args']
                LLMManager.registerModel(id, model_class, kwargs)

    def ready(self) -> None:
        """Called once the application is loaded."""
        root_dir = Path(__file__).resolve().parent.parent.parent
        path = root_dir.joinpath(self.config_path)

        try:
            self.__setupAuth(str(path))

            # avoid calling paid APIs for regular testing until we are ready for integration
            # use the test model for now; invoked with the same interface as the real ones
            self.__registerModelsFromConfig()

        except Exception as error:
            print(error)
        



            # llama_args = {
            #     "model_path": "C:\\Users\\Ryan\\Desktop\\Dev. Projects\\LLama\\llama-2-13b-chat.Q5_K_M.gguf",
            #     "n_gpu_layers": 50,     # num layers to offload to GPU      -> -1 = use all available
            #     "n_ctx": 2048,          # Context size                      -> smaller = faster, but worse generation
            #     "n_batch": 512,         # VRAM usage                        -> batch size
            #     "n_thread": None,       # number of cpu threads             -> None = automatically determine 
            # }
            # LLMManager.registerModel(id="Llama", model=LLama, model_kwargs=llama_args)
            #LLMManager.registerModel(id="GPT3.5", model=GPT, model_kwargs={"model_name": "gpt-3.5-turbo"})
            #LLMManager.registerModel(id="Bard", model=ChatBison, model_kwargs={"model_name": "chat-bison"})
            #LLMManager.registerModel(id="Claude", model=Claude2, model_kwargs={"model_name": "claude-2"})
            #LLMManager.registerModel(id="Llama", model=None, model_kwargs={"model_name": "llama"})