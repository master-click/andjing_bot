from aiogram import types
from app.services.user_service import UserService
from app.keyboards.inline_buttons import get_start_keyboard

user_service = UserService()


async def start_handler(message: types.Message):
    text = (
        "Добро пожаловать!\n"
        "Сформулируй свой вопрос и жми на кнопку!"
    )
    await message.answer(text, reply_markup=get_start_keyboard())
