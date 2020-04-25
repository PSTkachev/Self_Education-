#a = [int(i) for i in input().split()]
#print(len(a))
#s = sum(a)
#print(s)

#сумма соседних чисел
#a = [int(i) for i in input().split()]
#b = []
#if len(a) == 1:
#    print(a[0])
#else:
#    for i in range(len(a)-1):
#        b.append(a[i-1]+a[i+1])
#    b.append(a[-2] + a[0])
#print(*b)

#убирает повторы
#x =[4, 8, 0, 3, 4, 2, 0, 3]
#x.sort()
#r = [x[0]]
#i = 1
#j = 0
#while i < len(x):
#    if r[j] != x[i]:
#        r.append(x[i])
#        j += 1
#    i += 1
#print (r)

#повторяется столько раз, чему равно
a = int(input())
x = []
i = 1
while len(x) < a:
    x += [i] *i
    i += 1
print(*x[:a])



            
