import os
import requests
from pyrogram import filters
from main import get_text , get_url_song
from config import bot

@bot.on_message(filters.command('start'))
def text_1(bot , message):
    bot.send_message(message.chat.id,f'Привет {message.from_user.first_name}! \n Я бот помогающий искать текст песен! \n Вбивай любую песнь в формате /search (название) и получай текст!')

@bot.on_message(filters.command('search'))
def search(bot , message):
    try:
        text = ' '.join(message.text.split()[1:])
        print(text)
        bot.send_message(message.chat.id,f'Ищу текст твоей песни!')
        url = get_url_song(text)
        result = get_text(text,url)
        if result:
            bot.send_document(message.chat.id, f"{text}.txt", caption="Держи текст песни!")
        else:
            bot.send_message(message.chat.id,"Не удалось достать текст!")
        os.remove(f"{text}.txt")
    except IndexError :
        bot.send_message(message.chat.id,"А какую именно песню? Тут не написано какая")
bot.run()