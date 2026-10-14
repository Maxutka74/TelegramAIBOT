from io import BytesIO

from aiogram import Router, F
from aiogram.types import Message
from services.gpt.ChatGPT import OpenAIClient
from settings.config import config
from src.bot.states import ChatStates
from src.bot.keyboards import close_dialog
from settings.logging_config import get_logger

image_router = Router()
logger = get_logger(__name__)

@image_router.message(F.photo, ChatStates.image)
async def images(message: Message):
    image = message.photo[-1]
    file = await message.bot.get_file(image.file_id)

    image_bytes = BytesIO()
    await message.bot.download_file(file.file_path, destination=image_bytes)

    client = OpenAIClient(
         openai_api_key=config.gemini_api_key,
         model=config.opeanai_model,
         temperature=config.opeanai_model_temperature
     )
    try:
         response = await client.take_task(f"Проаналізуй фото і скажи що зоображено", image_bytes=image_bytes.getvalue())
         await message.answer(response, reply_markup=close_dialog)
    except Exception as e:
        logger.error(f"Image {e}")
        raise
