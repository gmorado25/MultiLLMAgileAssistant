from django.apps import AppConfig
from .llm_communication import LLMManager, TestModel
from pathlib import Path
import os

models = {
    "Test": TestModel.MockInputModel
    # "GPT3.5": OpenAIModels.GPT_3_5,       # avoid calling paid APIs for regular testing until we are ready for integration
    # "GPT4": OpenAIModels.GPT4,            # use the test model for now; invoked with the same interface as the real ones
    # "Bard": GoogleModels.ChatBison,
    # "Claude": AnthropicModels.Claude2
}

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    root_dir = Path(__file__).resolve().parent.parent.parent
    path = root_dir.joinpath("credentials/mock-config.json")
    os.environ["PATH_AUTH_KEYS"] = str(path)

    try:
        LLMManager.init(models)
    except Exception as error:
        print(error)