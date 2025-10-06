from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes


class buttons:

    def __init__(self):
        pass

    def news_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        query = update.callback_query
