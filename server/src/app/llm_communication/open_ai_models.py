from langchain.chat_models import ChatOpenAI
from .abstract_endpoint import AbstractEndpoint

class GPT_3_5(AbstractEndpoint):

        def __init__(self) -> None:
            super().__init__(ChatOpenAI(model_name="gpt-3.5-turbo"))

class GPT4(AbstractEndpoint):

        def __init__(self) -> None:
            super().__init__(ChatOpenAI(model_name="gpt-4"))
