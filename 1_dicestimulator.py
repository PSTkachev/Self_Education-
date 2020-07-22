import random
print("Симулятор игровых костей")
x = "y"

while x == "y":
    number = random.randint(1,6)

    if number == 1:
        print("----------")
        print("|        |")
        print("|    O   |")
        print("|        |")
        print("----------")
    if number == 2:
        print("----------")
        print("|        |")
        print("| O    O |")
        print("|        |")
        print("----------")
    if number == 3:
        print("----------")
        print("|    O   |")
        print("|    O   |")
        print("|    O   |")
        print("----------")
    if number == 4:
        print("----------")
        print("| O    O |")
        print("|        |")
        print("| O    O |")
        print("----------")
    if number == 5:
        print("----------")
        print("| O    O |")
        print("|    O   |")
        print("| O    O |")
        print("----------")
    if number == 6:
        print("----------")
        print("| O    O |")
        print("| O    O |")
        print("| O    O |")
        print("----------")

    number2 = random.randint(1,6)

    if number2 == 1:
        print("----------")
        print("|        |")
        print("|    O   |")
        print("|        |")
        print("----------")
    if number2 == 2:
        print("----------")
        print("|        |")
        print("| O    O |")
        print("|        |")
        print("----------")
    if number2 == 3:
        print("----------")
        print("|    O   |")
        print("|    O   |")
        print("|    O   |")
        print("----------")
    if number2 == 4:
        print("----------")
        print("| O    O |")
        print("|        |")
        print("| O    O |")
        print("----------")
    if number2 == 5:
        print("----------")
        print("| O    O |")
        print("|    O   |")
        print("| O    O |")
        print("----------")
    if number2 == 6:
        print("----------")
        print("| O    O |")
        print("| O    O |")
        print("| O    O |")
        print("----------")

        
    x = input("Press y to roll again \n")
    
