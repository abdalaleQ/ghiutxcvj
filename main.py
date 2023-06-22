import telebot

import requests

bot = telebot.TeleBot('6227667077:AAEUQUCyrDcKwzkE_pBpS52GD8SULKf9DR0')

@bot.message_handler(commands=['start'])

def send_welcome(message):

    chat_id = message.chat.id

    user = message.from_user

    name = user.first_name

    from_id = user.id

    bot.send_message(chat_id, f"اهلا بك في بوت الذكاء الاصطناعي ارسل اي شي سأرد عليَك\n", reply_markup=telebot.types.InlineKeyboardMarkup([[telebot.types.InlineKeyboardButton(text='قناة البوت', url='Sero_Bots.t.me')]]))

    with open('ids', 'r') as f:

        if str(from_id) not in f.read():

            with open('ids', 'a') as ids_file:

                ids_file.write(f"{from_id}\n")

            bot.send_message(chat_id, "نورت البوت 🌹")

            bot.send_message(5561152568, f"تم دخول شخص جديد الي البوت ✈️\n"

                                         f"اسم المستخدم: [@{user.username}]\n"

                                         f"اسم الشخص: [{name}](tg://user?id={chat_id})\n"

                                         f"ايديه : {from_id}\n"

                                         f"عدد المستخدمين الكلي : ❲{len(open('ids').read().splitlines())}❳\n", 

                                         parse_mode="markdown")

@bot.message_handler(func=lambda message: True)

def response(message):

    text = message.text

    chat_id = message.chat.id

    j = bot.send_message(chat_id, "انتضر قليلا | Wait Please").message_id

    try:

        r = requests.get("https://gptzaid.zaidbot.repl.co/1/text=" + requests.utils.quote(text))

        ChatGpt = r.text

        bot.edit_message_text(chat_id=chat_id, message_id=j, text=ChatGpt, 

                              reply_markup=telebot.types.InlineKeyboardMarkup([[telebot.types.InlineKeyboardButton(text='قناة البوت', url='Sero_Bots.t.me')]]))

    except Exception as e:

        bot.edit_message_text(chat_id=chat_id, message_id=j, text=f"{e} \n ارسل هذا الخطا للمطور لطفا ✈️ \n - @x_Bero ")

bot.polling()
