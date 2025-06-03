from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from services.gpt.ChatGPT import OpenAIClient
from settings.config import config
from src.bot.keyboards import close_dialog
from src.bot.states import ChatStates
from settings.logging_config import get_logger

quiz_router = Router(name=__name__)
logger = get_logger(__name__)

true_answer = 0

@quiz_router.message(ChatStates.quiz)
async def quiz_handler(message: Message, state: FSMContext):
    global true_answer

    current_state = await state.get_state()
    if current_state != ChatStates.quiz.state:
        return

    data = await state.get_data()
    question = data.get("quiz_question")


    prompts = [f"""Ти — асистент, який перевіряє правильність відповіді користувача на запитання.  
                    Ось запитання: {question}  
                    Ось відповідь користувача: {message.text}
                    
                    Якщо відповідь правильна або дуже схожа на правильну — просто відповідай:  
                    Правильно!
                    
                    Якщо відповідь неправильна — відповідай у такому форматі:  
                    Неправильно!. Правильна відповідь: [тут правильна відповідь].  
                    Пояснення: [чому ця відповідь правильна].'
                    
                    Не додавай нічого більше. Не став нових запитань."""
    ]


    client = OpenAIClient(
        openai_api_key=config.openai_api_token,
        model=config.opeanai_model,
        temperature=config.opeanai_model_temperature
    )

    full_prompt = f"{prompts}"
    try:
        response = await client.take_task(full_prompt)
        await message.answer(response, reply_markup=close_dialog)

        if "Правильно!" in response:
            true_answer += 1

        await message.answer(f"Ваш поточний рахунок правильних відповідей: {true_answer}")

    except Exception as e:
        logger.error(f"Quiz {e}")
        raise

