from aiogram.types import ChatMemberUpdated

from botlogic.settings import bot, Secrets
from botlogic.utils.commands import set_commands
from botlogic import views

async def start_bot():
    await bot.send_message(Secrets.admin_id, views.start_bot_msg())


async def stop_bot():
    await bot.send_message(Secrets.admin_id, views.stop_bot_msg())


async def on_user_join(event: ChatMemberUpdated):
    #print(event)
    await event.answer(views.join_message(event.new_chat_member.user.first_name))


async def on_user_left(event: ChatMemberUpdated):
    #print(event)
    await event.answer(views.left_message(event.new_chat_member.user.first_name))