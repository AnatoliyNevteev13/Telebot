import telebot
import Configuration
import Classes


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help' ])
def help(message: telebot.types.Message):
    text = 'To start give a command to the Bot: \n<currency name> \
           <exchanging currency> \
           <amount>'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values' ])
def values(message: telebot.types.Message):
    text = 'Available currencies:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ProgramExceptions('Too many arguments. ')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except Exception:
        bot.reply_to(message, f'Cannot process command\n{e}')
    else:
    text = f'Price {amount} {quote} in {base} - {total_base}'
    bot.send_message(message.chat.id, text)


bot.polling()