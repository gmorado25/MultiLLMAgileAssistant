from langchain.llms.fake import FakeListLLM
from . import Abstract_LLM_Model

class MockInputModel(Abstract_LLM_Model.Endpoint):

    def __init__(self) -> None:
        super().__init__(None)

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
        response = f"Response for mock llm model {self}:\n\n" + "[SYSTEM PROMPT]: \"" \
            + prompt + "\"\n[DATASET]: \"" + dataset + "\""
        
        self._model = FakeListLLM(responses=[response])
        return super().query(prompt, dataset)
