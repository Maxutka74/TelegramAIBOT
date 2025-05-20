from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

random_facts_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Випадковий факт", callback_data="random_fact")],
        [InlineKeyboardButton(text="Закінчити", callback_data="exit_fact")]
    ]
)
