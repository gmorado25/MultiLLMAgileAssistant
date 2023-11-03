from langchain.llms import LlamaCpp
from .abstract_endpoint import AbstractEndpoint

class LLama(AbstractEndpoint):

    def __init__(self, **kwargs) -> None:
        super().__init__(LlamaCpp(**kwargs))