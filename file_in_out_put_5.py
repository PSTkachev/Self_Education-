'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".
Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
'''

import requests

download_link = 'https://stepic.org/media/attachments/course67/3.6.3/'
filename = '699991.txt'
zapros = requests.get(download_link+filename)

while not zapros.text.startswith("We"):
    zapros = requests.get(download_link + zapros.text)
    print(zapros.text)
print(zapros.text)

'''
import requests
url = 'https://stepic.org/media/attachments/course67/3.6.3/'
name = '699991.txt'
while name[:2] != 'We':
    name = requests.get(url + name).text
print(name)
'''