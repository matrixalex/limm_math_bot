# -*- coding: utf-8 -*-

import telebot
import math
import numpy
import sympy as sympy
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt
from sympy import simplify
from sympy import apart
from sympy import diff
from sympy import init_session
import wolframalpha
import ssl
client = wolframalpha.Client(app_id)

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

@bot.message_handler(commands=['fact'])
def handle_fact(message):
	try:
		message.text=str(message)
		if(len(message.text)!=0):
			bot.send_message(message.chat.id, numpy.math.factorial(int(s)))
	except BaseException:
		bot.send_message(message.chat.id, 'Ошибка')


@bot.message_handler(commands=['simplify'])
def handle_simplify(message):
	try:
		message.text=str(message)
		if(len(message.text)!=0):
			init_printing()
			s=simplify(message.text)
			lat=sympy.latex(s)
			plt.text(0, 0.6, r"$%s$" % s, fontsize = 50)
			plt.axis('off')
			plt.savefig('plot.png')
			bot.send_message(message.chat.id, simplify(message.text))
			photo = open('plot.png', 'rb')
			bot.send_photo(message.chat.id,photo)
			plt.close()
	except BaseException:
		bot.send_message(message.chat.id, 'Ошибка при вводе выражения!')


@bot.message_handler(commands=['apart'])
def handle_apart(message):
	try:
		message.text=str(message)
		if(len(message.text)!=0):
			s=simplify(message.text)
			lat=sympy.printing.latex(s)
			plt.text(0, 0.3, r"$%s$" % lat, fontsize = 30)
			plt.axis('off')
			plt.savefig('plot.png')
			bot.send_message(message.chat.id, apart(message.text))
			photo = open('plot.png', 'rb')
			bot.send_photo(message.chat.id,photo)
			plt.close()
	except BaseException:
		bot.send_message(message.chat.id, 'Ошибка при вводе дроби!')

@bot.message_handler(commands=['solve'])
def handle_solve(message):
	try:
		message.text=str(message)
		if(len(message.text)!=0):
			bot.send_message(message.chat.id, parser.eval_(message.text))
	except BaseException:
		bot.send_message(message.chat.id, 'Ошибка при вводе выражения!')

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
    photo = open('image1.jpg', 'rb')
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

@bot.message_handler(commands=['wolfram'])
def handle_apart(message):
	try:
		message.text=str(message)
		if(len(message.text)!=0):
			res = client.query(message.text)
			bot.send_message(message.chat.id,next(res.results).text)

	except BaseException:
		bot.send_message(message.chat.id, 'Ошибка при вводе дроби!')

if __name__ == '__main__':
    bot.polling(none_stop=True)

