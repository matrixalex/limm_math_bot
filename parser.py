import math
import re

OPERATORS = {'+' : (1, lambda x, y: x + y), 
			 '-' : (1, lambda x, y: x - y),
			 '*' : (2, lambda x, y: x * y), 
			 '/' : (2, lambda x, y: x / y),
			 '©' : (3, lambda x, y: math.cos(y*math.pi/180)), # cos
			 '$' : (3, lambda x, y: math.sin(y*math.pi/180)), # sin
			 'Ù' : (3, lambda x, y: math.tan(y*math.pi/180)), # tg
			 '¬' : (3, lambda x, y: math.tan(y*math.pi/180))} # ctg
				 
CHANGES = {'cos' : '©',
		   'sin' : '$',
		   'tg' : 'Ù',
		   'ctg' : '¬'}

def eval_(formula):
	def normalize (dirty_string):
		for key in CHANGES:
			dirty_string=dirty_string.replace(key, CHANGES[key])
		dirty_string=dirty_string.strip()  #удаление пробелов
		if dirty_string[0] in OPERATORS:			 # это условие и следующикл цикл для "бинаризации" унарных операторов
			dirty_string = ''+'1'+dirty_string[0:]		 
		i=1
		j=2
		while(j<len(dirty_string)):	             # МММ ООО
			if ((dirty_string[i] in OPERATORS or dirty_string[i] in "(") and (dirty_string[j] in OPERATORS)):
				dirty_string=''+dirty_string[:j]+'1'+dirty_string[j:]+ dirty_string[j+1:]
				i=i+1
				j=j+1
			i=i+1
			j=j+1
		dirty_string=dirty_string.strip()
		return dirty_string

	def parse(formula_string):
		number = ''
		for s in formula_string:
			if s in '1234567890.':
				number += s
			elif number:
				yield float(number)
				number = ''
			formula_copy = ''+ formula_string
			
			if s in OPERATORS or s in "()":
				yield s
		if number:
			yield float(number)

	def shunting_yard(parsed_formula):
		stack = []
		for token in parsed_formula:
			if token in OPERATORS:
				while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
					yield stack.pop()
				stack.append(token)
			elif token == ")":
				while stack:
					x = stack.pop()
					if x == "(":
						break
					yield x
			elif token == "(":
				stack.append(token)
			else:
				yield token
		while stack:
			yield stack.pop()

	def calc(polish):
		stack = []
		for token in polish:
			if token in OPERATORS:
				y, x = stack.pop(), stack.pop()
				stack.append(OPERATORS[token][1](x, y))
			else:
				stack.append(token)
		return stack[0]

	return calc(shunting_yard(parse(normalize(formula))))

