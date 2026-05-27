from openai import OpenAI
from app.core.config import settings
from app.providers.base import BaseProvider

class OpenAIProvider(BaseProvider):
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def chat(self, message: str) -> str:
        response = self.client.chat.completions.create(
           model="gpt-4o-mini",
           messages=[
              {"role": "user", "content": message}
           ]
        )
        return response.choices[0].message.content