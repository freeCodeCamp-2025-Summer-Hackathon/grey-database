import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    FLASK_ENV = os.getenv("FLASK_ENV", "dev")
    MONGODB_SETTINGS = {
        "host": os.getenv("MONGODB_URI"),
    }

