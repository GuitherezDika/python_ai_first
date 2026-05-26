from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    APP_NAME = os.getenv("APP_NAME", "AI Gateway")
    # akan cari env.APP_NAME kalau tidak ada -> default value = AI Gateway

settings = Settings()