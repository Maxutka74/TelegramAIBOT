import base64
from openai import AsyncOpenAI, OpenAIError
from settings.logging_config import get_logger

logger = get_logger(__name__)


class OpenAIClient:
    def __init__(self, openai_api_key: str, model: str, temperature: float):
        self._client = AsyncOpenAI(
            api_key=openai_api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
        self._model = model
        self._temperature = temperature

    async def take_task(
        self,
        user_message: str,
        system_promt: str = (
                "Ти — помічник, що завжди відповідає українською мовою. "
                "Відповідай звичайним текстом без Markdown-форматування. "
                "Не використовуй ** для жирного тексту, * для курсиву, "
                "заголовки через # або Markdown-списки."
        ),
        image_bytes: bytes | None = None
    ) -> str | None:
        try:
            if image_bytes:
                encoded_image = base64.b64encode(image_bytes).decode("utf-8")

                content = [
                    {
                        "type": "text",
                        "text": user_message
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encoded_image}"
                        }
                    }
                ]
            else:
                content = user_message

            response = await self._client.chat.completions.create(
                model=self._model,
                messages=[
                    {'role': 'system', 'content': system_promt},
                    {'role': 'user', 'content': content}
                ],
                temperature=self._temperature
            )

            return response.choices[0].message.content

        except OpenAIError as e:
            logger.error(f'Gemini API Error: {e}')
            raise