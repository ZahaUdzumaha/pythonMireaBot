import json
import os
import random
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import create_bot
import parsing
from create_bot import dp

players = {}
players_btn = {}
players_points = {}


@dp.callback_query_handler(text='country_btn')
async def country_game_button_callback(callback_query: types.CallbackQuery):
    await create_bot.bot.answer_callback_query(callback_query.id)
    await callback_query.message.answer(text="🏛 Игра \"угадай чей флаг\" vs ZahaUdzumaha`s bot 🏛")
    result = add_keyboard_with_images(callback_query)
    await callback_query.message.answer_photo(photo=parsing.get_image("", result[1]),
                                              reply_markup=result[0],
                                              caption="Правильно угаданных стран: %d" % players_points[
                                                  callback_query.from_user.id])
    create_json({})


@dp.callback_query_handler(text='answer_btn1')
async def country_game_button1_callback(callback_query: types.CallbackQuery):
    await create_bot.bot.answer_callback_query(callback_query.id)
    if players[callback_query.from_user.id] == players_btn[callback_query.from_user.id][0]:
        players_points[callback_query.from_user.id] += 1
    else:
        players_points[callback_query.from_user.id] -= 1
    await callback_query.message.delete()
    result = add_keyboard_with_images(callback_query)
    await callback_query.message.answer_photo(photo=parsing.get_image("", result[1]),
                                              reply_markup=result[0],
                                              caption="Правильно угаданных стран: %d" % players_points[
                                                  callback_query.from_user.id])


@dp.callback_query_handler(text='answer_btn2')
async def country_game_button2_callback(callback_query: types.CallbackQuery):
    await create_bot.bot.answer_callback_query(callback_query.id)
    if players[callback_query.from_user.id] == players_btn[callback_query.from_user.id][1]:
        players_points[callback_query.from_user.id] += 1
    else:
        players_points[callback_query.from_user.id] -= 1
    await callback_query.message.delete()
    result = add_keyboard_with_images(callback_query)
    await callback_query.message.answer_photo(photo=parsing.get_image("", result[1]),
                                              reply_markup=result[0],
                                              caption="Правильно угаданных стран: %d" % players_points[
                                                  callback_query.from_user.id])


@dp.callback_query_handler(text='answer_btn3')
async def country_game_button3_callback(callback_query: types.CallbackQuery):
    await create_bot.bot.answer_callback_query(callback_query.id)
    if players[callback_query.from_user.id] == players_btn[callback_query.from_user.id][2]:
        players_points[callback_query.from_user.id] += 1
    else:
        players_points[callback_query.from_user.id] -= 1
    await callback_query.message.delete()
    result = add_keyboard_with_images(callback_query)
    await callback_query.message.answer_photo(photo=parsing.get_image("", result[1]),
                                              reply_markup=result[0],
                                              caption="Правильно угаданных стран: %d" % players_points[
                                                  callback_query.from_user.id])


@dp.callback_query_handler(text='answer_btn4')
async def country_game_button4_callback(callback_query: types.CallbackQuery):
    await create_bot.bot.answer_callback_query(callback_query.id)
    if players[callback_query.from_user.id] == players_btn[callback_query.from_user.id][3]:
        players_points[callback_query.from_user.id] += 1
    else:
        players_points[callback_query.from_user.id] -= 1
    await callback_query.message.delete()
    result = add_keyboard_with_images(callback_query)
    await callback_query.message.answer_photo(photo=parsing.get_image("", result[1]),
                                              reply_markup=result[0],
                                              caption="Правильно угаданных стран: %d" % players_points[
                                                  callback_query.from_user.id])


@dp.callback_query_handler(text='end_country_game')
async def country_game_end_button_callback(callback_query: types.CallbackQuery):
    await create_bot.bot.answer_callback_query(callback_query.id)
    if players_points[callback_query.from_user.id] > int(get_json()[str(callback_query.from_user.id)]):
        update_json(callback_query.from_user.id, players_points[callback_query.from_user.id])

    await callback_query.message.answer("Игра окончена! Результат: %d" % players_points[callback_query.from_user.id])
    await callback_query.message.delete()

    players_points[callback_query.from_user.id] = 0


def add_keyboard_with_images(callback_query: types.CallbackQuery):
    answer_menu = InlineKeyboardMarkup()
    ids = random.sample(range(0, 192), 4)
    answer_id = ids[int(random.uniform(0, 4))]
    first_answer = InlineKeyboardButton(parsing.get_json()[ids[0]], callback_data='answer_btn1')
    second_answer = InlineKeyboardButton(parsing.get_json()[ids[1]], callback_data='answer_btn2')
    third_answer = InlineKeyboardButton(parsing.get_json()[ids[2]], callback_data='answer_btn3')
    fourth_answer = InlineKeyboardButton(parsing.get_json()[ids[3]], callback_data='answer_btn4')
    end_country_game = InlineKeyboardButton("Закончить игру 🏳️", callback_data='end_country_game')
    answer_menu.add(first_answer, second_answer)
    answer_menu.add(third_answer, fourth_answer)
    answer_menu.add(end_country_game)

    name = parsing.get_json()[answer_id]
    players[callback_query.from_user.id] = parsing.get_json()[answer_id]
    players_btn[callback_query.from_user.id] = list(
        [parsing.get_json()[ids[0]], parsing.get_json()[ids[1]],
         parsing.get_json()[ids[2]], parsing.get_json()[ids[3]]])
    try:
        players_points[callback_query.from_user.id]
    except KeyError:
        players_points[callback_query.from_user.id] = 0

    return [answer_menu, name]


def create_json(data):
    if os.path.exists("country_player_data.json"):
        return
    with open("country_player_data.json", "w") as write_file:
        json.dump(data, write_file)


def update_json(id, new_value):
    with open("country_player_data.json", "r") as write_file:
        data = dict(json.load(write_file))
    data[str(id)] = new_value
    with open("country_player_data.json", "w") as write_file:
        json.dump(data, write_file)


def get_json():
    if not os.path.exists("country_player_data.json"):
        return
    with open("country_player_data.json", "r") as read_file:
        return json.load(read_file)
