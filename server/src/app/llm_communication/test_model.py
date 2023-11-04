from langchain.llms.fake import FakeListLLM
from app.llm_communication.abstract_endpoint import AbstractEndpoint

class MockInputModel(AbstractEndpoint):

    def __init__(self, **kwargs) -> None:
        super().__init__(None)
        self.response = kwargs.get('response')
        self.model_name = kwargs.get('model_name')

    """ -----------------------------------------------------------------------
    Summary:
        Queries the Mock LLM with the provided system prompt and dataset. Mock
        llm returns the question and query info as its response.
    
    Parameters:
        prompt - a string containing the system prompt to provide to the model.
        dataset - the user data or question to be processed by the model.

    Returns:
        Returns a mock response from the query.
    ----------------------------------------------------------------------- """ 
    def query(self, prompt: str, dataset: str) -> str:
        response = self.response or \
            f"[*] Mock model invoked: {self.model_name}\n" \
          + f"[*] System Prompt: {prompt}\n" \
          + f"[*] Dataset: {dataset}\n"
        
        self._model = FakeListLLM(responses=[response])
        return super().query(prompt, dataset)
