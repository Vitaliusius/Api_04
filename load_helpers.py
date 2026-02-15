
import requests
import os
import json
from PIL import Image
from pathlib import Path

def reduces_the_image(path):
    image = Image.open(path)
    image.thumbnail((2200, 1600))
    image.save(path)
    return path


def load_image(url, path):
    os.makedirs("images", exist_ok=True)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def get_expansion(url):
    expansion = os.path.splitext(url)[-1]
    return expansion
