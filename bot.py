import logging
import sys

import asyncio
from distutils.cmd import Command

from aiogram import Dispatcher, Router
from aiogram.filters import ChatMemberUpdatedFilter, IS_NOT_MEMBER, IS_MEMBER
from aiogram.methods import DeleteWebhook

from user import rpelements, mini
from user import commands_all
from DB import collect_user_group

from botlogic.settings import bot
from botlogic.handlers.events import stop_bot, start_bot, on_user_join, on_user_left

router = Router()
dp = Dispatcher()


async def main():
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.chat_member.register(on_user_join, ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
    dp.chat_member.register(on_user_left, ChatMemberUpdatedFilter(IS_MEMBER >> IS_NOT_MEMBER))
    
    dp.include_routers(
        rpelements.router,
        mini.router,
        commands_all.router,
        collect_user_group.router
    )
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
