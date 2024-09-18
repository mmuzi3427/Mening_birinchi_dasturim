from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
def btn():
    btn1 = InlineKeyboardMarkup()
    btn1.add(InlineKeyboardButton("❌", callback_data="delete1"))
    return btn1
