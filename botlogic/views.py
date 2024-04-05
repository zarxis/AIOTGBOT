from aiogram.types import message


def start_bot_msg():
    return 'Бот запущен'


def stop_bot_msg():
    return 'Бот остановлен'


def about_message():
    return "Бот создан @Rognella"


def help_message():
    return """Помощь по доступным командам:
/start - запуск бота и регистрация пользователя
/get_file - получение файла с материалами к посту с канала
/help - помощь по доступным командам. Вы сейчас здесь 😉
/about - информация о боте"""


def help_chat_message():
    return """Помощь по доступным командам:
/help - помощь по доступным командам. Вы сейчас здесь 😉
/about - информация о боте"""


def join_message(first_name):
    return f"""Добро пожаловать в нашу группу, {first_name}!

Давай знакомиться. 

Расскажи немного о себе, своих увлечениях и о своём пути."""


def left_message(first_name):
    return f"""С прискорбием сообщаю, что {first_name} решил(а) покинуть наш уютный чатик.
    
(предатель(ница))"""
