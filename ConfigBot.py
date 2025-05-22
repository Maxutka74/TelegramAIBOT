import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from TelegramHandler.command_handler import command_router
from TelegramHandler.callback_keyboards import output_router
from Chatgpt.gpt_answer import input_router

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

dp = Dispatcher()


dp.include_router(command_router)
dp.include_router(output_router)
dp.include_router(input_router)

async def main() -> None:
    bot = Bot(token=TELEGRAM_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
