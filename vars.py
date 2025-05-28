# DON'T add anything here just add in render's secret or env section 
from os import environ

API_ID = int(environ.get("API_ID", "21484008"))
API_HASH = environ.get("API_HASH", "336734e723ed5c7824720449780bd00c")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
