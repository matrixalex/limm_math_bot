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


from sympy.parsing.sympy_parser import parse_expr

#ссскномер
#import Image

import parser		  
import config
import graphics
import dworker


token=config.token
bot=telebot.TeleBot(token)

wolfram_app_id = config.wolfram_app_id
client = wolframalpha.Client(wolfram_app_id)


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
            result=result+message.text[i]
            if (i<len(message.text)-1):
                 result += ' '
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
		bot.send_message(message.chat.id, 'Ошибка факторизации')


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
			photo = open('plot.png', 'rb')
			bot.send_photo(message.chat.id,photo, s)
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

@bot.message_handler(commands=['solve', 'SOLVE'])
def handle_solve(message):
	try:
		message.text=str(message)
		if(len(message.text)!=0):
			bot.send_message(message.chat.id, parser.eval_(message.text))
	except BaseException:
		bot.send_message(message.chat.id, 'Ошибка при вводе выражения!')

@bot.message_handler(commands=['sqrt'])
def handle_sqrt(message):
	if(0==0):
		message.text=str(message)
		if(len(message.text)!=0):
			hui = message.text.split(" ")[0]
			c = complex(hui)
			n = int(message.text.split(" ")[1])
			l = math.pow(c.real**2+c.imag**2,1/n)
			alpha = math.atan(c.imag/c.real)
			s = ''
			for i in range [0:n-1]:
				p1 = l*math.cos((alpha+2*math.pi*i)/n)
				p2 = l*math.sin((alpha+2*math.pi*i)/n)
				p = complex(p1,p2)
				if i != n-1:
					s += p+' , '
				else: s+= p
			bot.send_message(message.chat.id, s)
	#except BaseException:
	#	bot.send_message(message.chat.id, 'Ошибка при вводе выражения!')

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
	try:
		message.text=str(message)
		if(len(message.text)!=0):
			if 'z' in message.text:
				bot.send_message(message.chat.id, "Поверхность должна быть задана в явном виде!")
				return
			graphics.movie_graph(message.text)
			photo = open('movie.gif', 'rb')
			bot.send_document(message.chat.id, photo)
	except BaseException:
		bot.send_message(message.chat.id, 'Ошибка при вводе поверхности')

@bot.message_handler(func=lambda message: message.text!='')
def handle_wolfram(message):
	try:							  
	#	message.text=str(message)
		if(len(message.text)!=0):
			res = client.query(message.text)
			s = next(res.results).text
			bot.send_message(message.chat.id, s)
			#lat=sympy.printing.latex(s)
			#plt.text(0, 0.3, r"$%s$" % lat, fontsize = 30)
			#plt.axis('off')
			#plt.savefig('plot.png')
			#photo = open('plot.png', 'rb')
			#bot.send_photo(message.chat.id,photo, s)

	except BaseException:
		bot.send_message(message.chat.id, 'Неверный запрос к базе знаний Wolfram Alpha')

if __name__ == '__main__':
    bot.polling(none_stop=True)

