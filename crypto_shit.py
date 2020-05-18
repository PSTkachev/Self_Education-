#l ='этот если способ вы плохо это подходит читаете для что-то шифрования пошло важных не сообщений так'.split()
l = input().split()
for i in range(0, len(l), 2):
    print(l[i], end=' ')
for i in range(-1, len(l), 2):
    print(l[i], end=' ')
input('Press ENTER to exit')
