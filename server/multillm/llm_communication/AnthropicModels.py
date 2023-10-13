from langchain.chat_models import ChatAnthropic
from server.multillm.llm_communication import Abstract_LLM_Model

class Claude2(Abstract_LLM_Model.Endpoint):

        def __init__(self) -> None:
            super().__init__(ChatAnthropic(model_name="claude-2"))