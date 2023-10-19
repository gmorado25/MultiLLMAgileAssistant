from langchain.chat_models import ChatOpenAI
from .abstract_model import AbstractModel

class GPT_3_5(AbstractModel):

        def __init__(self) -> None:
            super().__init__(ChatOpenAI(model_name="gpt-3.5-turbo"))

class GPT4(AbstractModel):

        def __init__(self) -> None:
            super().__init__(ChatOpenAI(model_name="gpt-4"))
