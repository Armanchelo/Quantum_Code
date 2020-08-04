from tkinter import *
from math import radians, cos, sin, pi
from random import randint
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-e', default = 1)
parser.add_argument('-r', default = False)
parser.add_argument('-c', default = '')
args = parser.parse_args()
random = args.r
escala = int(args.e)
if args.c == 'i': 
    coordenadas = [
        [50, 100, 50], [225, 100, 50],
        [225, 100, 100], [200, 100, 100],
        [200, 100, 150], [100, 100, 150],
        [100, 100, 225], [50, 100, 225]
    ]
    orden = [[8, 1, 2, 3, 4, 5, 6, 7, 8]]

elif args.c == 'i2':
    coordenadas = [
        [50, 100, 75], [150, 100, 75],
        [150, 225, 75], [50, 225, 75],
        [50, 100, 200], [150, 100, 200],
        [150, 175, 200], [50, 175, 200],
        [50, 225, 125], [150, 225, 175]
    ]
    orden = [
        [1, 2, 3, 4, 1], [2, 6], [1, 5], [3, 10], [4, 9],
        [6, 7], [10, 3], [5, 8], [9, 4], [6, 5], [7, 8], [9, 10]
    ]

if args.c == '':
    num = int(input('número: '))
    coordenadas = []
    orden = []
    for n in range(num):
        if random: coords = [randint(0, 300), randint(0, 300), randint(0, 300)]
        else:
            coord = input('coordenada: ')
            coord = coord.replace(' ', '')
            coords = coord.split(',')
            coords[0] = float(coords[0]) * escala
            coords[1] = float(coords[1]) * escala
            coords[2] = float(coords[2]) * escala
        coordenadas.append(coords)
    num = int(input('numero de ordenes: '))
    for n in range(num):
        o = input('orden: ')
        o = o.replace(' ', '')
        o = o.split(',')
        aux = []
        for e in o:
            aux.append(int(e))
        orden.append(aux)

tk = Tk()
tk.overrideredirect(True) 
width, height = tk.winfo_screenwidth(), tk.winfo_screenheight()
tk.geometry("%dx%d+0+0" % (width, height))
canvas = Canvas(tk, bg = 'black', width = width, height = height)
canvas.pack()

class Punto:
    def __init__(self, coords, pos, radio, index):
        self.coords = coords
        self.index = str(index)
        self.x = [float(coords[0]) * cos(pi + pi / 6), -float(coords[0]) * sin(pi + pi / 6)]
        self.y = [-float(coords[1]) * cos(pi + pi / 6), -float(coords[1]) * sin(pi + pi / 6)]
        self.z = [0, -float(coords[2])]
        self.pos = [300 + self.x[0] + self.y[0], 300 + self.x[1] + self.y[1] + self.z[1]]
        self.X = pos[0]
        self.Y = pos[1]
        self.radio = radio
        self.P = [self.X + self.x[0] + self.y[0], self.Y + self.x[1] + self.y[1] + self.z[1]]

    def dibujar(self):
        self.radio = radio
        X, Y = self.X, self.Y
        x, y, z = self.x, self.y, self.z
        color = 'grey'
        #xy
        canvas.create_line(X, Y, X + x[0], Y + x[1], fill = color)
        canvas.create_line(X + x[0], Y + x[1], X + x[0] + y[0], Y + x[1] + y[1], fill = color)
        canvas.create_line(X + x[0] + y[0], Y + x[1] + y[1], X + y[0], Y + y[1], fill = color)
        #yz
        canvas.create_line(X, Y, X + y[0], Y + y[1], fill = color)
        canvas.create_line(X + y[0], Y + y[1], X + y[0], Y + z[1] + y[1], fill = color)
        canvas.create_line(X + y[0], Y + y[1] + z[1], X, Y + z[1], fill = color)
        #zx
        canvas.create_line(X, Y, X + z[0], Y + z[1], fill = color)
        canvas.create_line(X + x[0], Y + x[1], X + x[0], Y + x[1] + z[1], fill = color)
        canvas.create_line(X + x[0], Y + x[1] + z[1], X, Y + z[1], fill = color)
        #lineas del punto
        canvas.create_line(X + x[0], Y + x[1] + z[1], X + x[0] + y[0], Y + x[1] + y[1] + z[1], fill = color)
        canvas.create_line(X + x[0] + y[0], Y + x[1] + y[1] + z[1], X + y[0], Y + y[1] + z[1], fill = color)
        canvas.create_line(X + x[0] + y[0], Y + x[1] + y[1] + z[1], X + x[0] + y[0], Y + x[1] + y[1], fill = color)
        #punto
        pradio = 5
        color = 'red'
        canvas.create_oval(X + x[0] + y[0] - pradio, Y + x[1] + y[1] + z[1] - pradio, X + x[0] + y[0] + pradio, Y + x[1] + y[1] + z[1] + pradio, fill = color, outline = color)
        self.P = [X + x[0] + y[0], Y + x[1] + y[1] + z[1]]
        canvas.create_text(self.P, text = self.index, font = 'Times 20', fill = 'white')

puntos = []
pos = [width / 4, height / 2]
radio = width / 4 - 5

canvas.create_line(width / 2, 0, width / 2, height, fill = 'red')

indice = 1
for coordenada in coordenadas:
    puntos.append(Punto(coordenada, pos, radio, indice))
    indice += 1

X,Y = pos[0], pos[1]
color = 'blue'
canvas.create_oval(X - radio, Y - radio, X + radio, Y + radio, outline = color)
canvas.create_line(X, Y, X, Y - radio, fill = color)
canvas.create_line(X, Y, X + (radio * cos(pi / 6)), Y + radio - (radio * sin(pi / 6)), fill = color)
canvas.create_line(X, Y, X - (radio * cos(pi / 6)), Y + radio - (radio * sin(pi / 6)), fill = color)

canvas.create_rectangle(.75 * width, height / 2, .75 * width - radio, height / 2 - radio, outline = 'cyan')
canvas.create_text(width / 2 + 40, height / 2 - radio + 30, text = 'PV', font = 'Times 30', fill = 'cyan')
canvas.create_rectangle(.75 * width, height / 2, .75 * width + radio, height / 2 - radio, outline = 'cyan')
canvas.create_text(width - 40, height / 2 - radio + 30, text = 'PLe', font = 'Times 30', fill = 'cyan')
canvas.create_rectangle(.75 * width, height / 2, .75 * width - radio, height / 2 + radio, outline = 'cyan')
canvas.create_text(width / 2 + 40, height / 2 + radio - 30, text = 'PHe', font = 'Times 30', fill = 'cyan')

for punto in puntos:
    vertical = [.75 * width - float(punto.coords[0]), height / 2 - float(punto.coords[2])]
    lateral = [.75 * width + float(punto.coords[1]), height / 2 - float(punto.coords[2])]
    horizontal = [.75 * width - float(punto.coords[0]), height / 2 + float(punto.coords[1])]
    canvas.create_line(vertical, lateral, fill = 'yellow')
    canvas.create_line(vertical, horizontal, fill = 'yellow')
    canvas.create_line(horizontal, .75 * width, horizontal[1], fill = 'yellow')
    canvas.create_line(lateral, lateral[0], height / 2, fill = 'yellow')
    canvas.create_line(lateral[0], height / 2, .75 * width, horizontal[1], fill = 'yellow')
    canvas.create_oval(vertical[0] - 5, vertical[1] - 5, vertical[0] + 5, vertical[1] + 5, fill = 'red')
    canvas.create_text(vertical, text = punto.index + "'", font = 'Times 20', fill = 'white')
    canvas.create_oval(lateral[0] - 5, lateral[1] - 5, lateral[0] + 5, lateral[1] + 5, fill = 'red')
    canvas.create_text(lateral, text = punto.index + "''e", font = 'Times 20', fill = 'white')
    canvas.create_oval(horizontal[0] - 5, horizontal[1] - 5, horizontal[0] + 5, horizontal[1] + 5, fill = 'red')
    canvas.create_text(horizontal, text = punto.index + "e", font = 'Times 20', fill = 'white')

for o in range(len(orden)):
    for n in range(len(orden[o]) - 1):
        canvas.create_line(puntos[orden[o][n] - 1].P, puntos[orden[o][n + 1] - 1].P, fill = '#00FF00', width = 3)

for punto in puntos:
    punto.dibujar()
tk.update()

tk.mainloop()