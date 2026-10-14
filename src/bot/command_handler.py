from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from aiogram import Router
from aiogram.fsm.context import FSMContext
from src.bot.keyboards import random_facts_keyboard, famous_person, quiz, translate
from settings.config import config
from src.bot.states import ChatStates

command_router = Router(name=__name__)

photo1 = FSInputFile(config.path_to_images / 'gpt.jpg')
photo2 = FSInputFile(config.path_to_images / 'main.jpg')
photo3 = FSInputFile(config.path_to_images / 'talk.jpg')
photo4 = FSInputFile(config.path_to_images / 'quiz.jpg')

@command_router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привіт! {message.from_user.full_name}. Я Telegram_ChatGPT бот\n\n"
                         f"Список доступних команд:\n"
                         f"/random - Випадковий факт\n"
                         f"/gpt - Ваш запит до штучного інтелекту\n"
                         f"/talk - Діалог з відомою особистістю\n"
                         f"/quiz - Квіз на тему яку ви хочете\n"
                         f"/translate - Перекладіть повідомлення\n"
                         f"/image - Аналіз фото"
                         )


@command_router.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    await message.answer(f"Список доступних команд:\n"
                         f"/random - Випадковий факт\n"
                         f"/gpt - Ваш запит до штучного інтелекту\n"
                         f"/talk - Діалог з відомою особистістю\n"
                         f"/quiz - Квіз на тему яку ви хочете\n"
                         f"/translate - Перекладіть повідомлення\n"
                         f"/image - Аналіз фото")

@command_router.message(Command("random"))
async def command_ramdomfacts_handler(message: Message, state:FSMContext) -> None:
    await message.answer_photo(photo=photo1)
    await message.answer("Пригадую цікавий факт...",
                         reply_markup=random_facts_keyboard)
    await state.set_state(ChatStates.chatting)

@command_router.message(Command("gpt"))
async def command_gpt_handler(message: Message, state: FSMContext) -> None:
    await message.answer_photo(photo=photo2)
    await message.answer("Задай запитання ChatGPT:")
    await state.set_state(ChatStates.gpt)

@command_router.message(Command("talk"))
async def command_talk_handler(message: Message, state: FSMContext) -> None:
    await message.answer_photo(photo=photo3)
    await message.answer("""Оберіть відому особистість, з якою хочете поговорити:
Список доступних особистостей:
1. Курт Кобейн - Соліст гурту Nirvana 🎸
2. Єлизавета II - Королева Об'єднаного Королівства 👑
3. Джон Толкін - Автор книги "Володар Перснів" 📖
4. Фрідріх Ніцше - Філософ 🧠
5. Стівен Гокінг - Фізик 🔬""",
                         reply_markup=famous_person)
    await state.set_state(ChatStates.chatting)

@command_router.message(Command("quiz"))
async def command_quiz_handler(message: Message, state: FSMContext) -> None:
    await message.answer_photo(photo=photo4)
    await message.answer("""Перевір свою ерудицію разом з ChatGPT!
Обери тему, на яку будеш грати:""", reply_markup=quiz)
    await state.set_state(ChatStates.quiz)

@command_router.message(Command("translate"))
async def command_translate_handle(message: Message) -> None:
    await message.answer("Виберіть мову на яку хочите перекласти текст!", reply_markup=translate)


@command_router.message(Command("image"))
async def command_image_handler(message:Message, state:FSMContext) -> None:
    await message.answer(f"Надішліть фото-повідомлення для аналізу!")
    await state.set_state(ChatStates.image)

