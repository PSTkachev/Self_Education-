g=int(input('чсл '))
if (g % 4 == 0) or ((g % 400 == 0) and (g % 100 !=0)):
    print('Високосный')
else:
    print('Обычный')
