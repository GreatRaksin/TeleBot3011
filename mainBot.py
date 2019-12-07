import telebot
from random import randint

bot = telebot.TeleBot('1022635227:AAEi2woyfX_SWvKlpztyWHOHM-RIVIeFids')
kboard1 = telebot.types.ReplyKeyboardMarkup()
kboard1.row('Привет', 'Пока')

stickers = [
    'CAADAgADdwgAArnWiwIi5eIJihlNqhYE',
    'CAADAgADcRsAAkKvaQABxGrqRKCHd68WBA'
]


@bot.message_handler(commands=['start'])
def startMessage(message):
    bot.send_message(message.chat.id, 'Доброе утро, девочки!', reply_markup=kboard1)


@bot.message_handler(content_types=['text'])
def sendText(message):
    if message.text.lower().startswith(('прив', 'дар', 'здра', 'здар', 'h')):
        bot.send_sticker(message.chat.id, 'CAADAgADcRsAAkKvaQABxGrqRKCHd68WBA')
    elif message.text.lower().startswith(('п', 'б', 'b', 'до')):
        bot.send_sticker(message.chat.id, 'CAADAgADcxsAAkKvaQAB067jXaufa7gWBA')
    elif message.text.lower == 'оцени мой шедевр':
        bot.send_message(message.chat.id, 'Пришли картинку.')

        if message.text == message.file:
            bot.send_sticker(message.chat.id, 'CAADAgADdxsAAkKvaQAB-6zAoEGW87cWBA')


@bot.message_handler(content_types=['sticker'])
def sendSticker(message):
    print(message)

bot.polling()

