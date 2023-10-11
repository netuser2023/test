import telebot
import webbrowser
from telebot import types
bot = telebot.TeleBot('6499649891:AAEwJUCVCem1MqJg4eXyHMQNCvdv-eAiFak')

@bot.message_handler(commands=["youtube"])
def youtube(message):
    webbrowser.open('https://youtube.com')

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, "Саймон «Гоуст» Райли (англ. Simon «Ghost» Riley) — вымышленный персонаж сюжетной линии Modern Warfare серии Call of Duty. Впервые он появляется в качестве основного игрового персонажа в компьютерной игре 2009 года Call of Duty: Modern Warfare 2. Обновлённая версия Гоуста была упомянута в перезапуске серии 2019 года Call of Duty: Modern Warfare и в сопутствующей ей Call of Duty: Warzone, где он стал игровым персонажем. Полноценный дебют состоялся в Call of Duty: Modern Warfare II 2022 года.")

@bot.message_handler(commands=['start', 'hello', '?'])
def main(message):
    bot.send_message(message.chat.id, f"<b>Hello</b> how are you? <b>{message.from_user.first_name}</b>", parse_mode="html")


name = ""
surname = ""
age = 0

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "/reg":
        bot.send_message(message.from_user.id, "What's your name? ")
        bot.register_next_step_handler(message, get_name)

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Whats your surname? ")
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "How old are you? ")
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    if age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Write in numbers please ')
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Yes', callback_data='yes')
    keyboard.add(key_yes) 
    key_no= types.InlineKeyboardButton(text='No', callback_data='no')
    keyboard.add(key_no)
    question = 'Your are '+ str(age) +' years old, Your name is ' + name + " " + surname + '?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": 
        bot.send_message(call.message.chat.id, 'Keep in mind 🙂')
    else:
        bot.send_message(call.message.chat.id, "I'm sorry 😔")

@bot.message_handler()
def message(message):
    if message.text == "Hello" or "hello":
        bot.send_message(message.chat.id, "Hello!!", parse_mode="html")
    elif message.text == "How are you?" or "how are you?":
        bot.send_message(message.chat.id, "I'm fine 😄", parse_mode="html")
    else:
        bot.send_message(message.chat.id, "I don't understand you, if you can leave feedback to my developer ---> @netuser2023", parse_mode="html")

bot.polling(non_stop=True)


