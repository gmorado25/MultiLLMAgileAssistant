from langchain.llms.fake import FakeListLLM
from langchain.schema.output_parser import StrOutputParser
from server.multillm.llm_communication import Abstract_LLM_Model

class MockInputModel(Abstract_LLM_Model.Endpoint):

        def __init__(self, output: str) -> None:
            super().__init__(FakeListLLM(responses=[output]))

