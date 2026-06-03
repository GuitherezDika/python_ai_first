from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    APP_NAME = os.getenv("APP_NAME", "AI Gateway")

settings = Settings()