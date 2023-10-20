from langchain.chat_models import ChatVertexAI
from .abstract_model import AbstractModel

class ChatBison(AbstractModel):

        def __init__(self) -> None:
            super().__init__(ChatVertexAI(model_name="chat-bison"))

