import logging
from typing import Dict, Optional

from telegram import (
    Update,
    ForceReply,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ParseMode,
)
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    CallbackQueryHandler,
)
from telegram.error import TelegramError


# Enable logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# set higher logging level for httpx to avoid all GET and POST requests being logged

logging.getLogger("httpx").setLevel(logging.WARNING)


class Bot:
    """Minimal Bot helpers for handlers."""

    def __init__(self, screaming: bool = False):
        self.screaming = screaming
        self.users_dict: Dict[int, Dict[str, Optional[str]]] = {}
        self.logger = logging.getLogger(__name__)

    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message when the command /start is issued."""

        user = update.effective_user

        await update.message.reply_html(
            rf"Hi {user.mention_html()}!",
            reply_markup=ForceReply(selective=True),
        )

    @staticmethod
    def on_update_received(update: Update):
        # Record the user whenever an update is received
        pass

    @staticmethod
    def echo(update: Update, context: CallbackContext) -> None:
        # Use the same logic as on_update_received to print incoming messages.
        Bot.on_update_received(update)
