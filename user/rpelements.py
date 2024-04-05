import random

from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text.lower().lower() == 'обнять')
async def hug(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'нежно обнял '
                             f'{userTo}')
    else:
        await message.answer("Что бы обнять, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower().lower() == "поцеловать")
async def kiss(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'поцеловал по франзуски  '
                             f'{userTo}')
    else:
        await message.answer("Что бы поцеловать, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "выебать")
async def fuck(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'занялся жестким хентаем с '
                             f'{userTo}')
    else:
        await message.answer("Что бы выебать, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "отдаться")
async def givefuck(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'медленно кладет руку {userTo} на свой бюст, '
                             f'невзначай намекая что ему дозволено все')
    else:
        await message.answer("Что бы отдаться, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "пнуть")
async def kick(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'пнул '
                             f'{userTo}')
    else:
        await message.answer("Что бы пнуть, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "дать пять")
async def hifive(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'дал пять '
                             f'{userTo}')
    else:
        await message.answer("Что бы дать пять, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "покормить")
async def feed(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'покормил с ложечки  '
                             f'{userTo}')
    else:
        await message.answer("Что бы покормить, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "укусить")
async def bite(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'укусил '
                             f'{userTo}')
    else:
        await message.answer("Что бы укусить, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "взять")
async def take(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'взял на руки '
                             f'{userTo}')
    else:
        await message.answer("Что бы взять, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "помахать")
async def hi(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'поздоровался c '
                             f'{userTo}')
    else:
        await message.answer("Что бы помахать, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "помоги")
async def helpme(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'просит помощи у '
                             f'{userTo}')
    else:
        await message.answer("Что бы попросить о помощи, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "чмокнуть")
async def kiss2(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'чмокнул '
                             f'{userTo}')
    else:
        await message.answer("Что бы чмокнуть, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "погладить")
async def stroke(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'погладил '
                             f'{userTo}')
    else:
        await message.answer("Что бы погладить, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "кусь")
async def kus(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'кусьнул '
                             f'{userTo}')
    else:
        await message.answer("Что бы кусьнуть, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "облизать")
async def lick(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'облизал '
                             f'{userTo}')
    else:
        await message.answer("Что бы облизать, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "облизать шею")
async def necklick(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'облизал шею '
                             f'{userTo}')
    else:
        await message.answer("Что бы облизать шею, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "осудить")
async def blame(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'осуждает действия '
                             f'{userTo}')
    else:
        await message.answer("Что бы осудить, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "одобрить")
async def approve(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'одобряет действия '
                             f'{userTo}')
    else:
        await message.answer("Что бы одобрить, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "шлепнуть")
async def slap(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'шлёпнул по жопе '
                             f'{userTo}')
    else:
        await message.answer("Что бы шлепнуть, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "лапать")
async def touch(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'лапает жопку '
                             f'{userTo}')
    else:
        await message.answer("Что бы лапать, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "гладить ушки")
async def ears(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'жамкает ушки '
                             f'{userTo}')
    else:
        await message.answer("Что бы гладить ушки, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "съесть")
async def eat(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'съел кусочек '
                             f'{userTo}')
    else:
        await message.answer("Что бы съесть, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "исцелить")
async def heal(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        if message.from_user.id == message.reply_to_message.from_user.id:
            if message.from_user.username == 'Rognella':
                await message.answer(f'{userFrom} смог исцелить себя!')
            elif message.from_user.username != 'Rognella':
                await message.answer(f'{userFrom} Попроси себя исцелить!')
        elif message.from_user.id != message.reply_to_message.from_user.id:
            await message.answer(f'{userFrom} исцелил {userTo}')
    else:
        await message.answer("Что исцелить, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "кастрировать")
async def castrate(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'кастрировал '
                             f'{userTo}')
    else:
        await message.answer("Что бы кастрировать, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "иди нахуй")
async def naxui(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'шлет нахуй '
                             f'{userTo}')
    else:
        await message.answer("Что бы послать, нужно выбрать цель (Ответь на сообщение цели) и отправить иди нахуй")


@router.message(F.text.lower() == "похоронить")
async def bury(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} '
                             f'проводит похороны '
                             f'{userTo}')
    else:
        await message.answer("Что бы похоронить, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "хоронить")
async def burya(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} заживо хоронит '
                             f'{userTo} к сожалению он не может кричать')
    else:
        await message.answer("Что бы хоронить, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "прятаться")
async def hide(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} пытается спрятаться... '
                             f'кажется удалось...'
                             f'{userTo} ты ослеп?')
    else:
        await message.answer("Что бы прятаться, нужно выбрать цель (Ответь на сообщение цели) от которой прячетесь")


@router.message(F.text.lower() == "воскресить")
async def resurect(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} воскресил {userTo}')
    else:
        await message.answer("Что бы воскресить, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "отсосать")
async def suckd(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} нежно взял гениталии '
                             f'{userTo} и медленно начал их сосать')
    else:
        await message.answer("Что бы отсосать, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "цветочек")
async def flower(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        rand = random.randint(1, 100)
        if rand < 50:
            await message.answer(f'{userFrom} нашел цветочек пренадлежащий '
                                 f'{userTo} возможно это намек...')
        elif rand > 50:
            await message.answer(f'{userFrom} нашел цветочек пренадлежащий '
                                 f'{userTo}... '
                                 f'Соболеезнуем {userFrom}, ведь цветочек принадлежит садисту')
    else:
        await message.answer("Что бы вернуть цветочек, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "тык")
async def poke(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} активно тыкает '
                             f'{userTo} пытаясь щекотать! '
                             f'Главное не в мягое место... ')
    else:
        await message.answer("Что бы тыкнуть, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == "оставить засос")
async def hickey(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        rand = random.randint(1, 100)
        if rand < 50:
            await message.answer(f'{userFrom} оставил засос '
                                 f'{userTo}, кажется это было вкусно...')
        elif rand > 50:
            await message.answer(f'{userFrom} выпил всюкровь '
                                 f'{userTo} ой...')
    else:
        await message.answer("Что бы оставить оставить засос, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == 'жмакнуть')
async def chew(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} нежно прикасается к груди {userTo}, \n '
                             f'{userTo} медленно вздрагивает... \n'
                             f'кажется {userTo} получает удовольствие')
    else:
        await message.answer("Что бы оставить оставить засос, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == 'отлизать')
async def plick(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        await message.answer(f'{userFrom} медленно раздвинул ножки {userTo}, \n '
                             f'{userTo} медленно вздрагивает... \n'
                             f'кажется {userTo} ощущает что-то мягкое и на своем лоно...')
    else:
        await message.answer("Что бы отлизать, нужно выбрать цель (Ответь на сообщение цели)")


@router.message(F.text.lower() == 'убить')
async def kill(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        if message.from_user.id == message.reply_to_message.from_user.id:
            await message.answer(f'{userFrom} совершает сэппуку')
        else:
            await message.answer(f'{userFrom} убивает с особым пристрастием {userTo}')
    else:
        await message.answer("Что бы отлизать, нужно выбрать цель (Ответь на сообщение цели)")


# -------------------------------------------------


@router.message(F.text.lower() == "лера обнять")
async def lerahug(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        if message.from_user.username == 'Pr0ct0_Lera':
            await message.answer(f'{userFrom} обвила руками шею, '
                                 f'прижавшись всем телом к {userTo}')
        else:
            await message.answer(f'Простите данная команда доступна только @Pr0ct0_Lera')
    else:
        pass


@router.message(F.text.lower() == "полина засос")
async def polina(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        if message.from_user.username == 'Ich_Ihr_Anbieter':
            rand = random.randint(1, 100)
            if rand < 50:
                await message.answer(f'{userFrom} оставил на шее '
                                     f'{userTo} засос продолжая целовать того шею..Спасите его от поцелуев!')
            elif rand > 50:
                await message.answer(f'{userFrom} выпил всюкровь '
                                     f'{userTo} ой...')
        else:
            await message.answer(f'Простите данная команда доступна только для @Ich_Ihr_Anbieter')
    else:
        pass


@router.message(F.text.lower() == "амина убить")
async def amina(message: Message):
    if message is not None and message.reply_to_message is not None:
        userFrom = message.from_user.mention_html()
        userTo = message.reply_to_message.from_user.mention_html()
        if message.from_user.username == 'Qisertb':
            rand = random.randint(1, 100)
            if rand < 50:
                await message.answer(f'{userFrom} достал осторожно нож бабочку и осторожно вонзил его в '
                                     f'{userTo} . К сожалению шансев выжить было мало.')
            elif rand > 50:
                await message.answer(f'{userFrom} ошибся потайным карманом и вытащил 357 magnum. '
                                     f'Теперь {userTo} сложно опознать...')
        else:
            await message.answer(f'Простите данная команда доступна только для @Qisertb')
    else:
        pass
