from langchain.chat_models.base import BaseChatModel
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

class AbstractEndpoint:

    """ -----------------------------------------------------------------------
    Summary:
        Constructs and returns the response chain to handle and parse queries
        and answers from the LLM model.

    Returns:
        Returns 
    ----------------------------------------------------------------------- """ 
    def _setupChain(self, prompt: str, dataset: str) -> LLMChain:
        if (self._model is None):
            raise Exception(f"Error: No endpoint defined in attribute '_model' for {self}.\n")
        
        input = ChatPromptTemplate.from_messages([
            ("system", prompt),
            ("human", dataset)
        ])
        return input | self._model | StrOutputParser()

    """ -----------------------------------------------------------------------
    Summary:
        Initialization code to setup the LangChain llm. Deriving classes
        should pass the chat model to use during construction.

    Returns:
        N/A
    ----------------------------------------------------------------------- """ 
    def __init__(self, model: BaseChatModel) -> None:
        self._model = model

    """ -----------------------------------------------------------------------
    Summary:
        Queries the LLM with the provided system prompt and dataset to be
        processed.
    
    Parameters:
        prompt - a string containing the system prompt to provide to the model.
        dataset - the user data or question to be processed by the model.

    Returns:
        Returns a string containing the completion of the prompt generated
        by the LLM.
    ----------------------------------------------------------------------- """ 
    def query(self, prompt: str, dataset: str) -> str:
        llm_chain = self._setupChain(prompt, dataset)
        return llm_chain.invoke({})