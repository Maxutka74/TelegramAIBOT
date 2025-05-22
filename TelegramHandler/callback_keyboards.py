from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from Chatgpt.ChatGPT import main



output_router = Router()
photo = FSInputFile("OIP.jpg")

@output_router.callback_query(F.data == "random_fact")
async def handle_random_fact(callback: CallbackQuery):
    await callback.message.answer_photo(photo=photo)
    await callback.message.answer("Ось випадковий факт!")
    fact = await main()
    if fact:
        await callback.message.answer(fact)
    else:
        await callback.message.answer("Вибач, не зміг отримати факт.")
    await callback.answer()

@output_router.callback_query(F.data == "exit_fact")
async def handle_random_fact(callback: CallbackQuery):
    await callback.message.answer(f"Привіт! {callback.from_user.full_name}. Я Telegram_ChatGPT бот")
    await callback.answer()

