
import logging
import os
from dataclasses import dataclass

from aiogram import Bot

# Логгер
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter(
    "%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

'''file_handler = logging.FileHandler("logs.txt")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)'''

logger.addHandler(console_handler)
#logger.addHandler(file_handler)


@dataclass
class Secrets:
    token: str = 'yourkey'
    admin_id: int = #your id


bot = Bot(token=Secrets.token, parse_mode='HTML')

