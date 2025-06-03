from aiogram import BaseMiddleware
from typing import Callable, Awaitable, Dict, Any
from aiogram.types import TelegramObject

class EnvironmentMiddleware(BaseMiddleware):
    def __init__(self, openai_client, session_repository):
        super().__init__()  # виклик конструктора базового класу
        self.openai_client = openai_client
        self.session_repository = session_repository

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        # додаємо потрібні об'єкти у data, щоб їх можна було далі дістати в хендлерах
        data["openai_client"] = self.openai_client
        data["session_repository"] = self.session_repository
        return await handler(event, data)
