import random
num = random.randint(1, 100)
"""
#ищем ручками
while True:
    print('Угадайте число от 1 до 100')
    guess = input()
    i = int(guess)
    if i == num:
        print('Правильно!')
        input('Press ENTER to exit')
        break
    elif i < num:
        print('Загаданное число больше')
    elif i > num:
        print('Загаданное число меньше')
"""


#реализуем поиск ответа методом половинчатого деления
a = 1
b = 100
x = (b - a + 1) / 2

while x != num:
    if num < x:
        print('Загаданное число меньше чем', x)
        b = x
        x = round(((b - a) / 2) + a)
        print(x)

    elif num > x:
        print('Загаданное число больше чем', x)
        a = x
        x = round((b + a ) / 2)
        print(x)

if num == x:
    print('Правильно!', x)
