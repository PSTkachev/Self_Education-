from tkinter import *
import random

def hello():
    canvas.delete("all") #очистить холст
    print(random_rectangle(400, 400, 'green'), random_rectangle(400, 400, 'red'),
          random_rectangle(400, 400, 'blue'), random_rectangle(400, 400, 'orange'),
          random_rectangle(400, 400, 'yellow'), random_rectangle(400, 400, 'pink'),
          random_rectangle(400, 400, 'purple'), random_rectangle(400, 400, 'violet'),
          random_rectangle(400, 400, 'magenta'), random_rectangle(400, 400, 'cyan'))
    
    
def random_rectangle(width, height, fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = random.randrange(x1 + random.randrange(width))
    y2 = random.randrange(y1 + random.randrange(height))
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)
    
tk = Tk()
btn = Button(tk, text="нажми меня", command=hello)
btn.pack()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()



#вывод текста
#canvas.create_text(150, 100, text='Был один человек из Тулузы,')
#canvas.create_text(130, 120, text='Что сидел на огромном арбузе.', fill='red')

#рисуем круги
#canvas.create_arc(10, 10, 200, 80, extent=45, style=ARC)
#canvas.create_arc(10, 80, 200, 160, extent=90, style=ARC)
#canvas.create_arc(10, 160, 200, 240, extent=135, style=ARC)
#canvas.create_arc(10, 240, 200, 320, extent=180, style=ARC)
#canvas.create_arc(10, 320, 200, 400, extent=359, style=ARC)

#canvas.create_line(0, 0, 500, 500)
#canvas.create_rectangle(10, 10, 300, 50)

