# -*- coding: utf-8 -*-

import telebot
import math
#import sympy
from sympy import simplify
from sympy import apart
from sympy import diff
from sympy.parsing.sympy_parser import parse_expr

#ссскномер
#import Image

import parser		  
import config
import graphics
import dworker


token=config.token
bot=telebot.TeleBot(token)


def str(message): #Удаление команды из строки
    if message.text[0]=='/':
        if len(message.text)==0:
            bot.send_message(message.chat.id, "Введите аргументы команды!")
            return ''
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
    if(len(message.text)!=0):
        bot.send_message(message.chat.id, message.text)

@bot.message_handler(commands=['diff'])
def handle_diff(message):
    message.text=str(message)
    if(len(message.text)!=0):
        s=simplify(message.text)
        bot.send_message(message.chat.id, diff(message.text))


#@bot.message_handler(commands=['simplify'])
def handle_simplify(message):
    message.text=str(message)
    if(len(message.text)!=0):
        s=simplify(message.text)
        bot.send_message(message.chat.id, simplify(message.text))

#@bot.message_handler(commands=['apart'])
def handle_apart(message):
    message.text=str(message)
    if(len(message.text)!=0):
        def func(x):
            return eval(message.text)
        bot.send_message(message.chat.id, apart(func,x))

@bot.message_handler(commands=['solve'])
def handle_solve(message):
    message.text=str(message)
    if(len(message.text)!=0):
        bot.send_message(message.chat.id, parser.eval_(message.text))

@bot.message_handler(commands=['plot'])
def handle_plot(message):
	
	func=message.text=str(message)
	but1 =  telebot.types.InlineKeyboardButton(text="Android",callback_data="IOS") 
	bot.send_message(message.chat.id,"Введите левую границу интервала: ")
	photo = graphics.simple_graph(message.text)
	bot.send_photo(message.chat.id, photo)
	bot.send_message(message.chat.id,"Введите левую границу интервала: ")


@bot.message_handler(commands=['photo'])
def handle_photo(message):
    photo = open('smither/image1.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['animate'])
def handle_animate(message):
	message.text=str(message)
	if(len(message.text)!=0):
		if 'z' in message.text:
			bot.send_message(message.chat.id, "Поверхность должна быть задана в явном виде!")
			return
		graphics.movie_graph(message.text)
		photo = open('movie.gif', 'rb')
		bot.send_document(message.chat.id, photo)

if __name__ == '__main__':
    bot.polling(none_stop=True)

