import telebot

from keys import telegramkey
from binance import handleBinance
from currency import handleCurrency
from gas import handleGas
from mexc import handleMexc
from okx import handleOkx
from paribu import handleParibu
from coingecko import handleCoingecko

bot = telebot.TeleBot(telegramkey)

@bot.message_handler(content_types=['text'])
def handleMessage(message):

    resultMessage = ""
    chat_id = message.chat.id

    try:
        resultMessage = handleBinance(message, resultMessage)
        resultMessage = handleCurrency(message, resultMessage)
        resultMessage = handleGas(message, resultMessage)
        resultMessage = handleMexc(message, resultMessage)
        resultMessage = handleCoingecko(message, resultMessage)
        resultMessage = handleOkx(message, resultMessage)
        resultMessage = handleParibu(message, resultMessage)
    except:
        resultMessage = "Not available."
    
    if message.text.startswith('/'):
        resultMessage = "Try without typing '/'."
        
    if resultMessage != "":
        bot.send_message(chat_id, resultMessage)

bot.polling()
