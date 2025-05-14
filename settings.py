from dotenv import load_dotenv
from os import getenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    base_url: str = 'https://www.saucedemo.com/v1'
    username: str = getenv("USER_NAME")
    password: str = getenv("PASSWORD")  
