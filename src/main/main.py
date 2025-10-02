import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

load_dotenv()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


if __name__ == "__main__":
    # Get token from environment variable
    token = os.getenv("telegram_bot")
    if not token:
        raise RuntimeError("Environment variable 'telegram_bot' not found. Add it to your .env file.")

    application = (
        ApplicationBuilder()
        .token(token)
        .build()
    )

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    application.run_polling()
