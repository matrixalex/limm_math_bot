# -*- coding: utf-8 -*-
 
from enum import Enum
from os import environ

token = environ.get('heroku_token')
wolfram_app_id = environ.get('client_id')

db_file = "database.vdb"

class States(Enum):
    """
    используем БД Vedis, в которой хранимые значения всегда строки,
    поэтому и тут будем использовать тоже строки (str)
    """
    S_START = "0"  # Вызван новый оператор
    S_ENTER_FIRST = "1"
    S_ENTER_SECOND = "2"
    S_ENTER_THIRD = "3"

url = 'https://api.telegram.org/bot'
'''base_url = 'https://api.telegram.org/bot' + token + '/'
data = {"url": ""}
requests.post(base_url + 'setWebhook', data=data)		   '''

offset = 0
