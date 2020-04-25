#перемножение строк и столбцов, своеобразная матрица
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range (a, b+1):
    for j in range (c, d+1):
        print(i * j, end="\t")
    print(i, "\n")
"""
#перемножение c d, сначала на а, потом на b
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for j in range(a, b + 1): # здесь выводим значение из диапазона 
    print (j, '\t', end = '') 
    for i in range(c, d + 1): # здесь считаем значения для каждой комбинации 
        print( i * j, '\t', end = '')
"""   
#среднеарифметическое каждого третьего числа (хз что это)
""" 
a, b = (int(i) for i in input().split())
s = 0
k = 0
while a % 3 != 0:
    a += 1
for i in range(a, b+1, 3):
    s += i
    k += 1
print(s/k)
"""     
# сортировка по соседям
"""
a = [5,2,7,4,0,9,8,6] 
n = 1 
while n < len(a):
    for i in range (len(a)-n):
        if a[i] > a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
        n += 1
print(a)
"""
