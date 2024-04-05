import random

from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text.lower() == "выстрел")
async def GunGame(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        rand = random.randint(1, 100)
        if rand <= 33:
            await message.answer(f'{userFrom} стреляет в {userTo}, но не попадает в {userTo} '
                                 f'{userFrom} сходи в тир ')
        elif rand <= 66:
            await message.answer(f'{userFrom} стреляет в {userTo}, и ранит {userTo}, '
                                 f'{userFrom}, а ты не плох ')
        elif rand <= 100:
            await message.answer(f'{userFrom} стреляет и попадает в {userTo}, '
                                  f'{userFrom} убивает {userTo} стоит, задуматься над своими действиями ')
    else:
        await message.answer("Что бы сделать выстрел, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "повесить")
async def hang(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        rand = random.randint(1, 100)
        if rand <= 33:
            await message.answer(f'{userFrom} приговаривает к смерти {userTo} через повешание \n'
                                 f'{userTo} занимался гимнастикой, расставив ноги он застрял в отверстии\n')
        elif rand <= 66:
            await message.answer(f'{userFrom} приговаривает к смерти {userTo} через повешание \n'
                                 f'{userTo} удачно раскачался до этого на веревке и уверенно '
                                 f'зацепился ногами за опору.\n')
        elif rand <= 100:
            await message.answer(f'{userFrom} приговаривает к смерти {userTo} через повешание \n'
                                 f'{userTo} не успел ничего предпринять и окончил свою жизнь')
    else:
        await message.answer("Что бы повесить, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "укоротить аппарат")
async def minimize(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        rand = random.randint(1, 10)
        if message.reply_to_message.from_user.username == 'Rognella':
            await message.answer(f'{userFrom} укоротил свой аппарат на {rand} см')
        else:
            await message.answer(f'{userFrom} укоротил аппарат {userTo} на {rand} см')