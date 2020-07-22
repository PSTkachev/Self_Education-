"""
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.
На вход программе первой строкой передаётся количество dd известных нам слов,
после чего на dd строках указываются эти слова. 
Затем передаётся количество ll строк текста для проверки,
после чего ll строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:
4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic

Sample Output:
stepic
champignons
the"""
def merge_check_list(lstlst): #преобразуем многомерный список в одномерный
    all=[]
    for lst in lstlst:
      all.extend(lst) # .extend как  .append только для нескольких объектов
    return all

n = int(input('введите количество слов в словаре')) #уберите то что в скобках
dict_list = [input('words: ').lower().split() for x in range(n)] #добавляем словарь, и переводим все слова в нижний регистр
m = int(input('введите количество предложений для проверки')) #уберите то что в скобках
check_list = [input('words: ').lower().split(' ') for x in range(m)] # вводим проверяемый текст,  и переводим все слова в нижний регистр
dict_list_2 = merge_check_list(dict_list) # преобразуем многомерный список в одномерный
check_list_2 = merge_check_list(check_list) #преобразуем многомерный список в одномерный
print(dict_list_2) #удоли
print(check_list_2) #удоли
mistaken_words = []
for words in check_list_2: #сравниваем два списка, если слово не совпадает со словарем, то заносим его в ошибки
    if not words in dict_list_2:
        mistaken_words.append(words)
print(mistaken_words) #удоли
print('\n'.list(set(mistaken_words))) # set что бы убрать повторения получается что на вывод идет список list

"""
# формируем множество известных слов на основании построчного ввода
dic = {input().lower() for i in range(int(input()))}
# заводим пустое множество для приема текста
wrd = set()
# т.к. текст построчно подается, а также в каждой строке несколько слов,
# то каждую строку превращаем во множество и добавляем в единое множество wrd
for _ in range(int(input())):
    wrd |= {i.lower() for i in input().split()}
# на вывод отправляем результат вычитания словарного множества dic
# из текстового множества wrd; впереди ставим *, чтобы раскрыть поэлементно
print(*(wrd-dic), sep="\n")
#Основа работы кода - свойство множеств хранить только уникальные значения.
#wrd |= {...} отвечает за добавление множества {...} в единое wrd (аналог метода update)
#Обращаем внимание на звездочку *, которая вытаскивает элементы на вывод, вместо того, чтобы печатать в виде множества
"""
"""
count_dict = int(input())
dict = []
check_words = []
result = []
#заполняем словарь
for i in range(count_dict):
  dict.append(input().lower())
  
count_lines = int(input())
#заполняем список проверяемых слов
for i in range(count_lines):
  check_words += input().lower().strip().split(' ')

#выбираем слова которые не проходят проверку
for i in check_words:
  if i not in dict and i not in result:
    result.append(i)

#печатаем
for i in result:
  print(i)
"""