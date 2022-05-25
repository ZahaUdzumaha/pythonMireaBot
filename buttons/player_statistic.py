import json
import os

from aiogram import types

import create_bot
from create_bot import dp


@dp.callback_query_handler(text='statistic_btn')
async def game_button_callback(callback_query: types.CallbackQuery):
    await create_bot.bot.answer_callback_query(callback_query.id)
    await create_bot.bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await callback_query.message.answer(text="Статистика игрока!")
    await callback_query.message.answer(text="В игре в страны вы максимально набирали: %d" % int(get_json()[str(callback_query.from_user.id)]))
    await callback_query.message.answer(text="Для вызова игрового меню нажмите /start")


def get_json():
    if not os.path.exists("country_player_data.json"):
        return
    with open("country_player_data.json", "r") as read_file:
        return json.load(read_file)
