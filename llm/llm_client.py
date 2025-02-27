from langchain_ollama import ChatOllama
from config.settings import settings

class LLMClient:
    def __init__(self):
        self.llm = ChatOllama(model=settings.LLM_MODEL)

    def query(self, prompt: str) -> str:
        response = self.llm.invoke(prompt)
        return response.content

llm_client = LLMClient()