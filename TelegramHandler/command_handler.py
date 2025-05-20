from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
from TelegramHandler.keyboards import random_facts_keyboard

command_router = Router(name=__name__)

@command_router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привіт! {message.from_user.full_name}. Я Telegram_ChatGPT бот")


@command_router.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    await message.answer(f"Список доступних команд:\n"
                         f"/random - Випадковий факт\n"
                         f"/gpt - Ваш запит до штучного інтелекту\n"
                         f"/talk - Діалог з відомою особистістю\n"
                         f"/quiz - Квіз на тему яку ви хочете")

@command_router.message(Command("random"))
async def command_ramdomfacts_handler(message: Message) -> None:
    await message.answer("Виберіть, що ви хочете отримати",
                         reply_markup=random_facts_keyboard)