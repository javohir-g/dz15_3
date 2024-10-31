import telebot
from buttons import register_buttons


bot = telebot.TeleBot('7927478236:AAEaWaz1v2rNK9W5Oc2cZ7PPRjDhaZZMUHk')

users_data = {}

@bot.message_handler(commands=['start'])
def welcome(message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    users_data[user_id] = {"first_name": user_first_name}
    bot.send_message(message.chat.id, f"Привет, {user_first_name}!\nПожалуйста, зарегистрируйтесь.", reply_markup=register_buttons())


@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    user_id = message.from_user.id
    if message.contact is not None:
        users_data[user_id]["phone_number"] = message.contact.phone_number
        bot.send_message(message.chat.id, "Спасибо за номер телефона!")


@bot.message_handler(content_types=['location'])
def location_handler(message):
    user_id = message.from_user.id
    if message.location is not None:
        users_data[user_id]["location"] = (message.location.latitude, message.location.longitude)
        bot.send_message(message.chat.id, "Спасибо за локацию!")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "Справка:\n/start - Начало регистрации\n/help - Справочная информация")


bot.polling()
