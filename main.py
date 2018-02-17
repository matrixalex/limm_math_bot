# -*- coding: utf-8 -*-

from PIL import Image
import telebot

import parser
import config
import math
from os import environ


token=environ.get('token')

bot=telebot.TeleBot(token)

def str(message): #Удаление команды из строки
    if message.text[0]=='/':
        #temp='\\'+command+' '
        #message.text=message.text.replace(temp,'')
        message.text=message.text.split(" ")
        result=''
        i=1
        while i<len(message.text):
            result=result+' '+message.text[i]
            i=i+1
    return result

@bot.message_handler(commands=['echo'])
def handle_echo(message):
    message.text=str(message)
    bot.send_message(message.chat.id, message.text)

@bot.message_handler(commands=['solve'])
def handle_solve(message):
    message.text=str(message)
    bot.send_message(message.chat.id, parser.eval_(message.text))

@bot.message_handler(commands=['photo'])
def handle_photo(message):
    photo = open('image1.jpg', 'r')
    bot.send_photo(message.chat.id, photo)

if __name__ == '__main__':
    bot.polling(none_stop=True)
