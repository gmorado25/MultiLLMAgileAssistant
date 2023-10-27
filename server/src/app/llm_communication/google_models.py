from langchain.chat_models import ChatVertexAI
from .abstract_endpoint import AbstractEndpoint

class ChatBison(AbstractEndpoint):

        def __init__(self) -> None:
            super().__init__(ChatVertexAI(model_name="chat-bison"))

