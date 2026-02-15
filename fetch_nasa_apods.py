import requests
import os
import json
from dotenv import load_dotenv
from environs import env
from load_helpers import load_image
from load_helpers import get_expansion


def fetch_nasa_apod(token):
    params = {
        'api_key': token,
        'start_date': '2026-01-25',
    }
    response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
    response.raise_for_status()
    for image_number, image in enumerate(response.json()):
        load_image(image['url'], f'images/nasa_apod_{image_number}{get_expansion(image)}')


if __name__ == "__main__":
    load_dotenv()
    token = env.str("NASA_API_KEY")
    demo_token = env.str("NASA_API_DEMO_KEY")
    try:
        fetch_nasa_apod(token)
    except requests.exceptions.HTTPError:
        fetch_nasa_apod(demo_token)