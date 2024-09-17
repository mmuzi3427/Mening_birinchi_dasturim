from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import random
import Text
import Calcbtn
import Video
import funcs
import test
import Nat
import lugat
import Tilbtn
import kvuz
import edit
import admin
import wikipedia
wikipedia.set_lang("uz")
#https://t.me/MATHtestchannel
channel = "@MATHtestchannel"
admin_id = "-1002099634180"
master_id = 7151642135
son1 = 0
son2 = 0
amal = ""
ildiz = 0
text = ""
bot = TeleBot("Token")
@bot.message_handler(commands=['admin'])
def admin1(m):
    if m.from_user.id == master_id:
        admin.adduser(m.from_user.id)
        bot.send_message(m.chat.id, "Kimga xabar yubormoqchisiz? ID:")
        bot.register_next_step_handler(m, id)

def id(m):
    admin.getid(m.from_user.id, m.text)
    bot.send_message(m.chat.id, "Yuboriladigan xabarni kiriting!")
    bot.register_next_step_handler(m, getme)
def getme(m):
    admin.getext(m.from_user.id, m.text)
    try:
        bot.send_message(int(admin.id(m.from_user.id)), str(admin.text(m.from_user.id)))
        bot.send_message(m.chat.id, "Xabarni yubordim ✅")
        bot.send_message(m.chat.id, "⚽")
    except:
        bot.send_message(m.chat.id, "Xabar yuborilmadi?")
def mdel():
    return ReplyKeyboardRemove()
def delete():
    deleteInline = InlineKeyboardMarkup()
    deleteInline.add(InlineKeyboardButton("✖️  Oʻchirirish" , callback_data="delete1"))
    return deleteInline
def tushundim():
    tush = InlineKeyboardMarkup()
    tush.add(InlineKeyboardButton("♻️ Tushundim ✅", callback_data="delete1"))
    return tush
def test10():
    test10_1 = InlineKeyboardMarkup(row_width=1)
    test10_1.add(InlineKeyboardButton("A) 502", callback_data="A10"), InlineKeyboardButton("B) 511", callback_data="B10"), InlineKeyboardButton("C) 521", callback_data="C10"))
    return test10_1
def test9():
    test9_1 = InlineKeyboardMarkup(row_width=1)
    test9_1.add(InlineKeyboardButton("A) 1766", callback_data="A9"), InlineKeyboardButton("B) 1966", callback_data="B9"), InlineKeyboardButton("C) 2266", callback_data="C9"))
    return test9_1
def test8():
    test8_1 = InlineKeyboardMarkup(row_width=1)
    test8_1.add(InlineKeyboardButton("A) 390", callback_data="A8"), InlineKeyboardButton("B) 400", callback_data="B8"), InlineKeyboardButton("C) 420", callback_data="C8"))
    return test8_1
def test7():
    test7_1 = InlineKeyboardMarkup(row_width=1)
    test7_1.add(InlineKeyboardButton("A) --211", callback_data="A7"), InlineKeyboardButton("B) --221", callback_data="B7"), InlineKeyboardButton("C) --231", callback_data="C7"))
    return test7_1
def test6():
    test6_1 = InlineKeyboardMarkup(row_width=1)
    test6_1.add(InlineKeyboardButton("A) 337", callback_data="A6"), InlineKeyboardButton("B) 347", callback_data="B6"), InlineKeyboardButton("C) 357", callback_data="C6"))
    return test6_1
def test5():
    test5_1 = InlineKeyboardMarkup(row_width=1)
    test5_1.add(InlineKeyboardButton("A) 9", callback_data="A5"), InlineKeyboardButton("B) 11", callback_data="B5"), InlineKeyboardButton("C) 12", callback_data="C5"))
    return test5_1
def test4():
    test4_1 = InlineKeyboardMarkup(row_width=1)
    test4_1.add(InlineKeyboardButton("A) 48,5", callback_data="A4"), InlineKeyboardButton("B) 49,5", callback_data="B4"), InlineKeyboardButton("C) 50,5", callback_data="C4"))
    return test4_1
def test3():
    test14 = InlineKeyboardMarkup(row_width=1)
    test14.add(InlineKeyboardButton("A) 62,5", callback_data="A3"), InlineKeyboardButton("B) 63,5", callback_data="B3"), InlineKeyboardButton("C) 64,5", callback_data="C3"))
    return test14
def test2():
    test11 = InlineKeyboardMarkup(row_width=1)
    test11.add(InlineKeyboardButton("A) 203", callback_data="A2"), InlineKeyboardButton("B) 213", callback_data="B2"), InlineKeyboardButton("C) 233", callback_data="C2"))
    return test11
def test1():
    test13 = InlineKeyboardMarkup(row_width=1)
    test13.add(InlineKeyboardButton("A) 1567", callback_data="A1"), InlineKeyboardButton("B) 1667", callback_data="B1"), InlineKeyboardButton("C) 1777", callback_data="C1"))
    return test13
def test12():
    btnm = InlineKeyboardMarkup()
    btnm.add(InlineKeyboardButton("Testni boshlash", callback_data="text"))
    return btnm
def true():
    ta = ReplyKeyboardMarkup()
    ta.add(KeyboardButton("Ma'umotlar toʻgʻri 100%"), KeyboardButton("📊 Testda qatnashish"))
    return ta
def error():
    e = InlineKeyboardMarkup()
    e.add(InlineKeyboardButton("-Orqaga" , callback_data="back"))
    return e
def obuna():
    m = InlineKeyboardMarkup(row_width=1)
    n1 = InlineKeyboardButton("Obuna boʻlish ✅", url="https://t.me/MATHtestchannel")
    n2 = InlineKeyboardButton("Obuna boʻldim ✅", callback_data='obuna')
    m.add(n1, n2)
    return m
def k1():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('Kalkulyator'), KeyboardButton("Ildiz"))
    markup.add(KeyboardButton("Kvadrat²"), KeyboardButton("Kub³"))
    markup.add(KeyboardButton("Tasodifiy raqam"), KeyboardButton("⚙ Sozlamalar"))
    markup.add(KeyboardButton("📊 Testda qatnashish"))
    markup.add(KeyboardButton("📼 Video darslar"))
    return markup
def k2():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('Kalkulyator'), KeyboardButton("Ildiz"))
    markup.add(KeyboardButton("Kvadrat²"), KeyboardButton("Kub³"))
    markup.add(KeyboardButton("Tasodifiy raqam"))
    markup.add(KeyboardButton("📊 Testda qatnashish"))
    markup.add(KeyboardButton("📼 Video darslar"))
    return markup
@bot.message_handler(commands=['edit'])
def editism(m):
    bot.send_message(m.chat.id, "Qaysi ma'lumotni oʻzgartirmoqchisiz?", reply_markup=edit.test1())
@bot.message_handler(content_types=['video'])
def video(m):
    bot.send_message(m.chat.id, m.video.file_id)
@bot.message_handler(content_types=['photo'])
def photo(m):
    bot.delete_message(m.chat.id, m.message_id)
    bot.send_message(m.chat.id, m.photo[0].file_id)
@bot.message_handler(commands=['search', 'wiki', 'поиск'])
def search(m):
    if m.from_user.language_code == "uz":
        bot.delete_message(m.chat.id, m.message_id)
        bot.send_message(m.chat.id, "🔎", reply_markup=kvuz.kv1())
    elif m.from_user.language_code == "ru":
        bot.delete_message(m.chat.id, m.message_id)
        bot.send_message(m.chat.id, "🔎")
        bot.send_message(m.chat.id, "Введите условия поиска!")
        bot.register_next_step_handler(m, get_search)
@bot.message_handler(commands=['start'])
def start(m):
    Nat.adduser(m.from_user.id)
    funcs.adduser(m.from_user.id)
    b = bot.get_chat_member(channel, m.from_user.id).status
    if m.from_user.language_code == "uz":
        if b != "left":
            if test.getb(m.from_user.id) == "1":
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_message(m.chat.id, f"<i>Assalomu Alaykum!</i>\n<u><b>{test.familiya(m.from_user.id)} {test.ism(m.from_user.id)}!</b>\n\n<i>Bugun nimani oʻrganishni xohlaysiz! ✅</i></u> ", reply_markup=k1(), parse_mode='html')
            else:
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_message(m.chat.id, f"Assalomu Alaykum {m.from_user.first_name}\n\nmen MATEMATIKA FANIDAN TESTLAR kanalining rasmiy botiman!", reply_markup=k2())
                bot.send_message(admin_id, f"Botga {m.from_user.first_name} /start buyrugʻini yubordi.\n\nIsmi:  {m.from_user.first_name}\n\nUsername:  @{m.from_user.username}\n\nID:  {m.from_user.id}")
        else:
            bot.delete_message(m.chat.id, m.message_id)
            bot.send_message(m.chat.id, "Kanallarga obuna boʻling!", reply_markup=obuna())
    elif m.from_user.language_code == "ru":
        funcs.adduser(m.from_user.id)
        bot.delete_message(m.chat.id, m.message_id)
        bot.send_message(m.chat.id, f"Привет {m.from_user.first_name}\n\nЯ официальный бот канала MATEMATIKADAN TESTLAR!", reply_markup=Tilbtn.ru())
@bot.message_handler(content_types=['text'])
def get_text(m):
    channeltest = bot.get_chat_member(channel, m.from_user.id).status
    if m.from_user.language_code == "uz":
        if channeltest != "left":
            if m.text == 'Kalkulyator':
                funcs.toza(m.from_user.id)
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_message(m.chat.id, "Kalkulyatorga xush kelibsiz!\nIltimos sonni kiriting", reply_markup=Calcbtn.calcb())
            elif m.text == "Chiqish ↩️ va tugatish ✔️":
                try:
                    bot.delete_message(m.chat.id, m.message_id)
                    bot.delete_message(m.chat.id, m.message_id - 1)
                    bot.send_message(m.chat.id, f"{Nat.natol(m.from_user.id)}", reply_markup=Nat.yangi())
                    bot.send_message(m.chat.id, f"Jami savollar soni: 10 ta\n✅ Toʻgʻri javoblar soni: {Nat.h(m.from_user.id)} ta")
                    Nat.delete(m.from_user.id)
                except:
                    bot.delete_message(m.chat.id, m.message_id)
                    bot.send_message(m.chat.id, Nat.natol(m.from_user.id), reply_markup=Nat.yangi())
            elif m.text == "📼 Video darslar":
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_message(m.chat.id, "Oʻzingizga kerakli boʻlimni tanlang!" , reply_markup=Video.menu())
            elif m.text == "⚙ Sozlamalar":
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_message(m.chat.id, f"Bot sozlamalariga xush kelibsiz qaysi ma'lumotni kiritmoqchisiz yoki oʻzgartirmoqchisiz!\n\nSizning ma'lumotlaringiz!\nIsmingiz: {test.ism(m.from_user.id)}\nFamiliyangiz: {test.familiya(m.from_user.id)}\nYoshingiz: {test.yosh(m.from_user.id)} da", reply_markup=edit.test1())
            elif m.text == "Asosiy sahifa ♻️":
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_photo(m.chat.id, "AgACAgIAAxkBAAICkmbYMj7HBh2xM2OS3wABIcEM19RSZgACKNsxG73HwUqoJ16vtcQvmAEAAwIAA3MAAzYE", f"<i><b>Salom! <u>{test.familiya(m.from_user.id)} {test.ism(m.from_user.id)}</u></b>\n\nTayyor boʻlsangiz quyidagi tugmani bosing!👇</i>", reply_markup=test12(), parse_mode="html")
            elif m.text == "Ma'umotlar toʻgʻri 100%":
                test.editb(m.from_user.id, 1)
                bot.delete_message(m.chat.id, m.message_id)
                bot.delete_message(m.chat.id, m.message_id - 1)
                bot.send_photo(m.chat.id, "AgACAgIAAxkBAAICkmbYMj7HBh2xM2OS3wABIcEM19RSZgACKNsxG73HwUqoJ16vtcQvmAEAAwIAA3MAAzYE", "Tayyor boʻlsngiz qiyidagi tugmani bosing! 👇", reply_markup=test12())
            elif m.text == "📊 Testda qatnashish":
                f = test.getb(m.from_user.id)
                if f == "1":
                    bot.delete_message(m.chat.id, m.message_id)
                    bot.send_photo(m.chat.id, "AgACAgIAAxkBAAICkmbYMj7HBh2xM2OS3wABIcEM19RSZgACKNsxG73HwUqoJ16vtcQvmAEAAwIAA3MAAzYE", f"<b><i>Salom!</i> <u>{test.familiya(m.from_user.id)} {test.ism(m.from_user.id)}</u></b> \n\n<i>Tayyor boʻlsangiz quyidagi tugmani bosing!👇</i>", reply_markup=test12(), parse_mode="html")
                else:
                    test.adduser(m.from_user.id)
                    bot.delete_message(m.chat.id, m.message_id)
                    bot.send_message(m.chat.id, "👋")
                    bot.send_message(m.chat.id, "👋\nKeling testni boshlashdan oldin siz bilan tanishib olamiz! ✅")
                    bot.send_message(m.chat.id, "Iltimos ismingizni kiriting!", reply_markup=mdel())
                    bot.register_next_step_handler(m, get_name)
            elif m.text == 'Tasodifiy raqam':
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_message(m.chat.id, "Tasodifiy raqam tanlandi : " + str(random.randint(1, 100)) + " ✅", reply_markup=delete())
            elif m.text == 'Ildiz':
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_message(m.chat.id, "Sonni kiriting")
                bot.register_next_step_handler(m, get_Ildiz)
            elif m.text == 'Kvadrat²':
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_message(m.chat.id, "Sonni kiriting")
                bot.register_next_step_handler(m, get_kv)
            elif m.text == 'Kub³':
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_message(m.chat.id, "Sonni kiriting")
                bot.register_next_step_handler(m, get_kub)
            else:
                bot.send_message(m.chat.id, "❌ Noma'lum buyruq!\n\nSiz to'g'ridan-to'g'ri bot chatiga xabar yubordingiz, yoki\nbot tuzilishi yaratuvchisi tomonidan o'zgartirilgan boʻlishi mumkin.\n\nℹ️ Xabarlarni to'g'ridan-to'g'ri botga yubormang yoki\n/start orqali bot menyusini yangilang", reply_markup=mdel())
        else:
            bot.delete_message(m.chat.id, m.message_id)
            bot.send_message(m.chat.id, "Kanallarga obuna boʻling!", reply_markup=obuna())
    elif m.from_user.language_code == "ru":
        if m.text == "Калькулятор":
            bot.delete_message(m.chat.id, m.message_id)
            bot.send_message(m.chat.id, "Добро пожаловать в калькулятор!\nПожалуйста, введите номер", reply_markup=Calcbtn.calcb())
        elif m.text == "Случайное число":
            bot.delete_message(m.chat.id, m.message_id)
            bot.send_message(m.chat.id, f"Было выбрано случайное число: {str(random.randint(1, 100))} ✅", reply_markup=Tilbtn.rudel())
        else:
            bot.send_message(m.chat.id, "❌ Неизвестная команда!\n\nВы отправили сообщение прямо в чат бота, или\nСтруктура бота могла быть изменена создателем.\n\nℹ️ Не отправляйте сообщения напрямую боту или\nОбновите меню бота через /start")
def get_search(m):
#    channeltest1 = bot.get_chat_member(channel, m.from_user.id).status
    if m.from_user.language_code == "ru":
        try:
            bot.delete_message(m.chat.id, m.message_id)
            bot.delete_message(m.chat.id, m.message_id - 1)
            bot.delete_message(m.chat.id, m.message_id - 2)
            wikipedia.set_lang('ru')
            bot.send_message(m.chat.id, wikipedia.summary(m.text), reply_markup=Tilbtn.rudel())
        except:
            bot.send_message(m.chat.id, "У меня нет информации,\nкоторый вы ищете!", reply_markup=Tilbtn.tu())
def get_Ildiz(m):
    global ildiz
    ildiz = m.text
    bot.delete_message(m.chat.id, m.message_id)
    bot.delete_message(m.chat.id, m.message_id - 1)
    bot.send_message(m.chat.id, f"Javob: {int(ildiz) ** 0.5}", reply_markup=k1())
def get_kv(m):
    global ildiz
    ildiz = m.text
    bot.delete_message(m.chat.id, m.message_id)
    bot.delete_message(m.chat.id, m.message_id - 1)
    bot.send_message(m.chat.id, f"Javob: {int(ildiz) ** 2}", reply_markup=k1())
def get_kub(m):
    global ildiz
    ildiz = m.text
    bot.delete_message(m.chat.id, m.message_id)
    bot.delete_message(m.chat.id, m.message_id - 1)
    bot.send_message(m.chat.id, f"Javob: {int(ildiz) ** 3}", reply_markup=k1())
@bot.callback_query_handler(func=lambda call: True)
def call(call):
    test = bot.get_chat_member(channel, call.from_user.id).status
    if call.from_user.language_code == "uz":
        if test != "left":
            if call.data == "obuna":
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.send_message(call.message.chat.id, f"Assalomu Alaykum {call.from_user.first_name}\n\nmen MATEMATIKA FANIDAN TESTLAR kanalining rasmiy botiman ", reply_markup=k1())
            elif call.data == "fam":
                try:
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    bot.delete_message(call.message.chat.id, call.message.message_id - 1)
                    bot.send_message(call.message.chat.id, "Familiyangizni kiriting!")
                    bot.register_next_step_handler(call.message, get2)
                except:
                    bot.send_message(call.message.chat.id, "Familiyangizni kiriting!")
                    bot.register_next_step_handler(call.message, get2)
            elif call.data == "ism":
                try:
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    bot.delete_message(call.message.chat.id, call.message.message_id - 1)
                    bot.send_message(call.message.chat.id, "Ismingizni qayta kiriting!", reply_markup=False)
                    bot.register_next_step_handler(call.message, get1)
                except:
                    bot.send_message(call.message.chat.id, "Ismingizni qayta kiriting!", reply_markup=False)
                    bot.register_next_step_handler(call.message, get1)
            elif call.data == "eyosh":
                try:
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    bot.delete_message(call.message.chat.id, call.message.message_id - 1)
                    bot.send_message(call.message.chat.id, "Yoshingizni qayta kiriting!")
                    bot.register_next_step_handler(call.message, get3)
                except:
                    bot.send_message(call.message.chat.id, "Yoshingizni qayta kiriting!")
                    bot.register_next_step_handler(call.message, get3)
            elif call.data == "enter":
                try:
                    d = wikipedia.search(funcs.getmatn(call.from_user.id))
                    m = ""
                    n = 0
                    for l in d:
                        r = n + 1
                        n = n + 1
                        m += f"{r}) {l}\n\n"
                    bot.send_message(call.message.chat.id, wikipedia.summary(funcs.getmatn(call.from_user.id)), reply_markup=delete(), parse_mode="html")
                    bot.send_message(call.message.chat.id, f"Balki xato qilgandirsiz!!! 👇\n\n{m}", reply_markup=kvuz.kv())
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    funcs.del1(call.from_user.id)
                except:
                    try:
                        bot.send_message(call.message.chat.id, lugat.pydev[(funcs.getmatn(call.from_user.id).lower())], reply_markup=kvuz.kv())
                        funcs.del1(call.from_user.id)
                        bot.delete_message(call.message.chat.id, call.message.message_id)
                    except:
                        bot.answer_callback_query(callback_query_id=call.id, text="❌ Topa olmadim! ✏️", show_alert=True)
                        funcs.del1(call.from_user.id)
            elif call.data == "del":
                try:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🔎\n\n|", reply_markup=kvuz.kv())
                    funcs.del1(call.from_user.id)
                except:
                    bot.answer_callback_query(callback_query_id=call.id, text="Allaqachon tozalangan! ✅", show_alert=True)
            elif call.data == "toza":
                try:
                    funcs.toza(call.from_user.id)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Kalkulyator tarixi tozalandi hisoblashda davom etishingiz mumkin!...", reply_markup=Calcbtn.calcb())
                except:
                    bot.answer_callback_query(callback_query_id=call.id, text="Juda koʻp urunishlar ❌\nMa'lumotlar tozalangan!\nRaqamlar ustiga bosib hisoblashda davom etishingiz mumkin. Hammasi 0 dan boshlanadi✅", show_alert=True)
            def wiki(m):
                try:
                    funcs.addwiki(call.from_user.id, m)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"🔎\n\n{funcs.getmatn(call.from_user.id)}|", reply_markup=kvuz.kv1())
                except:
                    bot.answer_callback_query(callback_query_id=call.id, text="❌ Xatolik\nJuda koʻp tugmani bosib yubordingiz!", show_alert=True)
            if call.data == "a":
                wiki("a")
            elif call.data == "q":
                wiki("q")
            elif call.data =="w":
                wiki("w")
            elif call.data =="e":
                wiki("e")
            elif call.data =="r":
                wiki("r")
            elif call.data =="t":
                wiki("t")
            elif call.data =="y":
                wiki("y")
            elif call.data =="u":
                wiki("u")
            elif call.data =="i":
                 wiki("i")
            elif call.data =="o":
                wiki("o")
            elif call.data =="p":
                wiki("p")
            elif call.data =="o1":
                wiki("oʻ")
            elif call.data =="s":
                wiki("s")
            elif call.data =="d":
                wiki("d")
            elif call.data =="f":
                wiki("f")
            elif call.data =="g":
                wiki("g")
            elif call.data == "h":
                wiki("h")
            elif call.data =="j":
                wiki("j")
            elif call.data =="k":
                wiki("k")
            elif call.data =="l":
                wiki("l")
            elif call.data =="g1":
                wiki("gʻ")
            elif call.data =="tutuq":
                wiki("ʼ")
            elif call.data =="z":
                wiki("z")
            elif call.data =="x":
                wiki("x")
            elif call.data =="c":
                wiki("c")
            elif call.data =="v":
                wiki("v")
            elif call.data =="b":
                wiki("b")
            elif call.data =="n":
                wiki("n")
            elif call.data =="m":
                wiki("m")
            elif call.data ==",":
                wiki(",")
            elif call.data =="pro":
                wiki(" ")
            elif call.data ==".":
                funcs.addwiki(call.from_user.id, ". ")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"🔎\n\n{funcs.getmatn(call.from_user.id)}|", reply_markup=kvuz.kv())
            elif call.data =="Q":
                wiki("Q")
            elif call.data =="W":
                wiki("W")
            elif call.data =="E":
                wiki("E")
            elif call.data =="R":
                wiki("R")
            elif call.data =="T":
                wiki("T")
            elif call.data =="Y":
                wiki("Y")
            elif call.data =="U":
                wiki("U")
            elif call.data =="I":
                wiki("I")
            elif call.data =="O":
                wiki("O")
            elif call.data =="P":
                wiki("P")
            elif call.data =="O1":
                wiki("Oʻ")
            elif call.data =="A":
                wiki("A")
            elif call.data =="S":
                wiki("S")
            elif call.data =="D":
                wiki("D")
            elif call.data =="F":
                wiki("F")
            elif call.data =="G":
                wiki("G")
            elif call.data =="H":
                wiki("H")
            elif call.data =="J":
                wiki("J")
            elif call.data =="K":
                wiki("K")
            elif call.data =="L":
                wiki("L")
            elif call.data =="G1":
                wiki("Gʻ")
            elif call.data =="Z":
                wiki("Z")
            elif call.data =="X":
                wiki("X")
            elif call.data =="C":
                wiki("C")
            elif call.data =="V":
                wiki("V")
            elif call.data =="B":
                wiki("B")
            elif call.data =="N":
                wiki("N")
            elif call.data =="M":
                wiki("M")
            elif call.data =="kichkina":
                wiki("")
            elif call.data == "katta":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"🔎\n\n{funcs.getmatn(call.from_user.id)}|", reply_markup=kvuz.kv())
            elif call.data == "text":
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.send_message(call.message.chat.id, "Jami savollar soni: 10\nTest ishlashni boshladik ❗️❗️❗️\n⏰ Vaqt belgilanmagan\n\nNatijalarni xohlagan payti chiqish tugmasi orqali ko'rishingiz mumkin 👇", reply_markup=Nat.qayt())
                bot.send_message(call.message.chat.id, "1). Hisoblang:  -78+1745 = ?\nA) 1567\nB) 1667\nC) 1777", reply_markup=test1())
            def delta(natija):
                Nat.nat(call.from_user.id, natija)
            def n():
                Nat.true(call.from_user.id)
            if call.data == "A1":
                delta("1). A)❌  B)☑️\n")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="2). Hisoblang:\n( 55 + 344 ) -- ( 122 + 44 ) = ? \nA) 203\nB) 213\nC) 233", reply_markup=test2())
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
            elif call.data == "B1":
                delta("1). B)✅\n")
                n()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="2). Hisoblang:\n( 55 + 344 ) -- ( 122 + 44 ) = ? \nA) 203\nB) 213\nC) 233", reply_markup=test2())
                bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
            elif call.data == "C1":
                delta("1). C)❌ B)☑️\n")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="2). Hisoblang:\n( 55 + 344 ) -- ( 122 + 44 ) = ? \nA) 203\nB) 213\nC) 233", reply_markup=test2())
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
            elif call.data == "A2":
                delta("2). A)❌  C)☑️\n")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="3). Hisoblang:  0,25*250= ?\nA) 62,5\nB) 63,5\nC) 64,5", reply_markup=test3())
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
            elif call.data == "B2":
                delta("2). B)❌  C)☑️\n")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="3). Hisoblang:  0,25*250= ?\nA) 62,5\nB) 63,5\nC) 64,5", reply_markup=test3())
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
            elif call.data == "C2":
                delta("2). C)✅\n")
                n()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="3). Hisoblang:  0,25*250= ?\nA) 62,5\nB) 63,5\nC) 64,5", reply_markup=test3())
                bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
            elif call.data == "A3":
                delta("3). A)✅\n")
                n()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="4). Hisoblang :   ( 33 * 6 ) : 4 = ?\nA) 48,5\nB) 49,5\nC) 50,5", reply_markup=test4())
                bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
            elif call.data == "B3":
                delta("3). B)❌  A)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="4). Hisoblang :   ( 33 * 6 ) : 4 = ?\nA) 48,5\nB) 49,5\nC) 50,5", reply_markup=test4())
            elif call.data == "C3":
                delta("3). C)❌  A)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="4). Hisoblang :   ( 33 * 6 ) : 4 = ?\nA) 48,5\nB) 49,5\nC) 50,5", reply_markup=test4())
            elif call.data == "A4":
                delta("4). A)❌  B)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="5). Hisoblang:  1430 : 26 : 5 = ?\nA) 9\nB) 11\nC) 12", reply_markup=test5())
            elif call.data == "B4":
                delta("4). B)✅\n")
                n()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="5). Hisoblang:  1430 : 26 : 5 = ?\nA) 9\nB) 11\nC) 12", reply_markup=test5())
                bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
            elif call.data == "C4":
                delta("4). C)❌  B)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="5). Hisoblang:  1430 : 26 : 5 = ?\nA) 9\nB) 11\nC) 12", reply_markup=test5())
            elif call.data == "A5":
                delta("5). A)❌  B)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="6). Hisoblang:  - 2340 + 2677 = ?\nA) 337\nB) 347\nC) 357", reply_markup=test6())
            elif call.data == "B5":
                delta("5). B)✅\n")
                n()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="6). Hisoblang:  - 2340 + 2677 = ?\nA) 337\nB) 347\nC) 357", reply_markup=test6())
                bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
            elif call.data == "C5":
                delta("5). C)❌  B)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="6). Hisoblang:  - 2340 + 2677 = ?\nA) 337\nB) 347\nC) 357", reply_markup=test6())
            elif call.data == "A6":
                delta("6). A)✅\n")
                n()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="7). Hisoblang:  ( - 977 - 178 ) : 5 = ?\nA) -211\nB) -221\nC) -231", reply_markup=test7())
                bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
            elif call.data == "B6":
                delta("6). B)❌  A)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="7). Hisoblang:  ( - 977 - 178 ) : 5 = ?\nA) -211\nB) -221\nC) -231", reply_markup=test7())
            elif call.data == "C6":
                delta("6). C)❌  A)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="7). Hisoblang:  ( - 977 - 178 ) : 5 = ?\nA) -211\nB) -221\nC) -231", reply_markup=test7())
            elif call.data == "A7":
                delta("7). A)❌  C)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="8). Hisoblang:  ( 975 : 5 ) * 2 = ?\nA) 390\nB) 400\nC) 420", reply_markup=test8())
            elif call.data == "B7":
                delta("7). B)❌  C)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="8). Hisoblang:  ( 975 : 5 ) * 2 = ?\nA) 390\nB) 400\nC) 420", reply_markup=test8())
            elif call.data == "C7":
                delta("7). C)✅\n")
                n()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="8). Hisoblang:  ( 975 : 5 ) * 2 = ?\nA) 390\nB) 400\nC) 420", reply_markup=test8())
                bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
            elif call.data == "A8":
                delta("8). A)✅\n")
                n()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="9). Hisoblang:  (6754-1456): 3= ?\nA) 1766\nB) 1966 \nC) 2266", reply_markup=test9())
                bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
            elif call.data == "B8":
                delta("8). B)❌  A)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="9). Hisoblang:  (6754-1456): 3= ?\nA) 1766\nB) 1966 \nC) 2266", reply_markup=test9())
            elif call.data == "C8":
                delta("8). C)❌  A)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="9). Hisoblang:  (6754-1456): 3= ?\nA) 1766\nB) 1966 \nC) 2266", reply_markup=test9())
            elif call.data == "A9":
                delta("9). A)✅\n")
                n()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="10). Hisoblang:  ( 456 + 566 ) : 2= ?\nA) 502\nB) 511\nC) 521", reply_markup=test10())
                bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
            elif call.data == "B9":
                delta("9). B)❌  A)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="10). Hisoblang:  ( 456 + 566 ) : 2= ?\nA) 502\nB) 511\nC) 521", reply_markup=test10())
            elif call.data == "C9":
                delta("9). C)❌  A)☑️\n")
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="10). Hisoblang:  ( 456 + 566 ) : 2= ?\nA) 502\nB) 511\nC) 521", reply_markup=test10())
            elif call.data == "A10":
                delta("10). A)❌  B)☑️")
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.send_message(call.message.chat.id, f"{Nat.natol(call.from_user.id)}", reply_markup=Nat.yangi())
                bot.send_message(call.message.chat.id, f"Jami savollar soni: 10 ta\nToʻgʻri javoblar soni: { Nat.h(call.from_user.id)} ta")
                Nat.delete(call.from_user.id)
            elif call.data == "B10":
                delta("10). B)✅")
                n()
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
                bot.send_message(call.message.chat.id, f"{Nat.natol(call.from_user.id)}", reply_markup=Nat.yangi())
                bot.send_message(call.message.chat.id, f"Jami savollar soni: 10 ta\nToʻgʻri javoblar soni: {Nat.h(call.from_user.id)} ta")
                Nat.delete(call.from_user.id)
            elif call.data == "C10":
                delta("10). C)❌  B)☑️")
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
                bot.send_message(call.message.chat.id, f"{Nat.natol(call.from_user.id)}", reply_markup=Nat.yangi())
                bot.send_message(call.message.chat.id, f"Jami savollar soni: 10 ta\nToʻgʻri javoblar soni: {Nat.h(call.from_user.id)} ta")
                Nat.delete(call.from_user.id)
            elif call.data == "delete1":
                bot.delete_message(call.message.chat.id, call.message.message_id)
            elif call.data == "1_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli Botga video joʻnatsangiz u oʻzi tokenni qaytaradi oʻsha tokenni yozing!", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "2_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "3_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "4_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "5_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "6_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "7_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "8_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "9_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "10_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "11_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "12_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "13_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "14_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "15_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "16_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "17_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "18_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "19_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "20_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "21_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "22_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "23_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "24_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "25_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "26_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "27_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "28_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "29_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "30_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "31_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data == "32_dars":
                bot.send_video(call.message.chat.id, "video tokeni yoki telegramda joylashgan video urli", caption="<b>🎞 Video\n•   Hajmi -- 483.8 MB\n•   Manba --  <a href='https://www.youtube.com/'>YouTube</a>\n\n<i><u><a href='https://t.me/Matematikauniversalbot'>Matematika | Rasmiy 𝗕𝗢𝗧</a></u></i></b>", parse_mode="html")
            elif call.data =="matematika":
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.send_message(call.message.chat.id, "Matematika kursi darslari tanlang!", reply_markup=Video.videos())
            def sonlar(n):
                funcs.changeson(call.message.chat.id, n)
                d = funcs.getSon(call.from_user.id)
                matn = ""
                try:
                    for i in d:
                        matn += i
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Hozirgi holat:\n\n{matn}", reply_markup=Calcbtn.calcb())
                except:
                    bot.answer_callback_query(call.id, "Xatolik yuz berdi!\nEndi kalkulyator siz uchun umuman ishlamasligi mumkin!!!\nBunga oʻzingiz aybdorsiz...",  show_alert=True)
            if call.data == "1":
                sonlar(1)
            elif call.data =="2":
                sonlar(2)
            elif call.data =="3":
                sonlar(3)
            elif call.data =="4":
                sonlar(4)
            elif call.data =="5":
                sonlar(5)
            elif call.data =="6":
                sonlar(6)
            elif call.data =="7":
                sonlar(7)
            elif call.data =="8":
                sonlar(8)
            elif call.data =="9":
                sonlar(9)
            elif call.data =="0":
                sonlar(0)
            def amal(amal):
                funcs.changeamal(call.from_user.id, amal)
                try:
                    data = funcs.getSon(call.from_user.id)
                    funcs.belgi(call.from_user.id)
                    matn = ""
                    for i in data:
                        matn += i
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Hozirgi holat:\n\n{matn}", reply_markup=Calcbtn.calcb())
                except:
                    bot.answer_callback_query(call.id, "Xatolik: ❌❌❌❌❌", show_alert=True)
            if call.data == "+":
                amal("+")
            elif call.data =="-":
                amal("-")
            elif call.data == "*":
                amal("*")
            elif call.data == "/":
                amal("//")
            elif call.data == "=":
                try:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Natija:\n\n{funcs.getRes(call.from_user.id)}", reply_markup=Calcbtn.calcb())
                    funcs.davomi(call.from_user.id, funcs.getRes(call.from_user.id))
                except:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Xatolik yuz berdi!", reply_markup=Calcbtn.calcb())
                    funcs.toza(call.from_user.id)
        else:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.answer_callback_query(callback_query_id=call.id, text="Barcha kanallarga obuna boʻlishingiz shart! ✅", show_alert=True)
            bot.send_message(call.message.chat.id, "Kanallarga obuna boʻling!", reply_markup=obuna())
    elif call.from_user.language_code == "ru":
        def son(n):
            funcs.changeson(call.from_user.id, n)
            try:
                d = funcs.getSon(call.from_user.id)
                matn = ""
                for i in d:
                    matn += i
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Текущий статус:\n\n{matn}", reply_markup=Calcbtn.calcb())
            except:
                bot.answer_callback_query(call.id, "Произошла ошибка ❌", show_alert=True)
        if call.data == "1":
            son(1)
        elif call.data == "2":
            son(2)
        elif call.data == "3":
            son(3)
        elif call.data == "4":
            son(4)
        elif call.data =="5":
            son(5)
        elif call.data =="6":
            son(6)
        elif call.data =="7":
            son(7)
        elif call.data =="8":
            son(8)
        elif call.data =="9":
            son(9)
        elif call.data =="0":
            son(0)
        def a(a):
            funcs.changeamal(call.from_user.id, a)
            try:
                dat = funcs.getSon(call.from_user.id)
                funcs.belgi(call.from_user.id)
                mat = ""
                for i in dat:
                    mat += i
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Текущий статус:\n\n{mat}", reply_markup=Calcbtn.calcb())
            except:
                bot.answer_callback_query(call.id, "Произошла ошибка ❌", show_alert=True)
        if call.data == "+":
            a("+")
        elif call.data == "-":
            a("-")
        elif call.data == "*":
            a("*")
        elif call.data == "/":
            a("//")
        elif call.data == "toza":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="История калькулятора очищена, и вы можете продолжить расчет!...", reply_markup=Calcbtn.calcb())
                funcs.toza(call.from_user.id)
            except:
                bot.answer_callback_query(callback_query_id=call.id, text="Слишком много попыток ❌\nДанные удалены!\nВы можете продолжить подсчет, нажимая на цифры. Все начинается с 0 ✅", show_alert=True)
        elif call.data == "=":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Результат:\n\n{funcs.getRes(call.from_user.id)}", reply_markup=Calcbtn.calcb())
                funcs.davomi(call.from_user.id, funcs.getRes(call.from_user.id))
            except:
                bot.answer_callback_query(call.id, "Произошла ошибка ❌ ♻️", show_alert=True)
        elif call.data == "delru":
            bot.delete_message(call.message.chat.id, call.message.message_id)
        elif call.data == "qoshimcha":
            bot.answer_callback_query(callback_query_id=call.id, text="Скоро!", show_alert=True)

def get1(m):
    test.addism(m.from_user.id, m.text)
    bot.delete_message(m.chat.id, m.message_id)
    bot.delete_message(m.chat.id, m.message_id - 1)
    bot.send_message(m.chat.id, "Ism tahrirlandi! ✅")
    bot.send_message(m.chat.id, f"Bot sozlamalariga xush kelibsiz qaysi ma'lumotni kiritmoqchisiz yoki oʻzgartirmoqchisiz!\n\nSizning ma'lumotlaringiz!\nIsmingiz: {test.ism(m.from_user.id)}\nFamiliyangiz: {test.familiya(m.from_user.id)}\nYoshingiz: {test.yosh(m.from_user.id)} da", reply_markup=edit.test1())
    bot.send_message(admin_id, f"Bot sozlamalari orqali ma'lumot oʻzgartirildi✏️\n Oʻzgartirilgan ma'lumot ism ✅!\n\nFoydalanuvchi ma'lumotlari!\nIsmi: {test.ism(m.from_user.id)}✅\nFamiliyasi: {test.familiya(m.from_user.id)}\nYoshi: {test.yosh(m.from_user.id)} da\nID: {m.from_user.id}\nUsername: @{m.from_user.username}", reply_markup=delete())
def get_name(m):
    test.addism(m.from_user.id, m.text)
    bot.delete_message(m.chat.id, m.message_id)
    bot.delete_message(m.chat.id, m.message_id - 1)
    bot.delete_message(m.chat.id, m.message_id - 2)
    bot.delete_message(m.chat.id, m.message_id - 3)
    bot.send_message(m.chat.id, "Yaxshi endi familiyangizni kiriting!")
    bot.register_next_step_handler(m, get_yosh)
def get2(m):
    test.addfamiliya(m.from_user.id, m.text)
    bot.delete_message(m.chat.id, m.message_id)
    bot.delete_message(m.chat.id, m.message_id - 1)
    bot.send_message(m.chat.id, "Familiya tahrirlandi! ✅")
    bot.send_message(m.chat.id, f"Bot sozlamalariga xush kelibsiz qaysi ma'lumotni kiritmoqchisiz yoki oʻzgartirmoqchisiz!\n\nSizning ma'lumotlaringiz!\nIsmingiz: {test.ism(m.from_user.id)}\nFamiliyangiz: {test.familiya(m.from_user.id)}\nYoshingiz: {test.yosh(m.from_user.id)} da", reply_markup=edit.test1())
    bot.send_message(admin_id, f"Bot sozlamalari orqali ma'lumot oʻzgartirildi✏️\n Oʻzgartirilgan ma'lumot familiya ✅!\n\nFoydalanuvchi ma'lumotlari!\nIsmi: {test.ism(m.from_user.id)}\nFamiliyasi: {test.familiya(m.from_user.id)}✅\nYoshi: {test.yosh(m.from_user.id)} da\nID: {m.from_user.id}\nUsername: @{m.from_user.username}", reply_markup=delete())
def get_yosh(m):
    test.addfamiliya(m.from_user.id, m.text)
    bot.delete_message(m.chat.id, m.message_id)
    bot.delete_message(m.chat.id, m.message_id - 1)
    bot.send_message(m.chat.id, "Yoshingiz nechada?")
    bot.register_next_step_handler(m, tasdiqlash)
def get3(m):
    test.addyosh(m.from_user.id, m.text)
    bot.delete_message(m.chat.id, m.message_id)
    bot.delete_message(m.chat.id, m.message_id - 1)
    bot.send_message(m.chat.id, "Yosh tahrirlandi! ✅")
    bot.send_message(m.chat.id, f"Bot sozlamalariga xush kelibsiz qaysi ma'lumotni kiritmoqchisiz yoki oʻzgartirmoqchisiz!\n\nSizning ma'lumotlaringiz!\nIsmingiz: {test.ism(m.from_user.id)}\nFamiliyangiz: {test.familiya(m.from_user.id)}\nYoshingiz: {test.yosh(m.from_user.id)} da", reply_markup=edit.test1())
    bot.send_message(admin_id, f"Bot sozlamalari orqali ma'lumot oʻzgartirildi✏️\n Oʻzgartirilgan ma'lumot yosh ✅!\n\nFoydalanuvchi ma'lumotlari!\nIsmi: {test.ism(m.from_user.id)}\nFamiliyasi: {test.familiya(m.from_user.id)}\nYoshi: {test.yosh(m.from_user.id)} da ✅\nID: {m.from_user.id}\nUsername: @{m.from_user.username}", reply_markup=delete())
def tasdiqlash(m):
    test.addyosh(m.from_user.id, m.text)
    bot.delete_message(m.chat.id, m.message_id)
    bot.delete_message(m.chat.id, m.message_id - 1)
    bot.send_message(admin_id, f"Yangi fiydalanuvchi\nIsmi: {test.ism(m.from_user.id)}\n<b>Familiyasi: </b> {test.familiya(m.from_user.id)}\nYoshi: {test.yosh(m.from_user.id)}\nUsername: @{m.from_user.username}\nID: {m.from_user.id}", parse_mode='html')
    bot.send_message(m.chat.id, f"Ma'lumotlaringiz toʻgʻri ekanligini tekshiring!\n\nIsmingiz: {test.ism(m.from_user.id)}\nFamiliyangiz: {test.familiya(m.from_user.id)}\nYoshingiz: {test.yosh(m.from_user.id)}\n\n\n\n\nAks holda <b>«Testda qatnashish»</b> tugmasini bosib qayta roʻyxatdan oʻting!", parse_mode='html', reply_markup=true())
bot.infinity_polling(skip_pending = True)
