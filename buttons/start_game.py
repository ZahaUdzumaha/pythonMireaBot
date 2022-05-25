import aiogram
from aiogram import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

mainMenu = InlineKeyboardMarkup()
statistic_button = InlineKeyboardButton('Статистика игрока', callback_data='statistic_btn')
tic_tac_toe_button = InlineKeyboardButton('Крестики нолики', callback_data='tic_tac_toe_btn')
country_button = InlineKeyboardButton('Игра в \"угадай чей флаг\"', callback_data='country_btn')
flip_button = InlineKeyboardButton('Подбросить монетку', callback_data='flip_btn')

mainMenu.add(statistic_button)
mainMenu.add(tic_tac_toe_button)
mainMenu.add(country_button)
mainMenu.add(flip_button)


async def start(message: aiogram.types.Message):
    await message.answer("Получится ли у тебя победить этого бота? Я думаю у тебя нет шансов!", reply_markup=mainMenu)


def register(dispatcher: Dispatcher):
    dispatcher.register_message_handler(start, regexp_commands=['start'])