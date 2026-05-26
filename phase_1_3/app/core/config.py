from dotenv import load_dotenv
import os

load_dotenv() # baca env

class Settings:
    APP_NAME = os.getenv("APP_NAME")
    DEBUG = os.getenv("DEBUG")

settings = Settings()