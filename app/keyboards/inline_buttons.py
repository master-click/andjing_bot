from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_start_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🪙 Бросить монетки",
                                  callback_data="cast_coins")]
        ]
    )
    return keyboard


def get_divination_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔮 Погадать еще",
                                  callback_data="divinate_again")]
        ]
    )
    return keyboard
