import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
HEXAGRAMS_FILE = "data/hexagrams.json"
IMAGES_DIR = "images/"
USERS_DATA_FILE = "data/users_data.json"
COIN_IMAGE = "images/3coins.png"
