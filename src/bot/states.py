from aiogram.fsm.state import StatesGroup, State

class ChatStates(StatesGroup):
    chatting = State()
    gpt = State()
    quiz = State()
    translate = State()
    image = State()