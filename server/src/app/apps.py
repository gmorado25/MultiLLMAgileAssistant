from django.apps import AppConfig
from .llm_communication import llm_manager as LLMManager
from.llm_communication.test_model import MockInputModel
from .llm_communication.open_ai_models import GPT_3_5
from .llm_communication.google_models import ChatBison
from .llm_communication.anthropic_models import Claude2
from pathlib import Path
import os

# avoid calling paid APIs for regular testing until we are ready for integration
# use the test model for now; invoked with the same interface as the real ones
models = {
    "Test": MockInputModel,
    #"GPT3.5": GPT_3_5,       
    #"Bard": ChatBison,
    #"Claude": Claude2
}

config = "config/mock-config.json" #"credentials/authentication-config.json"

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    root_dir = Path(__file__).resolve().parent.parent.parent
    path = root_dir.joinpath(config)
    os.environ["PATH_AUTH_KEYS"] = str(path)

    try:
        LLMManager.init(models)
    except Exception as error:
        print(error)