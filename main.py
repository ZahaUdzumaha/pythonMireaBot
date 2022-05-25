
from aiogram.utils import executor

import parsing
from buttons import start_game
from create_bot import dp

if __name__ == '__main__':
    parsing.country_parsing()
    start_game.register(dp)
    executor.start_polling(dp, skip_updates=True)