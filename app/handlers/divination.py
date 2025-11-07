from aiogram import types
from aiogram.types import FSInputFile
from app.services.hexagram_service import HexagramService
from app.services.user_service import UserService
from app.keyboards.inline_buttons import (
    get_start_keyboard, get_divination_keyboard)
import asyncio

from config import ADMIN_ID, COIN_IMAGE

hexagram_service = HexagramService()
user_service = UserService()


async def coin_cast_handler(event):
    if isinstance(event, types.CallbackQuery):
        message = event.message
        user_id = event.from_user.id
        await event.answer()
    else:
        message = event
        user_id = event.from_user.id
    await message.answer(
        "Монетки подбрасываются в воздухе и падают на землю..."
        )
    coin_img = FSInputFile(COIN_IMAGE)
    await message.answer_photo(coin_img)
    await asyncio.sleep(2)
    await message.answer("✨ Повторяем 6 раз...")
    await asyncio.sleep(2)
    hexagram = hexagram_service.get_random_hexagram()
    number = hexagram['id']
    name = hexagram['name']
    description = hexagram['description']
    image_path = hexagram_service.get_image_path(hexagram['image'])
    photo = FSInputFile(image_path)
    await message.answer(
        f"Готово! 🔮 Судьба принесла вам гексаграмму №{number}. {name}."
    )
    await message.answer_photo(photo, parse_mode="HTML")
    text2 = f"<b>№{number}. {name}</b>\n\n{description}"
    await message.answer(text2, parse_mode="HTML",
                         reply_markup=get_divination_keyboard())
    user_service.increment_counter(
        user_id,
        username=event.from_user.username
    )


async def prepare_divination(call: types.CallbackQuery):
    text = ("Сформулируй свой вопрос и жми на кнопку!")
    await call.message.answer(text,
                              reply_markup=get_start_keyboard())


async def users_stats_handler(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        stats = user_service.get_users_stats()
        total_users = len(stats)
        if not stats:
            await message.answer("Пользовательских данных нет.")
            return

        text = f"Общее количество пользователей: {total_users}\n\n"
        text += "ID | username | Гаданий\n" + "-"*32 + "\n"
        for u in stats:
            text += f"{u['user_id']} | @{u['username']} | {u['count']}\n"
        await message.answer(text)
    else:
        await message.answer("Доступ запрещён")
