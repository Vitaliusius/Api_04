import telegram
import imghdr
import os
import random
import argparse
from dotenv import load_dotenv
from environs import env
from pathlib import Path
from load_helpers import reduces_the_image


def create_parser():
    parser = argparse.ArgumentParser(description="Загружает фотографию в Telegram-канал")
    parser.add_argument('name', nargs='?', default=None, type=str, help="Название файла с фотографией")
    return parser


def upload_image(photo_name, token, chat_id):
    bot = telegram.Bot(token=token)
    photo_name = reduces_the_image(photo_name)
    with open(photo_name, 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)


if __name__ == "__main__":
    load_dotenv()
    token = env.str("POSTING_TELEGRAM_BOT_API_KEY")
    chat_id = env.str("TELEGRAM_CHAT_ID")
    absolute_path = Path('images').resolve()
    image_names = []
    folder = Path('images')
    for file in folder.iterdir():
        image_names.append(absolute_path / file.name)
    parser = create_parser()
    name_space = parser.parse_args()
    if name_space.name:
        photo_name = (absolute_path / name_space.name)
    else:
        photo_name = random.choice(image_names)
    try:
        upload_image(photo_name, token, chat_id)
    except FileNotFoundError:
        print("Неправильное имя файла")