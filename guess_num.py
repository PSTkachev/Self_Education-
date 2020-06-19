import random
num = random.randint(1, 100)
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
