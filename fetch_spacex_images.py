import requests
import json
import argparse
from load_helpers import load_image
from load_helpers import get_expansion


def create_parser():
    parser = argparse.ArgumentParser(description="Скачивает фотографии запуска ракет SpaceX")
    parser.add_argument('launch_number', nargs='?', default='50', type=int, help="Номер запуска SpaceX")
    return parser


def fetch_spacex_launch(launch):
    response = requests.get(f"https://api.spacexdata.com/v3/launches/{launch}")
    response.raise_for_status()   
    for image_number, image in enumerate(response.json()['links']['flickr_images']):
        load_image(image, f'images/spacex_{image_number}{get_expansion(image)}')
        

if __name__ == "__main__":
    parser = create_parser()
    launch_args = parser.parse_args()
    launch = launch_args.launch_number
    fetch_spacex_launch(launch)
    
