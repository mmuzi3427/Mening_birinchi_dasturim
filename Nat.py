import sqlite3
conn = sqlite3.connect("ta.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS hisob (id TEXT, nat TEXT, wiki TEXT, n TEXT)""")
conn.commit()
conn.close()
def adduser(id):
    conn = sqlite3.connect("ta.db")
    c = conn.cursor()
    hisob = c.execute("""SELECT * FROM hisob""").fetchall()
    conn.commit()
    conn.close()
    for i in hisob:
        if i[0] == str(id):
            break
        else:
            conn = sqlite3.connect("ta.db")
            c = conn.cursor()
            c.execute(f"""INSERT INTO hisob VALUES ('{id}', 'Javoblar varaqasi:\n\n', "", "0")""")
            conn.commit()
            conn.close()

def nat(id, matn):
    conn = sqlite3.connect("ta.db")
    c = conn.cursor()
    hisobla = c.execute("""SELECT *FROM hisob""").fetchall()
    conn.commit()
    conn.close()
    for i in hisobla:
        if i[0] == str(id):
            data = str(f"{i[1]}{matn}")
            conn = sqlite3.connect("ta.db")
            c = conn.cursor()
            c.execute(f"""UPDATE hisob SET nat = '{data}' WHERE id = '{id}'""")
            conn.commit()
            conn.close()

def natol(id):
    conn = sqlite3.connect("ta.db")
    c = conn.cursor()
    hisobla = c.execute("""SELECT *FROM hisob""").fetchall()
    conn.commit()
    conn.close()
    for i in hisobla:
        if i[0] == str(id):
            return i[1]
def delete(id):
    conn = sqlite3.connect("ta.db")
    c = conn.cursor()
    hisobla = c.execute("""SELECT *FROM hisob""").fetchall()
    conn.commit()
    conn.close()
    for i in hisobla:
        if i[0] == str(id):
            conn = sqlite3.connect("ta.db")
            c = conn.cursor()
            c.execute(f"""UPDATE hisob SET nat = 'Javoblar varaqasi:\n\n', n = "0"  WHERE id = '{id}'""")
            conn.commit()
            conn.close()
def true(id):
    conn = sqlite3.connect("ta.db")
    c = conn.cursor()
    hisobla = c.execute("SELECT *FROM hisob").fetchall()
    conn.commit()
    conn.close()
    for i in hisobla:
        if i[0] == str(id):
            d = eval(f"{int(i[3])} + 1")
            conn = sqlite3.connect("ta.db")
            c = conn.cursor()
            c.execute(f"""UPDATE hisob SET n = '{d}' WHERE id = '{id}'""")
            conn.commit()
            conn.close()
def h(id):
    conn = sqlite3.connect("ta.db")
    c = conn.cursor()
    hisobla = c.execute("SELECT *FROM hisob").fetchall()
    conn.commit()
    conn.close()
    for i in hisobla:
        if i[0] == str(id):
            return i[3]
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
def qayt():
    m = ReplyKeyboardMarkup(resize_keyboard=True)
    m.add(KeyboardButton("Chiqish ↩️ va tugatish ✔️"))
    return m
def yangi():
    n = ReplyKeyboardMarkup(resize_keyboard=True)
    n.add(KeyboardButton(" Asosiy sahifa ♻️"))
    return n
