from langchain.chat_models import ChatVertexAI
from app.llm_communication.abstract_endpoint import AbstractEndpoint

class ChatBison(AbstractEndpoint):
    
    def __init__(self, **kwargs) -> None:
        super().__init__(ChatVertexAI(**kwargs))

