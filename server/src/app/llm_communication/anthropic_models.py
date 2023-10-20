from langchain.chat_models import ChatAnthropic
from .abstract_model import AbstractModel

class Claude2(AbstractModel):

        def __init__(self) -> None:
            super().__init__(ChatAnthropic(model_name="claude-2"))