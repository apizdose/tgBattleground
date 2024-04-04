import charactions
import charstats
import telebot
from telebot import types
import time
import playersqueque

bot = telebot.TeleBot('')



@bot.message_handler(commands=["start"])
def join(message):
    chat_id=message.chat.id
    username = message.from_user.username
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("/join")
    item2=types.KeyboardButton("/tab")
    markup.add(item1)	
    markup.add(item2)
    charstats.start(chat_id)
    playersqueque.start(chat_id)

    bot.send_message(chat_id=chat_id,text=f"@{username} стартует игру",reply_markup=markup)

@bot.message_handler(commands=["join"])
def join(message):
    chat_id=message.chat.id
    username = message.from_user.username
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True,selective=True)
    item1=types.KeyboardButton("/attack")
    item2=types.KeyboardButton("/heal")
    markup.add(item1)	
    markup.add(item2)
    char=charstats.join(chat_id,username)
    if char:
        playersqueque.join(chat_id,username)
        bot.send_message(chat_id=chat_id,text=f"@{username} в игре. Стартовый запас здоровья и маны: {char['hp']}-hp, {char['mp']}-mp",reply_markup=markup)
    else:
        bot.send_message(chat_id=chat_id,text=f"@{username} уже в игре.",reply_markup=markup)


@bot.message_handler(commands=["test"])
def test(message):
    chat_id=message.chat.id
    username = message.from_user.username
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True,selective=True)
    item1=types.KeyboardButton(username)
    
    markup.add(item1)	
    
    bot.reply_to(message,text=f"@{username} test",reply_markup=markup)
    


@bot.message_handler(commands=["tab"])
def tab(message):
    chat_id=message.chat.id
    stat=charstats.tab(chat_id)
    bot.send_message(chat_id=chat_id,text=f"{stat}")


@bot.message_handler(commands=["attack","heal"])
def target(message):
    username = message.from_user.username
    chat_id=message.chat.id
    quequed=playersqueque.get(chat_id)[0]
    if username == quequed:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        players=charstats.players(chat_id)
        if message.text=="/attack":
            for i in players:
                if i == username:
                    continue
                markup.add(f'/attack: {i}')
        if message.text=="/heal":
            for i in players:
                markup.add(f'/restore: {i}')
        
        bot.reply_to(message, f"@{username} Выбери цель!", reply_markup=markup)
    if username != quequed:
        pass
    
@bot.message_handler(commands=["attack:"])
def attack(message):
    username = message.from_user.username
    chat_id=message.chat.id
    quequed=playersqueque.get(chat_id)[0]
    

    if username == quequed:
        msg=str(message.text)

        enemy=msg.split(maxsplit=1)[1]

        hit=charactions.attack(chat_id,username,enemy)
        
        targethp=charstats.data[chat_id]["players"][enemy]["hp"]

        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("/attack")
        item2=types.KeyboardButton("/heal")
        markup.add(item1)	
        markup.add(item2)
        playersqueque.roll(chat_id)

        bot.send_message(chat_id=message.chat.id,text=f"@{username} наносит {hit} урона @{enemy}. Здоровье @{enemy} теперь равно: {targethp}\n\nТеперь ход @{playersqueque.get(chat_id)[0]}",reply_markup=markup)
        
        time.sleep(3)
        



    else:
        bot.send_message(chat_id=message.chat.id,text=f"Не твоя очередь")
        




@bot.message_handler(commands=["restore:"])
def restore(message):
   
    username = message.from_user.username
    chat_id=message.chat.id
    quequed=playersqueque.get(chat_id)[0]
    

    if username == quequed:
        msg=str(message.text)

        enemy=msg.split(maxsplit=1)[1]

        heal=charactions.restore(chat_id,username,enemy)
        
        targethp=charstats.data[chat_id]["players"][enemy]["hp"]

        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("/attack")
        item2=types.KeyboardButton("/heal")
        markup.add(item1)	
        markup.add(item2)
        playersqueque.roll(chat_id)
        bot.send_message(chat_id=message.chat.id,text=f"@{username} восстанавливает {heal} здоровья @{enemy}. Здоровье @{enemy} теперь равно: {targethp}\n\nТеперь ход @{playersqueque.get(chat_id)[0]}",reply_markup=markup)
        
    else:
        bot.send_message(chat_id=message.chat.id,text=f"Не твоя очередь")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text=="help":      
        bot.reply_to(message, f"На реставрации, пиши /join и поиграем.")
    if message.text=="/drop":
         bot.reply_to(message, f"...",reply_markup=types.ReplyKeyboardRemove())
    
    
        

bot.infinity_polling()
