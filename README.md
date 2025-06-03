Telegram_ChatGPT

Telegram_ChatGPT — це багатофункціональний Telegram-бот, що використовує OpenAI GPT для взаємодії з користувачем. Побудований на Python із використанням фреймворку aiogram, бот вміє відповідати на запити, генерувати вікторини, перекладати тексти, аналізувати зображення, вести розмови з відомими особистостями та видавати випадкові факти.

Список доступних команд:
/random – Випадковий факт
/gpt – Ваш запит до штучного інтелекту
/talk – Діалог з відомою особистістю
/quiz – Квіз на тему, яку ви хочете
/translate – Перекладіть повідомлення
/image – Аналіз фото

Технології:

Python 3.12+

aiogram — асинхронний фреймворк для Telegram Bot API

OpenAI API (GPT)

SQLite (для збереження сесій)

.env конфігурація

Структура проєкту:
TelegramAIBOT/
├── logs/ - Логи застосунку
├── myenv/ - Віртуальне середовище
├── resourсes/images/ - Зображення для бота
├── services/
│ ├── funcion_gpt/ - Основні функції: GPT, вікторини, переклад
│ └── gpt/ - Робота з OpenAI
├── settings/ - Конфігурації та логування
├── src/
│ ├── bot/ - Основна логіка Telegram бота
│ └── db/ - Робота з базою даних
├── storage/ - Локальна SQLite база
├── .env - Файл змінних середовища (секрети)
├── requirements.txt - Залежності
├── README.md - Документація
├── .gitignore - Ігноровані файли

Інструкція зі встановлення:

Клонувати репозиторій:
git clone https://github.com/your_username/Telegram_ChatGPT.git
cd Telegram_ChatGPT

Створити та активувати віртуальне середовище (опціонально):
python -m venv myenv
source myenv/bin/activate (або myenv\Scripts\activate на Windows)

Встановити залежності:
pip install -r requirements.txt

Створити файл .env у корені проєкту зі вмістом:
OPENAI_API_KEY=your_openai_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token

Запуск бота:
python src/bot/bot.py

Приклади використання:
/gpt Чому небо синє?
/quiz Python
/translate Hello world
/image (відправити фото для аналізу)

Ліцензія: MIT License — дозволено вільне використання, зміну та розповсюдження.

Розробник: (Maxutka74)

