from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from src.bot.states import ChatStates
from services.gpt.ChatGPT import OpenAIClient
from src.db.enums import SessionMode
from src.db.repository import GptSessionRepository
from src.bot.keyboards import close_dialog
from settings.logging_config import get_logger

gpt_router = Router(name=__name__)
logger = get_logger(__name__)

@gpt_router.message(ChatStates.gpt)
async def gpt_reply(
    message: Message,
    state: FSMContext,
    openai_client: OpenAIClient,
    session_repository: GptSessionRepository
):
    user_id = message.from_user.id
    session_id = await session_repository.get_or_create_session(user_id, SessionMode.GPT)

    user_text = message.text.strip()
    await session_repository.add_message(session_id, role="user", content=user_text)

    system_prompt_text = (
        "Ти - експерт з надання коротких та точних відповідей. "
        "Дай лаконічну, але інформативну відповідь на запитання. "
        "Використовуй не більше 1-2 речень. Уникай зайвих деталей та відступів."
    )
    full_prompt = system_prompt_text + "\n\n" + user_text
    try:
        reply = await openai_client.take_task(user_message=full_prompt)
        await session_repository.add_message(session_id, role="system", content=reply)

        await message.answer(reply, reply_markup=close_dialog)
    except Exception as e:
        logger.error(f"gpt_answer {e}")
        raise
