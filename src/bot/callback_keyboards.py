from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from services.funcrion_gpt.random_facts import main
from src.bot.states import ChatStates
from src.bot.keyboards import close_dialog
from services.funcrion_gpt.quiz_question import quiz_questions
from services.funcrion_gpt import quiz
from src.bot.keyboards import translate

output_router = Router()

@output_router.callback_query(F.data == "exit_dialog")
async def exit_chat(callback: CallbackQuery, state: FSMContext):
    quiz.true_answer = 0
    await state.clear()
    await callback.message.answer(f"Привіт! {callback.from_user.full_name}. Я Telegram_ChatGPT бот\n\n"
                         f"Список доступних команд:\n"
                         f"/random - Випадковий факт\n"
                         f"/gpt - Ваш запит до штучного інтелекту\n"
                         f"/talk - Діалог з відомою особистістю\n"
                         f"/quiz - Квіз на тему яку ви хочете\n"
                         f"/translate - Перекладіть повідомлення\n"
                         f"/image - Аналіз фото"
                         )
    await callback.answer()

@output_router.callback_query(F.data == "random_fact")
async def handle_random_fact(callback: CallbackQuery):
    await callback.message.answer("Ось випадковий факт!")
    fact = await main()
    if fact:
        await callback.message.answer(fact, reply_markup=close_dialog)
    else:
        await callback.message.answer("Вибач, не зміг отримати факт.")
    await callback.answer()

@output_router.callback_query(F.data.startswith("persona_"))
async def select_persona(callback: CallbackQuery, state: FSMContext):
    persona = callback.data.replace("persona_", "")
    await state.set_data({"persona": persona})
    await state.set_state(ChatStates.chatting)
    await callback.message.answer(f"Тепер ти спілкуєшся з {persona.title()}! Напиши щось:")
    await callback.answer()

@output_router.callback_query(F.data.startswith("quiz_"))
async def select_quiz_quetion(callback: CallbackQuery, state: FSMContext):
    quiz = callback.data.replace("quiz_", "")
    await state.set_data({"quiz": quiz})
    await state.set_state(ChatStates.quiz)
    await callback.message.answer(f"Зараз будуть питання по темі {quiz.title()}! Приготуйся!")
    quiz_question = await quiz_questions(state)
    await callback.message.answer(quiz_question)
    await callback.answer()

@output_router.callback_query(F.data.startswith("translate_"))
async def select_translate(callback:CallbackQuery, state: FSMContext):
    translate = callback.data.replace("translate_", "")
    await state.update_data({"translate": translate})
    await state.set_state(ChatStates.translate)
    await callback.message.answer("Введіть текст для перекладу:")
    await callback.answer()

@output_router.callback_query(F.data == "change_theme")
async def chamge_theme(callback:CallbackQuery):
    await callback.message.answer("Виберіть нову мову для перекладу теусту!", reply_markup=translate)






