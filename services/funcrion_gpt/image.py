from aiogram import Router, F
from aiogram.types import Message
from services.gpt.ChatGPT import OpenAIClient
from settings.config import config
from src.bot.states import ChatStates
from io import BytesIO
from PIL import Image
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
    image_bytes.seek(0)

    photo = Image.open(image_bytes)

    client = OpenAIClient(
         openai_api_key=config.openai_api_token,
         model=config.opeanai_model,
         temperature=config.opeanai_model_temperature
     )
    try:
         response = await client.take_task(f"Проаналізуй фото і скажи що зоображено {photo}")
         await message.answer(response, reply_markup=close_dialog)
    except Exception as e:
        logger.error(f"Image {e}")
        raise
