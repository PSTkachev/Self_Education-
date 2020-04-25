# вывод *
#i = 0 
#while i < 5: 
#    print('*') 
#    if i % 2 == 0: 
#       print('**') 
#    if i > 2: 
#        print('***') 
#    i = i + 1

# вывести сумму прежних чисел при вводе 0
#i = int(input()) 
#a=0
#while i != 0:
#    a+= i
#    i = int(input())
#print(a)

# поиск НОК
a = int(input())
b = int(input())
i = max(a,b)
while i % a != 0 or i % b != 0:
    i+=1
print(i)
"""
i = 0
while i <= 100:
    i=int(input ())
    if i < 10 :
        continue
    if i > 100 :
        break
    print(i)
"""      
