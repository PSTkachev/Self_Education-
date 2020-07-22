"""Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки)
и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
В качестве ответа укажите вывод программы, а не саму программу.
Слова, написанные в разных регистрах, считаются одинаковыми."""

load_file = open("dataset_3363_3.txt", 'r') #открываем исходный файл
stroka = load_file.read().replace('\n', ' ').lower().split() #достаем все данные из исходника, убирая строки, пробелы, переводим в нижний регистр
load_file.close() #закрыли исходный файл
print(stroka)

dict = {} #создаем пустой словарь

for i in range(0,len(stroka)): #в диапазоне всего списка
    dict[stroka[i]] = stroka.count(stroka[i]) #добавляем в словарь i-е значение как ключ и считаем сколько раз оно встречается
print(dict)

sorted_by_value = sorted(dict.items(), key=lambda znach: znach[1]) #из словаря сделали кортеж и отсортировали по его значениям
sorted_by_value.reverse() #перевернули
print(sorted_by_value)
"""
dump_file = open("dataset_answer2.txt", "w")
for j in sorted_by_value:
    line = ' '.join(map(str, sorted_by_value)
    dump_file.write(line + '\n')
dump_file.close()"""

with open('dataset_answer2.txt', 'w') as dump_file:
    dump_file.write('\n'.join(' '.join(str(x) for x in tu) for tu in sorted_by_value)) #запись кортежа в файл

x = input('нажми что нибудь')
"""
#Без словаря, сразу читаем файл и сортируем список слов, чтобы потом первое найденное было лексиграфически впереди.
with open('dataset_3363_3.txt') as inf, open('MostPopularWord.txt','w') as ouf:
    maxc = 0
    s = inf.read().lower().strip().split()
    s.sort()
    for word in s:
        counter = s.count(word)
        if counter > maxc:
            maxc = counter
            result_word = word
    ouf.write(result_word +' ' + str(maxc))
"""
