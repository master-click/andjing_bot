import json
import random
from config import HEXAGRAMS_FILE, IMAGES_DIR


class HexagramService:
    def __init__(self):
        with open(HEXAGRAMS_FILE, "r", encoding="utf-8") as f:
            self.hexagrams = json.load(f)

    def get_random_hexagram(self):
        return random.choice(self.hexagrams)

    def get_image_path(self, image_name):
        return f"{IMAGES_DIR}{image_name}"
