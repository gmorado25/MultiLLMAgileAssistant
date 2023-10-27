from langchain.chat_models import ChatAnthropic
from .abstract_endpoint import AbstractEndpoint

class Claude2(AbstractEndpoint):

        def __init__(self) -> None:
            super().__init__(ChatAnthropic(model_name="claude-2"))