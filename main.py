import os
import telegram


def main(request):
    bot = telegram.Bot(token=os.environ["BOT_TOKEN"])
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        message_text = update.message.text
        formatted_phone_number = ''.join([c for c in message_text if c.isnumeric()])[-11:]
        result = f'https://wa.me/{formatted_phone_number}'
        bot.sendMessage(chat_id=chat_id, text=result)
    return "ok"
