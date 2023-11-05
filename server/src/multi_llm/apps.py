import importlib, json

from pathlib import Path
from django.apps import AppConfig
from multi_llm.util import llm_manager
from multi_llm.models.abstract_endpoint import AbstractEndpoint

class AppConfig(AppConfig):

    name = 'multi_llm'
    models_config = 'config/llm-models.json'
    
    def __getClassFromPath(self, path: str) -> AbstractEndpoint:
        """
        Get a reference to the given class from its module path.

        Args:
            path (str) - the path to the requested class.
        """
        module_name, class_name = path.rsplit(".", 1)
        module = importlib.import_module(module_name)
        return getattr(module, class_name)

    def __registerModelsFromConfig(self, path: str) -> None:
        """
        Load LLM model configuration from the given file.
        
        Args:
            path (str) - the file path to open and read.
        """
        with open(path) as config:
            models = json.load(config)
            for model in models:
                id = model['id']
                kwargs = model['args']
                model_class = self.__getClassFromPath(model['class'])
                llm_manager.registerModel(id, model_class, kwargs)

    def ready(self) -> None:
        """
        Called once the application is loaded to perform startup tasks.
        """
        root_dir = Path(__file__).resolve().parent.parent.parent
        path = root_dir.joinpath(self.models_config)

        try:
            self.__registerModelsFromConfig(str(path))

        except Exception as error:
            print(error)