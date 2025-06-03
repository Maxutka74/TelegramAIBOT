from aiogram.fsm.context import FSMContext
from services.gpt.ChatGPT import OpenAIClient
from settings.config import config
from src.bot.states import ChatStates
from settings.logging_config import get_logger

logger = get_logger(__name__)

async def quiz_questions(state:FSMContext):
    data = await state.get_data()
    quiz = data.get("quiz")

    promt = {
    'programist': 'Згенеруй одне невилике питання на тему програмування мовою python',
    'math': 'Згенеруй одне невилике питання на тему математичних теорій - теорії алгоритмів, теорії множин та матаналізу',
    'biology': 'Згенеруй одне невилике питання на тему біології',
    'more': 'Згенеруй одне невилике питання на ту ж тему, що й попереднє.'
    }

    base_prompt = promt.get(quiz)

    client = OpenAIClient(
        openai_api_key=config.openai_api_token,
        model=config.opeanai_model,
        temperature=config.opeanai_model_temperature
    )
    try:
        response = await client.take_task(base_prompt)
        await state.update_data({"quiz_question": response})
        await state.set_state(ChatStates.quiz)
        return response
    except Exception as e:
        logger.error(f"Quiz_question {e}")
        raise

