import random

from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text.lower().lower() == 'команды')
async def hug(message: Message):
    if message is not None:
        await message.answer(f'Вот мой весь список команд!\n'
                             f'╔Обнять - позволяет обнять пользователя\n'
                             f'╠Поцеловать - позволяет поцеловать пользователя\n'
                             f'╠Выебать - позволяет заняться хентаем с пользователем\n'
                             f'╠Отдаться - отдаетесь пользователю\n'
                             f'╠Пнуть - пинаете пользователя\n'
                             f'╠Дать пять - даеть пять пользователю\n'
                             f'╠Покормить - можете покормить пользователя\n'
                             f'╠Укусить - кусаете пользователя\n'
                             f'╠Взять - берете на руки пользователя\n'
                             f'╠Помохать - приветствуете пользователя\n'
                             f'╠Помоги - просите о помощи пользователя\n'
                             f'╠Чмокнуть - целуете вщеку пользователя\n'
                             f'╠Погладить - гладите пользователя\n'
                             f'╠Кусь - мягко кусаете пользователя\n'
                             f'╠Облизать - облизываете пользователя\n'
                             f'╠Облизать шею - облизываете шею пользователя\n'
                             f'╠Осудить - осуждаете действия пользователя\n'
                             f'╠Одобрить - одобряете действия пользователя\n'
                             f'╠Шлепнуть - шлепаете по попе пользователя\n'
                             f'╠Лапать - лапаете попец пользователя\n'
                             f'╠Гладить ушки - гладите ушки пользователя\n'
                             f'╠Съесть - кушаете кусочек пользователя\n'
                             f'╠Исцелить - исцеляете все повреждения пользователя\n'
                             f'╠Кастрировать - кастрируете пользователя\n'
                             f'╠Похоронить - проводите похороны пользователя\n'
                             f'╠Хоронить - заживо хороните пользователя\n'
                             f'╠Прятаться - прячетесь от пользователя\n'
                             f'╠Воскресить - воскрешаете из мертвых пользователя\n'
                             f'╠Отсосать - делаете омлет пользователю\n'
                             f'╠Цветочек - дарите цветочек пользователю! (будьте осторожны)\n'
                             f'╠Тык - тыкаете пользователя\n'
                             f'╠Оставить засос - оставляете засос! будьте осторожны!\n'
                             f'╠Жмакнуть - жмакаете грудь пользователя!\n'
                             f'╠Отлизать - лижите пользователю\n'
                             f'╚Убить - убиваете пользователя!\n')