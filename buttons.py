from telebot import types

def register_buttons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_phone = types.KeyboardButton("Отправить номер телефона", request_contact=True)
    button_location = types.KeyboardButton("Отправить локацию", request_location=True)
    markup.add(button_phone, button_location)
    return markup
