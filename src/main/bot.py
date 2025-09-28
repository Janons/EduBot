import logging

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


class Bot:

    def on_update_recieved(update: Update):
        pass


class Users:
    pass
