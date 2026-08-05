from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/add"), KeyboardButton(text="/plan")],
        [KeyboardButton(text="/statistik")],
    ],
    resize_keyboard=True
)
