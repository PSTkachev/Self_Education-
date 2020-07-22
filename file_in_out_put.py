"""На прошлой неделе мы сжимали строки, используя кодирование повторов.
Теперь нашей задачей будет восстановление исходной строки обратно.
Напишите программу, которая считывает из файла строку, соответствующую тексту,
сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
В исходном тексте не встречаются цифры, так что код однозначно интерпретируем."""

load_file = open('dataset_3363_2.txt', 'r')
stroka = load_file.readline().strip()
load_file.close()
print(stroka)

l = len(stroka)
integ = []
strin = []
result = []
i = 0

while i < l:
    s_int = ''
    a = stroka[i]
    if a.isalpha():
        strin.append(a)
    while '0' <= a <= '9':
        s_int += a
        i += 1
        if i < l:
            a = stroka[i]
            if a.isalpha():
                strin.append(a)
        else:
            break
    i += 1
    if s_int != '':
        integ.append(int(s_int))

for i in range(0,len(strin)):
    result.append(strin[i]*integ[i])
result_result =''.join(result)

dump_file = open("dataset_answer.txt", "w")
dump_file.write(result_result)
dump_file.close()

print(integ)
print(strin)
print(result_result)

"""
#решение здорового человека
with open('dataset_3363_2.txt', 'r') as f:
    s = f.readline().strip()
i = 0
while i < len(s):
    j = i + 1
    while j < len(s) and s[j].isdigit():
        j += 1
    print(s[i] * int(s[i+1:j]), end='')
    i = j
"""
"""
Первый символ - гарантированно буква.
Перебираем все последующие, пока они цифровые или пока не достигнут конец строки.
После внутреннего цикла j либо указывает на следующую букву, либо на конец строки. В обоих случаях между s[i] и s[j] - цифры, составляющие нужное нам число повторов символа s[i].
Печатаем символ нужное число раз, присваиваем i индекс следующей буквы для новой итерации цикла.
"""