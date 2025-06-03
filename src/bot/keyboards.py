from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

random_facts_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Випадковий факт", callback_data="random_fact")]
    ]
)

famous_person = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Курт Кобейн", callback_data="persona_kobeyn")],
        [InlineKeyboardButton(text="Єлизавета 2", callback_data="persona_queen")],
        [InlineKeyboardButton(text="Джон Толкін", callback_data="persona_tolkin")],
        [InlineKeyboardButton(text="Фрідріх Ніцше", callback_data="persona_nicce")],
        [InlineKeyboardButton(text="Стівен Гокінг", callback_data="persona_goking")]
    ]
)

quiz = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="quiz_prog(Питання по Python)", callback_data="quiz_programist")],
        [InlineKeyboardButton(text="quiz_math(Питання по Математиці)", callback_data="quiz_math")],
        [InlineKeyboardButton(text="quiz_biology(Питання по Біології)", callback_data="quiz_biology")],
        [InlineKeyboardButton(text="quiz_more(Питання по попередній Темі)", callback_data="quiz_more")],
    ]
)

translate = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Англійська", callback_data="translate_english")],
        [InlineKeyboardButton(text="Іспінська", callback_data="translate_spanish")]
    ]
)

change_language = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Змінити мову", callback_data="change_theme")]
    ]
)

close_dialog = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Закінчити діалог", callback_data="exit_dialog")]
    ]
)

combined_keyboards = InlineKeyboardMarkup(inline_keyboard=change_language.inline_keyboard+close_dialog.inline_keyboard)
