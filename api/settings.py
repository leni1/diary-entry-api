import os

from dotenv import load_dotenv

from api.database.store import diary_entry_db

load_dotenv()

FLASK_ENV = os.getenv("FLASK_ENV")
FLASK_APP = os.getenv("FLASK_APP")
DATABASE = diary_entry_db
