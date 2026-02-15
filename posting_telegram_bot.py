import telegram
import imghdr
import os
import random
import time
import argparse
from dotenv import load_dotenv
from environs import env
from pathlib import Path
from load_helpers import reduces_the_image


def create_parser():
    parser = argparse.ArgumentParser(description="Запускает Telegram бота по загрузке фотографий с нужным интервалом")
    parser.add_argument('hours', nargs='?', default='4', type=float, help="Интервал между загрузками фотографий в часах")
    return parser


def launch_upload_bot(interval, token, chat_id):
    bot = telegram.Bot(token=token)
    absolute_path = Path('images').resolve()
    image_names = []
    folder = Path('images')
    for file in folder.iterdir():
    	image_names.append(absolute_path / file.name)
    while True:
        for name in image_names:
            name = reduces_the_image(name)
            with open(name, 'rb') as photo:
                bot.send_photo(chat_id=chat_id, photo=photo)
            time.sleep(interval)
        image_names = random.shuffle(image_names, len(image_names))


if __name__ == "__main__":
    second_in_hour = 3600
    load_dotenv()
    token = env.str("POSTING_TELEGRAM_BOT_API_KEY")
    chat_id = env.str("TELEGRAM_CHAT_ID")
    parser = create_parser()
    interval_space = parser.parse_args()
    interval = second_in_hour * interval_space.hours
    launch_upload_bot(interval, token, chat_id)