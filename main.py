# -*- coding: utf-8 -*-

from PIL import Image
from boto.s3.connection import S3Connection
import config
import telebot
import parser
import os
import requests  
from flask import Flask, request

token = S3Connection(os.environ['token'])
token = '439470650:AAHup458zfpbjGp4c_78E4nMuzcSlRzIcv0'
bot=telebot.TeleBot(token)

PORT = int(os.environ.get('PORT', '5000'))
updater = Updater(token)

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
def handle_hui(message):
    message.text=str(message)
    bot.send_message(message.chat.id, parser.eval_(message.text))

@bot.message_handler(commands=['photo'])
def handle_photo(message):
    photo = open('image1.jpg', 'r')
    bot.send_photo(message.chat.id, photo)

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=token)
updater.bot.set_webhook("https://limm-math-bot.herokuapp.com/" + token)
updater.idle()
