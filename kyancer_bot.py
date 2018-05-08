# -*- coding: utf-8 -*-
"""
Created on Tue May 08 18:08:37 2018

@author: Isaac Ng
"""
# experiment for how inline bots work
# kyancer_bot
# remember to `pip install python-telegram-bot --upgrade`

from uuid import uuid4

from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from random import random
from string import ascii_letters
ascii_letters = unicode(ascii_letters)

import logging
import os
# import re # unused, but needed for future versions


# get api key from environment variable. 
# Replace this if you wish but don't git commit it if you do
TOKEN = os.environ[u"KYANCER_TELE_KEY"]
tele_message_maxlen = 4096 

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text(u"Hi!")


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text(u"I'm an inline bot! Use @kyancer_bot <your text here> to give people headaches!")


def inlinequery(bot, update):
    """Handle the inline query."""
    query = update.inline_query.query
    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title= u"|<y4n¢1ƒy!!!",
            input_message_content=InputTextMessageContent(
                kyancify(query))),
               ]

    update.inline_query.answer(results)

def kyancify(query):
    """Converts text to 1337$|º34|<"""
    query = unicode(query.lower())
    replacements = u"ə6¢d£ƒ6h1]ꓘ|ᴍɴᴏᴘǫ®s✚ᴜ✌ᴡ❌ʏᴢ"
    # boring 1 character replacements
    for n in zip(ascii_letters, replacements):
        query = psr(n[0], n[1], query, probability = 0.4)
    # more complex replacements
    query = psr(u"a", u"ə", query, probability = 0.8)
    query = psr(u"a", u"4", query, probability = 0.9)
    query = psr(u"b", u"🅱", query, probability = 0.99)
    query = psr(u"c", u"(", query, probability = 0.9)
    query = psr(u"d", u"cl", query, probability = 0.9)
    query = psr(u"e", u"Ɛ", query, probability = 0.9)
    query = psr(u"f", u"/=", query, probability = 0.9)
    query = psr(u"g", u"(_+", query, probability = 0.9)
    query = psr(u"h", u"]-[", query, probability = 0.9)
    query = psr(u"i", u"!", query, probability = 0.9)
    query = psr(u"j", u"]", query, probability = 0.9)
    query = psr(u"k", u"|<", query, probability = 0.9)
    query = psr(u"l", u"ℓ", query, probability = 0.9)
    query = psr(u"m", u"^^", query, probability = 0.9)
    query = psr(u"m", u"|\\|", query, probability = 0.9)
    query = psr(u"o", u"Θ", query, probability = 0.9)
    query = psr(u"p", u"|º", query, probability = 0.9)
    query = psr(u"q", u"0_", query, probability = 0.9)
    query = psr(u"r", u"I2", query, probability = 0.9)
    query = psr(u"s", u"$", query, probability = 0.9)
    query = psr(u"t", u"+", query, probability = 0.9)
    query = psr(u"u", u"บ", query, probability = 0.1)
    query = psr(u"u", u"µ", query, probability = 0.9)
    query = psr(u"v", u"\\/", query, probability = 0.9)
    query = psr(u"w", u"vV", query, probability = 0.9)
    query = psr(u"x", u"Ж", query, probability = 0.9)
    query = psr(u"y", u"¥", query, probability = 0.9)
    query = psr(u"z", u"7_", query, probability = 0.9)
    return query

def psr(pattern, replacement, input_string, probability = 0.5):
    """Probabilistic string replcements - used to kyancify stuff"""
    # only works for single chars so far - rewrite later using regex perhaps
    # also probably not the most efficient method but who cares it's still fast
    output_string = []
    for i in range(len(input_string)):
        output_string.append(u"ERR")
        r = random()
        if pattern == input_string[i] and r < probability:
            output_string[i] = replacement
        else:
            output_string[i] = input_string[i]
    return "".join(output_string)

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning(u'Update "%s" caused error "%s"', update, error)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler(u"start", start))
    dp.add_handler(CommandHandler(u"help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(InlineQueryHandler(inlinequery))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == u"__main__":
    main()
    
    
