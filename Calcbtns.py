from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
def calcb():
    calc1 = InlineKeyboardMarkup(row_width=4)
    calc1.add(InlineKeyboardButton("1️⃣", callback_data="1"), InlineKeyboardButton("2️⃣", callback_data="2"), InlineKeyboardButton("3️⃣", callback_data="3"), InlineKeyboardButton("➕", callback_data="+"), InlineKeyboardButton("4️⃣", callback_data="4"), InlineKeyboardButton("5️⃣", callback_data="5"), InlineKeyboardButton("6️⃣", callback_data="6"), InlineKeyboardButton("➖", callback_data="-"), InlineKeyboardButton("7️⃣", callback_data="7"), InlineKeyboardButton("8️⃣", callback_data="8"), InlineKeyboardButton("9️⃣", callback_data="9"), InlineKeyboardButton("✖️", callback_data="*"), InlineKeyboardButton("0️⃣", callback_data="0"), InlineKeyboardButton("C", callback_data="toza"), InlineKeyboardButton("=", callback_data="="), InlineKeyboardButton("➗", callback_data="/"))
    calc1.add(InlineKeyboardButton("....", callback_data="qoshimcha"),)
    return calc1
