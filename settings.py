from os import environ
from dotenv import load_dotenv

load_dotenv('.env')

CLIENT_ID = environ["CLIENT_ID"] 
CLIENT_SECRET = environ["CLIENT_SECRET"] 
REDDIT_NAME = environ["REDDIT_NAME"] 
PASSWORD = environ["PASSWORD"] 
USER_AGENT = environ["USER_AGENT"] 
