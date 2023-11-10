from langchain.chat_models import ChatVertexAI
from multi_llm.models.abstract_endpoint import AbstractEndpoint

class ChatBison(AbstractEndpoint):
    
    def __init__(self, **kwargs) -> None:
        super().__init__(ChatVertexAI(**kwargs))

