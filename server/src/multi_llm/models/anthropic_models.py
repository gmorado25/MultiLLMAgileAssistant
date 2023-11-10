from langchain.chat_models import ChatAnthropic
from multi_llm.models.abstract_endpoint import AbstractEndpoint

class Claude2(AbstractEndpoint):

    def __init__(self, **kwargs) -> None:
        super().__init__(ChatAnthropic(**kwargs))