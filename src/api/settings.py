from os import environ
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Settings:
    # General Flask config
    SECRET_KEY = environ.get("SECRET_KEY")

    # DATABASE
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
