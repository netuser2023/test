import telebot
from telebot import types

bot = telebot.TeleBot('6499649891:AAEwJUCVCem1MqJg4eXyHMQNCvdv-eAiFak')

# @bot.message_handler()
# def get_user_text(message):
#     if message.text == "Hello":
#         bot.send_message(message.chat.id, "Hello!!!", parse_mode="html")
#     elif message.text == "How are you?":
#         bot.send_message(message.chat.id, "I'm fine and you?", parse_mode="html")
#     elif message.text == "I'm good" or "I'm fine":
#         bot.send_message(message.chat.id, "Good :)", parse_mode="html")   
#     else:
#         bot.send_message(message.chat.id, "I didn't understand you :(")


@bot.message_handler(content_types=["text"])
def chat(message):
    if message.text == "Whats your name?":
        bot.send_message(message.chat.id, "My name is ITCSINFO BOT", parse_mode="html")
    elif message.text == "I can change your name?":
        bot.send_message(message.chat.id, "unfortunately you can't change my name", parse_mode="html")
    elif message.text == "Who created you?":
        bot.send_message(message.chat.id, "I was created by @netuser2023", parse_mode="html")
    else:
        bot.send_message(message.chat.id, "I don't understand you, if you can leave feedback to my developer ---> @netuser2023", parse_mode="html")


bot.polling(non_stop=True)