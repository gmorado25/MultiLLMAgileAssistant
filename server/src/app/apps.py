import importlib, json

from pathlib import Path
from django.apps import AppConfig
from app.llm_communication import llm_manager as LLMManager

class AppConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    config_path = 'config/llm-models.json'
    
    # avoid calling paid APIs for regular testing until we are ready for integration
    # use the test model for now; invoked with the same interface as the real ones
    def __registerModelsFromConfig(self, path: str) -> None:
        """Load LLM model configuration from file"""
        with open(path) as model_config:
            models = json.load(model_config)
            for model in models:
                id = model['id']
                model_path: str = model['class']
                kwargs = model['args']

                module_name, class_name = model_path.rsplit(".", 1)
                module = importlib.import_module(module_name)
                model_class = getattr(module, class_name)
                
                LLMManager.registerModel(id, model_class, kwargs)

    def ready(self) -> None:
        """Called once the application is loaded."""
        root_dir = Path(__file__).resolve().parent.parent.parent
        path = root_dir.joinpath(self.config_path)

        try:
            self.__registerModelsFromConfig(str(path))

        except Exception as error:
            print(error)

        # {
        #     "id": "Bard",
        #     "class": "app.llm_communication.google_models.ChatBison",
        #     "args": {
        #         "model_name": "chat-bison"
        #     }
        # },
        # {
        #     "id": "Claude",
        #     "class": "app.llm_communication.anthropic_models.Claude2",
        #     "args": {
        #         "model_name": "claude-2"
        #     }
        # },
        # {
        #     "id": "GPT3.5",
        #     "class": "app.llm_communication.open_ai_models.GPT",
        #     "args": {
        #         "model_name": "gpt-3.5-turbo"
        #     }
        # },