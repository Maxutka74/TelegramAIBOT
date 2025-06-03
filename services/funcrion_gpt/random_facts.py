from random import randint
from services.gpt.ChatGPT import OpenAIClient
from settings.config import config

CATEGORY_FACTS = {
    1: 'Історія',
    2: 'Кіно',
    3: 'Ігри',
    4: 'Природа',
    5: 'Наука',
    6: 'Географія',
    7: 'Культура',
    8: 'Людське тіло',
    9: 'Космос',
    10: 'Технології'
}

def generate_category(start: int = 1, end: int = 5) -> str:
    return CATEGORY_FACTS.get(randint(start, end), 'History')

async def main():
    client = OpenAIClient(
        openai_api_key=config.openai_api_token,
        model=config.opeanai_model,
        temperature=config.opeanai_model_temperature
    )

    try:
        random_fact = await client.take_task(f'Розкажи цікавий факт про {generate_category()}')
        return random_fact
    except Exception as e:
        logger.error(f"random_facts {e}")
        raise
