import os
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI, OpenAIError
from Chatgpt.random_facts import generate_category

load_dotenv()
CHATAI_TOKEN = os.getenv("CHATAI_TOKEN")

class OpenAIClient:
    def __init__(self):
        self._client = AsyncOpenAI(api_key=CHATAI_TOKEN)

    async def take_task(self, user_message: str, system_promt: str = 'Ти — помічник, що завжди відповідає українською мовою.') -> str | None:
        try:
            response = await self._client.chat.completions.create(
                model='gpt-3.5-turbo'
                , messages=[
                    {'role': 'system', 'content': system_promt},
                    {'role': 'user', 'content': user_message}
                ]
            )

            return response.choices[0].message.content
        except OpenAIError as e:
            print(f'Error in: {self.take_task.__name__}. Error is: {e}')


async def main():
    client = OpenAIClient()
    random_fact = await client.take_task(f'Розкажи цікавий факт про {generate_category()}')
    return random_fact


if __name__ == '__main__':
    asyncio.run(main())