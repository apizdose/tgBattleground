import charactions
import telebot
from telebot import types

bot = telebot.TeleBot('YOUR TOKEN')

@bot.message_handler(commands=["join"])
def join(message):
    chat_id=message.chat.id
    username = message.from_user.username
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("/dmg")
    item2=types.KeyboardButton("/heal")
    markup.add(item1)	
    markup.add(item2)
    charactions.charGen(username)

    bot.send_message(chat_id=chat_id,text=f"@{username} в игре. Стартовый запас здоровья и маны: {charactions.characters[username]['hp']}-hp, {charactions.characters[username]['mp']}-mp",reply_markup=markup)

@bot.message_handler(commands=["tab"])
def tab(message):
    chat_id=message.chat.id
    stat=charactions.characters

    bot.send_message(chat_id=chat_id,text=f"{stat}")

@bot.message_handler(commands=["dmg"])
def dmg(message):
    username = message.from_user.username
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in charactions.characters:
        markup.add(f'/attack: {i}')

    bot.reply_to(message, f"@{username}, кого ты атакуешь?", reply_markup=markup)
    

@bot.message_handler(commands=["attack:"])
def attack(message):
    username = message.from_user.username
    msg=str(message.text)
    enemy=msg.split(maxsplit=1)[1]
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("/dmg")
    item2=types.KeyboardButton("/heal")
    markup.add(item1)	
    markup.add(item2)
    bot.reply_to(message,'Атака!!!',reply_markup=markup)
    dmg=charactions.dmg()
    charactions.hit(enemy,dmg)

    bot.reply_to(message, f"@{username} наносит {dmg} урона {enemy}. Здоровье @{enemy} теперь равно: {charactions.characters[enemy]['hp']}",reply_markup=markup)

@bot.message_handler(commands=["heal"])
def heal(message):
    username = message.from_user.username
    heal=charactions.heal()
    charactions.restore(username,heal)

    bot.reply_to(message, f"@{username} восстанавливает здоровье. @{username} запас здоровья и маны: {charactions.characters[username]['hp']}-hp, {charactions.characters[username]['mp']}-mp")



@bot.message_handler(func=lambda message: True)
def handle_message(message):

    bot.reply_to(message, f"На реставрации, пиши /join и поиграем.")
        

bot.infinity_polling()
