from langchain.chat_models import ChatOpenAI
from . import Abstract_LLM_Model

class GPT_3_5(Abstract_LLM_Model.Endpoint):

        def __init__(self) -> None:
            super().__init__(ChatOpenAI(model_name="gpt-3.5-turbo"))

class GPT4(Abstract_LLM_Model.Endpoint):

        def __init__(self) -> None:
            super().__init__(ChatOpenAI(model_name="gpt-4"))
