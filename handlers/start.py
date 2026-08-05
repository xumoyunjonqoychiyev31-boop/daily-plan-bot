from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from database.db import add_user
from keyboards.menu import main_menu

router = Router()


@router.message(CommandStart())
async def start(message: Message):

    await add_user(
        message.from_user.id,
        message.from_user.full_name,
        message.from_user.username or ""
    )

    text = f"""
👋 Assalomu alaykum <b>{message.from_user.full_name}</b>!

📅 Daily Plan Botga xush kelibsiz.

Quyidagi menyudan foydalanishingiz mumkin.
"""

    await message.answer(
        text,
        reply_markup=main_menu
    )
