from telebot import TeleBot
from user import *

TOKEN = 'TG_TOKEN'  # MY-MAIN
bot = TeleBot(TOKEN)


@bot.message_handler()
def get_info(message):
    user_id = message.from_user.id
    bot.send_message(user_id, f'Your ID:\n{user_id}')
    print(user_id)

print('Bot is almost there!')
bot.polling(none_stop=True)
