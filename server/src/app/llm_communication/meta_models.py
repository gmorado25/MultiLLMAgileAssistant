from langchain.llms import LlamaCpp
from app.llm_communication.abstract_endpoint import AbstractEndpoint

class Llama2(AbstractEndpoint):

    def __init__(self, **kwargs) -> None:
        super().__init__(LlamaCpp(**kwargs))