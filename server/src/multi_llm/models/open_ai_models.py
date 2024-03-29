from langchain.chat_models import ChatOpenAI
from multi_llm.models.abstract_endpoint import AbstractEndpoint

class GPT(AbstractEndpoint):
    
    def __init__(self, **kwargs) -> None:
        super().__init__(ChatOpenAI(**kwargs))
