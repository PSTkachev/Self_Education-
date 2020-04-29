#счастливый билет, три варианта решения
"""
a = input()
b = str(a)
x = int(b[0]) + int(b[1]) + int(b[2])
y = int(b[3]) + int(b[4]) + int(b[5])
if x == y :
    print("Счастливый")
else :
    print("Обычный")
"""
"""
list = [5, 1, 3, 1, 0, 8]
raz = sum(list[0:3])
dva = sum(list[3:6])
print (raz, dva)
if raz==dva:
    print("lucky ticket")
else:
    print("next time")
"""

code=int(input()) 
a=code//100000 
b=code//10000%10 
c=code//1000%10 
d=code//100%10 
e=code//10%10 
f=code%10 
if a+b+c==d+e+f: 
    print('Счастливый') 
else: 
    print('Обычный')
