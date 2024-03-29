import importlib, json
from typing import Any
from pathlib import Path
from django.apps import AppConfig
from multi_llm.util import llm_manager
from multi_llm.models.abstract_endpoint import AbstractEndpoint
from app.settings import MODELS_CONFIG
class AppConfig(AppConfig):

    name = 'multi_llm'
    
    def __registerModel(self, model: dict[str, Any]) -> None:
        id = model['id']
        kwargs = model['args']
        model_class = self.__getClassFromPath(model['class'])
        llm_manager.registerModel(id, model_class, kwargs)

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
                try:
                    self.__registerModel(model)
                except Exception as error:
                    print(error)

    def ready(self) -> None:
        """
        Called once the application is loaded to perform startup tasks.
        """
        self.__registerModelsFromConfig(MODELS_CONFIG)