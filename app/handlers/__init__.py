from .start import start_handler
from .divination import coin_cast_handler, prepare_divination
from aiogram import F


def register_handlers(dp):
    dp.message.register(start_handler, F.text == "/start")
    dp.callback_query.register(coin_cast_handler, F.data == "cast_coins")
    dp.callback_query.register(prepare_divination, F.data == "divinate_again")
    dp.message.register(coin_cast_handler, F.text)
