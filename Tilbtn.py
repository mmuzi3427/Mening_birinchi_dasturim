from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
def ru():
    kirish = ReplyKeyboardMarkup(resize_keyboard=True)
    kirish.add(KeyboardButton("Калькулятор"), KeyboardButton("Случайное число"))
    return kirish
def rudel():
    b = InlineKeyboardMarkup()
    b.add(InlineKeyboardButton("✖️ Удалить", callback_data="delru"))
    return b
def tu():
    n = InlineKeyboardMarkup()
    n.add(InlineKeyboardButton("♻️ Я понимаю ️✅", callback_data="delru"))
    return n
