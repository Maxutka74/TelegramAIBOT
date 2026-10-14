# Telegram ChatGPT Bot

A multifunctional Telegram bot powered by Google's Gemini AI API that provides AI-powered conversations, quiz generation, text translation, image analysis, and more.

Built with Python and the asynchronous `aiogram` framework, the bot offers a variety of AI-powered features through an intuitive Telegram interface.

## Features

- **AI Chat** — Ask questions and get AI-generated responses.
- **Random Facts** — Discover interesting facts on various topics.
- **AI Quizzes** — Generate quizzes on topics of your choice.
- **Text Translation** — Translate messages between languages.
- **Image Analysis** — Send images to the bot and receive AI-generated descriptions and analysis.
- **Famous Personality Conversations** — Chat with an AI simulating a famous personality.
- **Session Storage** — Store conversation session data locally using SQLite.
- **Asynchronous Processing** — Handle Telegram updates efficiently with `aiogram`.

## Available Commands

| Command | Description |
|---|---|
| `/start` | Start the bot and display the welcome message. |
| `/random` | Get a random interesting fact. |
| `/gpt` | Ask the AI assistant a question. |
| `/talk` | Start a conversation with a famous personality. |
| `/quiz` | Generate a quiz on a topic of your choice. |
| `/translate` | Translate a message into another language. |
| `/image` | Enter image analysis mode and submit a photo. |


## Tech Stack

- **Python 3.12+** — Main programming language.
- **aiogram** — Asynchronous framework for the Telegram Bot API.
- **Google Gemini API** — AI-powered text generation and image analysis.
- **SQLite** — Local database for storing session data.
- **Pydantic Settings** — Environment-based application configuration.
- **python-dotenv / `.env`** — Environment variable management.
- **Pillow** — Image processing support.
- **Git** — Version control.

## Project Structure

```text
Telegram_ChatGPT/
├── resources/
│   ├── images/                 # Images used by the bot
├── services/
│   ├── function_gpt/           # AI features and bot functionality
│   │   ├── image.py            # Image analysis
│   │   ├── quiz.py              # Quiz generation
│   │   ├── quiz_question.py     # Quiz question handling
│   │   ├── random_facts.py      # Random facts
│   │   ├── talk_famous_person.py # Famous personality conversations
│   │   └── translate.py         # Text translation
│   └── gpt/
│       └── ChatGPT.py           # AI API client
├── settings/
│   ├── config.py                # Application settings
│   └── logging_config.py        # Logging configuration
├── src/
│   ├── bot/
│   │   ├── bot.py               # Application entry point
│   │   └── ...                  # Handlers, states, and keyboards
│   └── db/                      # Database operations
├── storage/                     # Local SQLite database
├── .env.example                 # Environment variable template
├── .gitignore
├── requirements.txt
└── README.md
```

> The structure above represents the main components of the project. Exact filenames and directory names may vary depending on the current repository version.

## Requirements

Before running the bot, make sure you have:

- Python 3.12 or newer.
- A Telegram bot token.
- A Google Gemini API key.
- Git.
- An active internet connection.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Maxutka74/TelegramAIBOT.git
cd TelegramAIBOT
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
```

Activate it on Linux or macOS:

```bash
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install Dependencies

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory.

You can use `.env.example` as a template if it is available:

```bash
cp .env.example .env
```

Add your credentials and model configuration:

```dotenv
# Google Gemini API key
GEMINI_API_KEY=your-gemini-api-key

# Telegram Bot API token
TELEGRAM_BOT_API_KEY=your-telegram-bot-token

# Gemini model
OPEANAI_MODEL=gemini-3.5-flash-lite

# Response generation temperature
OPEANAI_MODEL_TEMPERATURE=1.5
```

#### Where to Get the API Keys

- **Gemini API key:** https://aistudio.google.com/apikey
- **Telegram bot token:** Create a bot using [@BotFather](https://t.me/BotFather).

Replace the placeholder values with your actual credentials.

**Important:** Never commit your `.env` file or expose your API keys in a public repository.

> Make sure the environment variable names and model identifier match the configuration supported by your current project version and your Gemini API account.

### 5. Run the Bot

From the project root, execute:

```bash
python src/bot/bot.py
```

If the configuration is correct, the bot should connect to Telegram and start processing updates.

## Usage Examples

Open your bot in Telegram and try the following commands.

### Ask the AI Assistant

```text
/gpt Why is the sky blue?
```

The bot generates an AI-powered answer.

### Generate a Quiz

```text
/quiz Python
```

Generate quiz questions about Python.

### Translate Text

```text
/translate Hello, how are you?
```

Use the translation feature according to the instructions provided by the bot.

### Discover Random Facts

```text
/random
```

Receive an interesting fact.

### Chat with a Famous Personality

```text
/talk
```

Follow the bot's instructions to select or start a conversation with a famous personality.

### Analyze an Image

1. Enter image analysis mode using `/image`.
2. Send a photo to the bot.
3. Receive an AI-generated description or analysis of the image.

Image analysis requires a model that supports image input.

## Configuration

The application uses environment variables to separate configuration and credentials from the source code.

| Variable | Description |
|---|---|
| `GEMINI_API_KEY` | API key used to access Google Gemini. |
| `TELEGRAM_BOT_API_KEY` | Token used to authenticate the Telegram bot. |
| `OPEANAI_MODEL` | Name of the Gemini model used for AI requests. |
| `OPEANAI_MODEL_TEMPERATURE` | Controls the variability of generated responses. |

The current configuration uses the `OPEANAI_` prefix for historical compatibility. Consider renaming these variables to `GEMINI_MODEL` and `GEMINI_MODEL_TEMPERATURE` in a future refactoring.

## Database

The project uses SQLite for local session storage.

The database is stored locally, so no separate database server is required for basic development.

Make sure the application has permission to create and write to the configured storage directory.

## Logging

Application logs are used to record runtime events and help diagnose errors.

Logs are stored in the project's logging directory, depending on the logging configuration.

Do not include API keys, bot tokens, or other sensitive information in log messages.

## Troubleshooting

### Invalid Gemini API Key

If the API returns an authentication error:

- Check that `GEMINI_API_KEY` is set correctly.
- Verify that the key is active.
- Make sure the application loads the correct `.env` file.

### Model Not Found

If the selected model is unavailable:

- Check the model identifier in your `.env` file.
- Verify that the model is available to your API account.
- Update the configuration to use a currently supported model.

### Telegram Bot Does Not Respond

- Verify your Telegram bot token.
- Check that the application is running.
- Review the application logs for errors.
- Make sure the bot handlers and routers are registered correctly.

### Image Analysis Does Not Work

- Make sure the bot receives the uploaded photo.
- Verify that the image bytes are passed to the AI client.
- Ensure the selected model supports image input.
- Check the API response for model or request errors.

## Security

Follow these practices when running or modifying the project:

- Store credentials in environment variables.
- Keep `.env` out of version control.
- Use `.env.example` to document the required configuration.
- Never publish Telegram bot tokens or API keys.
- Avoid committing local databases containing private conversations.
- Handle API errors without exposing sensitive information.

## Future Improvements

Possible improvements include:

- Adding automated tests for bot handlers and AI integrations.
- Improving error handling and API retry logic.
- Adding support for additional AI models.
- Improving conversation history management.
- Adding Docker support for easier deployment.
- Implementing continuous integration and automated code checks.
- Improving image analysis and user interaction flows.

## Contributing

Contributions, bug reports, and feature suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test your implementation.
5. Submit a pull request describing your changes.

Please avoid including credentials or personal data in commits and issue reports.

## License

This project is distributed under the MIT License.

See the `LICENSE` file for the full license text.

## Author

**Maxutka74**

GitHub: [@Maxutka74](https://github.com/Maxutka74)

---

Built with Python, aiogram, and Google Gemini.