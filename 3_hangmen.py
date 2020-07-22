import random
def hangman():
    word = random.choice(["Dwalin", "Balin", "Kili", "Fili", "Dori", "Nori", "Ori", "Oin", "Gloin", "Bifur", "Bofur", "Bombur", "Thorin", "Bilbo", "Gandalf"])
    validLetters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    turns = 9
    guessmade = ''

    while len(word) > 0: #хех
        main = ""
        #missed = 0

        for letter in word: #цикл который преващает слово в подеркнутые символы или открывает буквы
            if letter in guessmade: #если буквы в слове и введенные буквы совпали то открываем их
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("Ты победил")
            break

        print("Введите букву:\n", main)
        guess = input()

        if (guess or guess.upper()) in validLetters:
            guessmade = guessmade + guess + guess.upper()  #записали сюда введенные буквы
        else:
            print("Введите корректную букву abcdefghijklmnopqrstuvwxyz \n")
            guess = input() #ввод буквы, повторный (слабое место)
        if (guess or guess.upper()) not in word: #если не угадана буква
            turns = turns - 1
            if turns == 8:
                print("осталось 8 попыток")

                print("     O      ")
            if turns == 7:
                print("осталось 7 попыток")

                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("осталось 6 попыток")

                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("осталось 5 попыток")

                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("осталось 4 попытки")

                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("осталось 3 попытки")

                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("осталось 2 попытки")

                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("осталась 1 попытка")
                print("Последний шанс")

                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("Ты проиграл")

                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break



name = input("Введите ваше имя\n")
print ("Добро пожаловать", name)
print("-------------------")
print("Попробуй угадать имя гнома за 9 попыток") #определенно стоит сделать меньше попыток
hangman()
print()