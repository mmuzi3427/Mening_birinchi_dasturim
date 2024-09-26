<h1><p align="center">Mening birinchi dasturimga xush kelibsiz </p></h1>
<p align="center">Assalomu Alaykum hammaga bu yerga men birinchi telegram bot dasturimni yukladim!</p>

[![PyPi Package Version](https://img.shields.io/pypi/v/pyTelegramBotAPI.svg)](https://pypi.python.org/pypi/pyTelegramBotAPI)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/pyTelegramBotAPI.svg)](https://pypi.python.org/pypi/pyTelegramBotAPI)

[![Documentation Status](https://readthedocs.org/projects/pytba/badge/?version=latest)](https://pytba.readthedocs.io/en/latest/?badge=latest)
[![PyPi downloads](https://img.shields.io/pypi/dm/pyTelegramBotAPI.svg)](https://pypi.org/project/pyTelegramBotAPI/)
[![PyPi status](https://img.shields.io/pypi/status/pytelegrambotapi.svg?style=flat-square)](https://pypi.python.org/pypi/pytelegrambotapi)

# <p align="center">pyTelegramBotAPI
<h1><a href="https://t.me/Matematikauniversalbot?start=true">Meni birinchi Telegram botim</a></h1>

## <p align="center">Qo'llab-quvvatlanadigan Bot API versiyasi: <a href="https://core.telegram.org/bots/api#august-14-2024"><img src="https://img.shields.io/badge/Bot%20API-7.9-blue?logo=telegram" alt="Supported Bot API version"></a>
```sablime
import
```

```python
import telebot

bot = telebot.TeleBot("7698002161:AAETkVO9y5SiPw_XRVIhlTpiZyDx5wxLiyY", parse_mode=None)# @BotFather dan olingan bot tokeni

@bot.message_handler(commands=['start', 'yordam'])
def start(xabar):
    bot.reply_to(xabar, f"Assalomu Alaykum {xabar.from_user.first_name}")

bot.infinity_polling()
```



