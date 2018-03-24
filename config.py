# -*- coding: utf-8 -*-
 
from enum import Enum

token = '414940346:AAFVfcpbR0kKFuQxNayhRckIlRGr0V_2DRE'


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
