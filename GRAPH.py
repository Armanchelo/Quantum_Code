from math import sin, pi, tan, cos, log
from tkinter import *

tk = Tk()
width, height = tk.winfo_screenwidth(), tk.winfo_screenheight()
tk.overrideredirect(True)
canvas = Canvas(tk, bg = 'black', width = width, height = height)
canvas.pack()

def dibujar_cuadricula(minx, maxx, miny, maxy, text_size = 15, square = False, text = True):
    spacex = width // (maxx - minx + 1)
    spacey = height // (maxy - miny + 1)
    zero_level = height + miny * spacey - .5 * spacey
    zero_width = abs(minx) * spacex + .5 * spacex
    if square:
        spacex = min(spacex, spacey)
        spacey = spacex
    for x in range(minx, maxx + 1):
        canvas.create_line(x * spacex + zero_width, zero_level - spacey * maxy - spacey, x * spacex + zero_width, zero_level - spacey * miny + spacey, fill = 'grey')
        if x != 0 and text: canvas.create_text(x * spacex + zero_width, zero_level + 15, text = f'{x}', font = f'Times {text_size} bold', fill = 'white')
        tk.update()
    for y in range(miny, maxy + 1):
        canvas.create_line(spacex * minx + zero_width - spacex, zero_level - y * spacey, spacex * maxx + zero_width + spacex, zero_level - y * spacey, fill = 'grey')
        if y != 0 and text: canvas.create_text(zero_width - 15, zero_level - y * spacey, text = f'{y}', font = f'Times {text_size} bold', fill = 'white')
        tk.update()
    
    canvas.create_line(spacex * minx + zero_width - spacex, zero_level, spacex * maxx + zero_width + spacex, zero_level, fill = 'white', width = 5)
    canvas.create_line(zero_width, zero_level - spacey * maxy - spacey, zero_width, zero_level - spacey * miny + spacey, fill = 'white', width = 5)
        

def graficar_funcion(function, minx, maxx, miny, maxy, color = '#3cfac7', thickness = 2, square = False):
    spacex = width // (maxx - minx + 1)
    spacey = height // (maxy - miny + 1)
    zero_level = height + miny * spacey - .5 * spacey
    zero_width = abs(minx) * spacex + .5 * spacex
    deltax = (maxx - minx + 1) / width
    if square:
        spacex = min(spacex, spacey)
        spacey = spacex
    for x in range(spacex * minx, spacex * maxx + spacex):
        try:
            x1, y1 = x + zero_width, zero_level - spacey * function(x * deltax)
            x2, y2 = (x + 1) + zero_width, zero_level - spacey * function((x + 1) * deltax)
            canvas.create_line(x1, y1, x2, y2, fill = color, width = thickness)
            tk.update()
        except: pass

def integral_ab(function, a, b, minx, maxx, miny, maxy, color = '#3cfac7', thickness = 5, square = False):
    spacex = width // (maxx - minx + 1)
    spacey = height // (maxy - miny + 1)
    zero_level = height + miny * spacey - .5 * spacey
    zero_width = abs(minx) * spacex + .5 * spacex
    if square:
        spacex = min(spacex, spacey)
        spacey = spacex
    deltax = (maxx - minx + 1) / width
    x1 = int(a / deltax) if abs(a / deltax) < abs(spacex * minx) else int(spacex * minx)
    x2 = int(b / deltax) if abs(b / deltax) < abs(spacex * maxx) else int(spacex * maxx)
    for x in range(x1, x2):
        try:
            y = spacey * function(x * deltax)
            canvas.create_line(x + zero_width, zero_level, x + zero_width, zero_level - y, fill = color, width = 1)
            tk.update()
        except: pass


y = lambda x: 100 / x
minxx, maxx, miny, maxy = -100, 0, -100, 0
a, b = -100, 100
square = False

dibujar_cuadricula(minxx, maxx, miny, maxy, square=square, text = True)
graficar_funcion(y, minxx, maxx, miny, maxy, square=square)
integral_ab(y, a, b, minxx, maxx, miny, maxy, square=square)

tk.update()
tk.mainloop()