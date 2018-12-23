import os
import re

from telegram import Bot
from telegram.ext import Dispatcher, Updater, MessageHandler, Filters
from telegram.update import Update

BOT_TOKEN = os.environ['BOT_TOKEN']


def phone_to_wame_link(phone):
    formatted_phone_number = ''.join([c for c in phone if c.isnumeric()])
    result = f'https://wa.me/{formatted_phone_number}'
    return result


def contact_callback(bot, update):
    message = update.message
    contact = update.effective_message.contact
    phone = contact.phone_number
    message.reply_text(text=phone_to_wame_link(phone))


def message_handler(bot, update):
    message = update.message
    message_text = message.text
    pattern = r'\+?\d[0-9\s\-\(\)]{7,15}\d'
    for phone in re.findall(pattern, message_text):
        message.reply_text(text=phone_to_wame_link(phone))


def set_handlers(dispatcher):
    echo_handler = MessageHandler(Filters.text, message_handler)
    dispatcher.add_handler(echo_handler)
    contact_handler = MessageHandler(Filters.contact, contact_callback)
    dispatcher.add_handler(contact_handler)


def setup_dispatcher(token):
    bot = Bot(token)
    dispatcher = Dispatcher(bot, None, workers=0)
    set_handlers(dispatcher)
    return dispatcher


def main(request):
    if request.method == "POST":
        dispatcher = setup_dispatcher(token=BOT_TOKEN)
        update = Update.de_json(request.get_json(force=True), dispatcher.bot)
        dispatcher.process_update(update)
    return "ok"


if __name__ == '__main__':
    # DEBUG ONLY
    webhook_url = os.environ['WEBHOOK_URL']
    updater = Updater(token=BOT_TOKEN)
    set_handlers(updater.dispatcher)
    updater.start_webhook(listen='0.0.0.0',
                          port=4000,
                          url_path='/',
                          webhook_url=webhook_url)
    updater.bot.set_webhook(webhook_url)
