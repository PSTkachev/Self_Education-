import turtle
a, b, i = 0, 1, 1
n = int(input("n=")) #14
avi = turtle.Pen()
while i <= n:
     result = b + a
     print(result)
     avi.forward(result)
     avi.left(90)
     a, b = b, result
     i += 1




