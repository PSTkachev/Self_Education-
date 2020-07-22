import json
from difflib import get_close_matches #близкие совпадения
data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data: #Проверяем написание с заглавной буквой
        return data[word.title()]
    elif word.lower() in data:
        return data[word.lower()] #Проверяем написание в нижем регистре
    elif word.upper() in data:
        return data[word.upper()] #Проверяем написание в верхнем регистре
    elif len(get_close_matches(word, data.keys())) > 0 :
        print("вы имелли ввиду слово %s ?" %get_close_matches(word, data.keys())[0]) #Вывод первого из близких совпадений
        decide = input("нажмите Y если это так, или что угодно если не так \n")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return ("Такого слова нет в словаре, может вы ввели его с ошибками?")
    else:
        print('Вы ввели слово которого нет в словаре')


word = input("Введите слово которое вы хотите найти \n")
output = translate(word)
if type(output) == list: #Делаем вывод без скобок списка []
    for item in output:
        print(item)
else:
    print(output)