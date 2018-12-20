import os
import re

import telegram


def main(request):
    bot = telegram.Bot(token=os.environ["BOT_TOKEN"])
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        message_text = update.message.text
        pattern = r'\+?\d[0-9\s\-\(\)]{7,15}\d'
        for phone in re.findall(pattern, message_text):
            formatted_phone_number = ''.join([c for c in phone if c.isnumeric()])
            result = f'https://wa.me/{formatted_phone_number}'
            bot.sendMessage(chat_id=chat_id, text=result)
    return "ok"
