from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from services.gpt.ChatGPT import OpenAIClient
from settings.config import config
from src.bot.states import ChatStates
from src.bot.keyboards import combined_keyboards
from settings.logging_config import get_logger

translate_router = Router(name=__name__)
logger = get_logger(__name__)

@translate_router.message(ChatStates.translate)
async def translate(message: Message,state:FSMContext):
    current = ChatStates.translate
    if current != ChatStates.translate:
        return

    data = await state.get_data()
    text_translate = data.get("translate")

    promt = {
        "english": f"Ти повинен введений текст перекласти на Анлійську мову {message.text}",
        "spanish": f"Ти повинен введений текст перекласти на Іспанську мову {message.text}"
    }

    translate_text_user = promt.get(text_translate)

    client = OpenAIClient(
        openai_api_key=config.openai_api_token,
        model=config.opeanai_model,
        temperature=config.opeanai_model_temperature
    )

    try:
        response = await client.take_task(translate_text_user)
        await message.answer(response, reply_markup=combined_keyboards)

    except Exception as e:
        logger.error(f"Translate {e}")
        raise
