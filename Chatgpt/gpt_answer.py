from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from TelegramHandler.states import ChatStates
from Chatgpt.ChatGPT import OpenAIClient

input_router = Router(name=__name__)

@input_router.message(ChatStates.chatting)
async def input_message(message: Message, state: FSMContext):
    if message.text == 'exit':
        await message.answer("Завершення діалогу)")
        await state.clear()
        return
    client = OpenAIClient()
    response = await client.take_task(f"Користувач запитав: {message.text}")
    await message.answer(response)
