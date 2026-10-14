from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).parent.parent


class AppConfig(BaseSettings):
    gemini_api_key: str
    telegram_bot_api_key: str

    opeanai_model: str = 'gemini-2.5-flash-lite'
    opeanai_model_temperature: float = 1.5

    path_to_messages: Path = BASE_DIR / 'resoursec' / 'messages'
    path_to_images: Path = BASE_DIR / 'resoursec' / 'images'
    path_to_menus: Path = BASE_DIR / 'resoursec' / 'menus'
    path_to_prompts: Path = BASE_DIR / 'resoursec' / 'prompts'

    path_to_logs: Path = BASE_DIR / 'logs'

    path_to_db: Path = BASE_DIR / 'storage' / 'chat_sessions.db'

    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / '.env'),
        env_file_encoding='utf-8'
    )


config = AppConfig()