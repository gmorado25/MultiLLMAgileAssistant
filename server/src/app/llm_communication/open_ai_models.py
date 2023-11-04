from langchain.chat_models import ChatOpenAI
from app.llm_communication.abstract_endpoint import AbstractEndpoint

class GPT(AbstractEndpoint):
    
    def __init__(self, **kwargs) -> None:
        super().__init__(ChatOpenAI(**kwargs))
