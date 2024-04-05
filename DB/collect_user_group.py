import mysql.connector
import enum

from datetime import date, datetime, timedelta
from aiogram import Router, F
from aiogram.types import Message

router = Router()

config = {
    'user': 'root',
    'password': 'Rognella101',
    'host': '127.0.0.1',
    'database': 'DWARFS',
    'raise_on_warnings': True
}


class need_to_add(enum.Enum):
    nothing = 0
    chat_and_state = 1
    user_and_state = 2
    state = 3
    all = 4


@router.message(F.text.lower().lower() != '')
async def insert(message: Message):
    con = mysql.connector.connect(**config)
    cur = con.cursor()

    add_user = ("INSERT INTO users "
                "(user_id, first_name, last_name) "
                "VALUES (%s, %s, %s)")

    add_chat = ("INSERT INTO chats "
                "(chat_id, chat_name) "
                "VALUES (%s, %s)")

    add_states = ("INSERT INTO states "
                  "(mute, ban, user_id, chat_id, rule_id, date_add_user_to_group) "
                  "VALUES (%s, %s, %s, %s, %s, %s)")

    first_name = ''
    last_name = ''
    if message.from_user.username is not None:
        first_name = message.from_user.first_name
    if message.from_user.last_name is not None:
        last_name = message.from_user.last_name

    data_user = (message.from_user.id, first_name, last_name)

    chat_name = ''
    if message.chat.title is not None:
        chat_name = message.chat.title

    data_chat = (message.chat.id, chat_name)

    data_states = (date(1, 1, 1),
                   date(1, 1, 1),
                   message.from_user.id,
                   message.chat.id,
                   1,
                   datetime.now().date())

    if message.chat.id is not None and message.chat.id < 0:
        add_code = allready_exisist(message.from_user.id, message.chat.id)
        if add_code == need_to_add.nothing:
            pass
        elif add_code == need_to_add.all:
            #print(data_chat)
            cur.execute(add_chat, data_chat)
            #print(data_user)
            cur.execute(add_user, data_user)
            #print("________________________")
            con.commit()
            cur.execute(add_states, data_states)
            con.commit()
        elif add_code == need_to_add.user_and_state:
            #print(data_user)
            cur.execute(add_user, data_user)
            con.commit()
            #print("________________________")
            cur.execute(add_states, data_states)
            con.commit()
        elif add_code == need_to_add.chat_and_state:
            #print(data_chat)
            cur.execute(add_chat, data_chat)
            con.commit()
            #print("________________________")
            cur.execute(add_states, data_states)
            con.commit()
        elif add_code == need_to_add.state:
            cur.execute(add_states, data_states)
            con.commit()
    con.close()


def allready_exisist(user_id, chat_id):
    con = mysql.connector.connect(**config)
    cur = con.cursor()

    check_chat = ("SELECT * FROM chats WHERE chat_id = %s")
    check_chat_data = (chat_id,)
    cur.execute(check_chat, check_chat_data)
    result_chats = cur.fetchall()

    check_user = ("SELECT * FROM states WHERE user_id = %s")
    check_user_data = (user_id,)
    cur.execute(check_user, check_user_data)
    result_users = cur.fetchall()

    if result_chats and result_users:
        check_States = ("SELECT * FROM states WHERE user_id = %s and chat_id = %s")
        check_States_data = (user_id, chat_id)
        cur.execute(check_States, check_States_data)
        result = cur.fetchall()

        if not result:
            return need_to_add.state
            con.close()
        else:
            return need_to_add.nothing
        con.close()
    elif not result_chats and result_users:
        return need_to_add.chat_and_state
        con.close()
    elif result_chats and not result_users:
        return need_to_add.user_and_state
        con.close()
    else:
        return need_to_add.all
        con.close()
