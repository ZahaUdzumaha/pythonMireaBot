import json
import os
import random

from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import create_bot
from create_bot import dp


gameMenu = InlineKeyboardMarkup()
start_flip_button = InlineKeyboardButton('Подбросить монетку!', callback_data='start_flip_btn')
exit_flip_button = InlineKeyboardButton('Закончить игру', callback_data='exit_flip_btn')
gameMenu.add(start_flip_button)
gameMenu.add(exit_flip_button)

players = {}
players_points = {}


@dp.callback_query_handler(text='flip_btn')
async def flip_game_button_callback(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    await create_bot.bot.answer_callback_query(callback_query.id)
    photo = types.InputFile("coin/coin_flip.jpg")
    await callback_query.message.answer_photo(photo=photo, caption="Подбросить монтеку?", reply_markup=gameMenu)


@dp.callback_query_handler(text='start_flip_btn')
async def country_game_button_callback(callback_query: types.CallbackQuery):
    await create_bot.bot.answer_callback_query(callback_query.id)
    flip = random.randint(1, 2)
    if flip == 1:
        photo = types.InputFile("coin/орёл.jpg")
        await callback_query.message.answer_photo(photo=photo, caption='Выпал орёл!', reply_markup=gameMenu)
    else:
        photo = types.InputFile("coin/решка.jpg")
        await callback_query.message.answer_photo(photo=photo, caption='Выпала решка!', reply_markup=gameMenu)
    await create_bot.bot.delete_message(chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id)


@dp.callback_query_handler(text='exit_flip_btn')
async def country_game_button_callback(callback_query: types.CallbackQuery):
    await create_bot.bot.answer_callback_query(callback_query.id)
    await callback_query.message.answer("Игра окончена! \nДля вызова игрового меню нажмите(flip) /start")
    await create_bot.bot.delete_message(chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id)


def create_json(data):
    if os.path.exists("coin_flip_player_data.json"):
        return
    with open("coin_flip_player_data.json", "w") as write_file:
        json.dump(data, write_file)


def update_json(id, new_value):
    with open("coin_flip_player_data.json", "r") as write_file:
        data = dict(json.load(write_file))
    data[str(id)] = new_value
    with open("coin_flip_player_data.json", "w") as write_file:
        json.dump(data, write_file)