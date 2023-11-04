from langchain.chat_models import ChatAnthropic
from app.llm_communication.abstract_endpoint import AbstractEndpoint

class Claude2(AbstractEndpoint):

    def __init__(self, **kwargs) -> None:
        super().__init__(ChatAnthropic(**kwargs))