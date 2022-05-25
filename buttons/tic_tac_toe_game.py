from aiogram import types
import random
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from create_bot import dp
import create_bot

gameMenu = InlineKeyboardMarkup()
first_button = InlineKeyboardButton('1', callback_data='tic_tac_toe_btn1')
second_button = InlineKeyboardButton('2', callback_data='tic_tac_toe_btn2')
third_button = InlineKeyboardButton('3', callback_data='tic_tac_toe_btn3')
fourth_button = InlineKeyboardButton('4', callback_data='tic_tac_toe_btn4')
fifth_button = InlineKeyboardButton('5', callback_data='tic_tac_toe_btn5')
sixth_button = InlineKeyboardButton('6', callback_data='tic_tac_toe_btn6')
seventh_button = InlineKeyboardButton('7', callback_data='tic_tac_toe_btn7')
eighth_button = InlineKeyboardButton('8', callback_data='tic_tac_toe_btn8')
ninth_button = InlineKeyboardButton('9', callback_data='tic_tac_toe_btn9')
end_game = InlineKeyboardButton("Закончить игру 🏳️", callback_data='end_tic_tac_game')
gameMenu.add(first_button, second_button, third_button)
gameMenu.add(fourth_button, fifth_button, sixth_button)
gameMenu.add(seventh_button, eighth_button, ninth_button)
gameMenu.add(end_game)
first_line = ["1️⃣", "2️⃣", "3️⃣"]
second_line = ["4️⃣", "5️⃣", "6️⃣"]
third_line = ["7️⃣", "8️⃣", "9️⃣"]
winner_text = "Игра продолжается!"
turn = 1


@dp.callback_query_handler(text='tic_tac_toe_btn')
async def game_button_callback(callback_query: types.CallbackQuery):
    await create_bot.bot.answer_callback_query(callback_query.id)
    first_line = ["1️⃣", "2️⃣", "3️⃣"]
    second_line = ["4️⃣", "5️⃣", "6️⃣"]
    third_line = ["7️⃣", "8️⃣", "9️⃣"]
    await callback_query.message.answer(text=first_line)
    await callback_query.message.answer(text=second_line)
    await callback_query.message.answer(text=third_line)
    await callback_query.message.answer(text="Игра в крестики нолики!", reply_markup=gameMenu)


@dp.callback_query_handler(text='tic_tac_toe_btn1')
async def game_button_callback(callback_query: types.CallbackQuery):
    await create_bot.bot.answer_callback_query(callback_query.id)
    if first_line[0] == "1️⃣":
        first_line[0] = "X"
        winner()
        await callback_query.message.answer(text=first_line)
        await callback_query.message.answer(text=second_line)
        await callback_query.message.answer(text=third_line)
    else:
        await callback_query.message.answer(text="Невозможный ход!")
    if winner_text == "Вы проиграли!" or winner_text == "Вы победили!" or winner_text == "Ничья!":
        await callback_query.message.answer(text=winner_text)
        await callback_query.message.answer("Игра окончена! \nДля вызова игрового меню нажмите(tic-tac) /start")
    else:
        await callback_query.message.answer(text=winner_text, reply_markup=gameMenu)


@dp.callback_query_handler(text='tic_tac_toe_btn2')
async def game_button_callback(callback_query: types.CallbackQuery):
    await create_bot.bot.answer_callback_query(callback_query.id)
    if first_line[1] == "2️⃣":
        first_line[1] = "X"
        winner()
        await callback_query.message.answer(text=first_line)
        await callback_query.message.answer(text=second_line)
        await callback_query.message.answer(text=third_line)
    else:
        await callback_query.message.answer(text="Невозможный ход!")
    if winner_text == "Вы проиграли!" or winner_text == "Вы победили!" or winner_text == "Ничья!":
        await callback_query.message.answer(text=winner_text)
        await callback_query.message.answer("Игра окончена! \nДля вызова игрового меню нажмите(tic-tac) /start")
    else:
        await callback_query.message.answer(text=winner_text, reply_markup=gameMenu)


@dp.callback_query_handler(text='tic_tac_toe_btn3')
async def game_button_callback(callback_query: types.CallbackQuery):
    await create_bot.bot.answer_callback_query(callback_query.id)
    if first_line[2] == "3️⃣":
        first_line[2] = "X"
        winner()
        await callback_query.message.answer(text=first_line)
        await callback_query.message.answer(text=second_line)
        await callback_query.message.answer(text=third_line)
    else:
        await callback_query.message.answer(text="Невозможный ход!")
    if winner_text == "Вы проиграли!" or winner_text == "Вы победили!" or winner_text == "Ничья!":
        await callback_query.message.answer(text=winner_text)
        await callback_query.message.answer("Игра окончена! \nДля вызова игрового меню нажмите(tic-tac) /start")
    else:
        await callback_query.message.answer(text=winner_text, reply_markup=gameMenu)


@dp.callback_query_handler(text='tic_tac_toe_btn4')
async def game_button_callback(callback_query: types.CallbackQuery):
    await create_bot.bot.answer_callback_query(callback_query.id)
    if second_line[0] == "4️⃣":
        second_line[0] = "X"
        winner()
        await callback_query.message.answer(text=first_line)
        await callback_query.message.answer(text=second_line)
        await callback_query.message.answer(text=third_line)
    else:
        await callback_query.message.answer(text="Невозможный ход!")
    if winner_text == "Вы проиграли!" or winner_text == "Вы победили!" or winner_text == "Ничья!":
        await callback_query.message.answer(text=winner_text)
        await callback_query.message.answer("Игра окончена! \nДля вызова игрового меню нажмите(tic-tac) /start")
    else:
        await callback_query.message.answer(text=winner_text, reply_markup=gameMenu)


@dp.callback_query_handler(text='tic_tac_toe_btn5')
async def game_button_callback(callback_query: types.CallbackQuery):
    await create_bot.bot.answer_callback_query(callback_query.id)
    if second_line[1] == "5️⃣":
        second_line[1] = "X"
        winner()
        await callback_query.message.answer(text=first_line)
        await callback_query.message.answer(text=second_line)
        await callback_query.message.answer(text=third_line)
    else:
        await callback_query.message.answer(text="Невозможный ход!")
    if winner_text == "Вы проиграли!" or winner_text == "Вы победили!" or winner_text == "Ничья!":
        await callback_query.message.answer(text=winner_text)
        await callback_query.message.answer("Игра окончена! \nДля вызова игрового меню нажмите(tic-tac) /start")
    else:
        await callback_query.message.answer(text=winner_text, reply_markup=gameMenu)


@dp.callback_query_handler(text='tic_tac_toe_btn6')
async def game_button_callback(callback_query: types.CallbackQuery):
    await create_bot.bot.answer_callback_query(callback_query.id)
    if second_line[2] == "6️⃣":
        second_line[2] = "X"
        winner()
        await callback_query.message.answer(text=first_line)
        await callback_query.message.answer(text=second_line)
        await callback_query.message.answer(text=third_line)
    else:
        await callback_query.message.answer(text="Невозможный ход!")
    if winner_text == "Вы проиграли!" or winner_text == "Вы победили!" or winner_text == "Ничья!":
        await callback_query.message.answer(text=winner_text)
        await callback_query.message.answer("Игра окончена! \nДля вызова игрового меню нажмите(tic-tac) /start")
    else:
        await callback_query.message.answer(text=winner_text, reply_markup=gameMenu)


@dp.callback_query_handler(text='tic_tac_toe_btn7')
async def game_button_callback(callback_query: types.CallbackQuery):
    await create_bot.bot.answer_callback_query(callback_query.id)
    if third_line[0] == "7️⃣":
        third_line[0] = "X"
        winner()
        await callback_query.message.answer(text=first_line)
        await callback_query.message.answer(text=second_line)
        await callback_query.message.answer(text=third_line)
    else:
        await callback_query.message.answer(text="Невозможный ход!")
    if winner_text == "Вы проиграли!" or winner_text == "Вы победили!" or winner_text == "Ничья!":
        await callback_query.message.answer(text=winner_text)
        await callback_query.message.answer("Игра окончена! \nДля вызова игрового меню нажмите(tic-tac) /start")
    else:
        await callback_query.message.answer(text=winner_text, reply_markup=gameMenu)


@dp.callback_query_handler(text='tic_tac_toe_btn8')
async def game_button_callback(callback_query: types.CallbackQuery):
    await create_bot.bot.answer_callback_query(callback_query.id)
    if third_line[1] == "8️⃣":
        third_line[1] = "X"
        winner()
        await callback_query.message.answer(text=first_line)
        await callback_query.message.answer(text=second_line)
        await callback_query.message.answer(text=third_line)
    else:
        await callback_query.message.answer(text="Невозможный ход!")
    if winner_text == "Вы проиграли!" or winner_text == "Вы победили!" or winner_text == "Ничья!":
        await callback_query.message.answer(text=winner_text)
        await callback_query.message.answer("Игра окончена! \nДля вызова игрового меню нажмите(tic-tac) /start")
    else:
        await callback_query.message.answer(text=winner_text, reply_markup=gameMenu)


@dp.callback_query_handler(text='tic_tac_toe_btn9')
async def game_button_callback(callback_query: types.CallbackQuery):
    await create_bot.bot.answer_callback_query(callback_query.id)
    if third_line[2] == "9️⃣":
        third_line[2] = "X"
        winner()
        await callback_query.message.answer(text=first_line)
        await callback_query.message.answer(text=second_line)
        await callback_query.message.answer(text=third_line)
    else:
        await callback_query.message.answer(text="Невозможный ход!")
    if winner_text == "Вы проиграли!" or winner_text == "Вы победили!" or winner_text == "Ничья!":
        await callback_query.message.answer(text=winner_text)
        await callback_query.message.answer("Игра окончена! \nДля вызова игрового меню нажмите(tic-tac) /start")
    else:
        await callback_query.message.answer(text=winner_text, reply_markup=gameMenu)


@dp.callback_query_handler(text='end_tic_tac_game')
async def game_button_callback(callback_query: types.CallbackQuery):
    await create_bot.bot.answer_callback_query(callback_query.id)
    await callback_query.message.answer("Игра окончена! \nДля вызова игрового меню нажмите(tic-tac) /start")
    await create_bot.bot.delete_message(chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id)


def winner():
    lines_free = [3, 3, 3]
    first_line_free = [0, 1, 2]
    second_line_free = [0, 1, 2]
    third_line_free = [0, 1, 2]
    turns_left = 9
    global winner_text
    for i in range(3 - 1, -1, -1):
        if first_line[i] == "X" or first_line[i] == "0":
            turns_left -= 1
            first_line_free.pop(i)
            lines_free[i] -= 1
        if second_line[i] == "X" or second_line[i] == "0":
            turns_left -= 1
            second_line_free.pop(i)
            lines_free[i] -= 1
        if third_line[i] == "X" or third_line[i] == "0":
            turns_left -= 1
            third_line_free.pop(i)
            lines_free[i] -= 1

    if turns_left != 0:
        max_on_line = max(lines_free)
        prefer_line = lines_free.count(max_on_line)
        rnd = random.randint(1, prefer_line)
        for i in range(3):
            k = 0
            if lines_free[i] == prefer_line:
                k += 1
                if k == rnd:
                    prefer_line = i + 1

        if prefer_line == 1:
            rnd = random.randint(0, len(first_line_free) - 1)
            first_line[first_line_free[rnd]] = "0"
        if prefer_line == 2:
            rnd = random.randint(0, len(second_line_free) - 1)
            second_line[second_line_free[rnd]] = "0"
        if prefer_line == 3:
            rnd = random.randint(0, len(third_line_free) - 1)
            third_line[third_line_free[rnd]] = "0"
    #➡️
    if first_line[0] == first_line[1] == first_line[2] == "X":
        winner_text = "Вы победили!"
    elif first_line[0] == first_line[1] == first_line[2] == "0":
        winner_text = "Вы проиграли!"

    if second_line[0] == second_line[1] == second_line[2] == "X":
        winner_text = "Вы победили!"
    elif second_line[0] == second_line[1] == second_line[2] == "0":
        winner_text = "Вы проиграли!"

    if third_line[0] == third_line[1] == third_line[2] == "X":
        winner_text = "Вы победили!"
    elif third_line[0] == third_line[1] == third_line[2] == "0":
        winner_text = "Вы проиграли!"
    #⬆️
    if first_line[0] == second_line[0] == third_line[0] == "X":
        winner_text = "Вы победили!"
    elif first_line[0] == second_line[0] == third_line[0] == "0":
        winner_text = "Вы проиграли!"

    if first_line[1] == second_line[1] == third_line[1] == "X":
        winner_text = "Вы победили!"
    elif first_line[1] == second_line[1] == third_line[1] == "0":
        winner_text = "Вы проиграли!"

    if first_line[2] == second_line[2] == third_line[2] == "X":
        winner_text = "Вы победили!"
    elif first_line[2] == second_line[2] == third_line[2] == "0":
        winner_text = "Вы проиграли!"
    #↘️
    if first_line[0] == second_line[1] == third_line[2] == "X":
        winner_text = "Вы победили!"
    elif first_line[0] == second_line[1] == third_line[2] == "0":
        winner_text = "Вы проиграли!"

    #↗️
    if first_line[2] == second_line[1] == third_line[0] == "X":
        winner_text = "Вы победили!"
    elif first_line[2] == second_line[1] == third_line[0] == "0":
        winner_text = "Вы проиграли!"

    #🤝
    if turns_left == 0:
        winner_text = "Ничья!"