import asyncio

from services.gpt.ChatGPT import OpenAIClient
from settings.config import config
from aiogram import Bot, Dispatcher
from src.bot.command_handler import command_router
from src.bot.callback_keyboards import output_router
from services.funcrion_gpt.gpt_answer import gpt_router
from services.funcrion_gpt.talk_famous_person import talk_router
from services.funcrion_gpt.quiz import quiz_router
from services.funcrion_gpt.translate import translate_router
from services.funcrion_gpt.image import image_router
from src.bot.enviroment import EnvironmentMiddleware
from src.db.initializator import DatabaseInitializer
from src.db.repository import GptSessionRepository



async def main() -> None:
    bot = Bot(token=config.telegram_bot_api_key)
    dp = Dispatcher()

    dp.include_router(command_router)
    dp.include_router(output_router)
    dp.include_router(gpt_router)
    dp.include_router(talk_router)
    dp.include_router(quiz_router)
    dp.include_router(translate_router)
    dp.include_router(image_router)

    db_initializator = DatabaseInitializer(config.path_to_db)
    db_initializator.create_tables()

    session_repository = GptSessionRepository(config.path_to_db)
    openai_client = OpenAIClient(
        openai_api_key=config.gemini_api_key,
        model=config.opeanai_model,
        temperature=config.opeanai_model_temperature
    )

    gpt_router.message.middleware(EnvironmentMiddleware(openai_client, session_repository))

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
