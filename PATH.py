import numpy as np
from PIL import Image
from time import sleep

class Node:
    def __init__(self, pos, parent, g):
        self.pos = pos
        self.parent = parent
        self.g = g

class Map:
    def __init__(self, mapa):
        self.mapa = mapa
        self.x, self.y = len(self.mapa[0]), len(self.mapa)
        self.size = (self.x, self.y)
        self.start = Node(self.search(2), Node(self.search(2), None, 0), 0)
        self.end = self.search(3)

    def search(self, X):
        for y in range(self.y):
            for x in range(self.x):
                if self.mapa[y, x] == X:
                    return (y, x)
        return None

def create_map(path):
    im = Image.open(path)  
    pixels = im.load()
    width, height = im.size
    maze = []
    for y in range(height):
        aux = []
        for x in range(width):
            r, g, b = pixels[x, y][0:3]
            if r > 127: r = 255
            else: r = 0
            if g > 127: g = 255
            else: g = 0
            if b > 127: b = 255
            else: b = 0
            if (r, g, b) == (0, 0, 0): aux.append(1)
            elif (r, g, b) == (255, 255, 255): aux.append(0)
            elif (r, g, b) == (255, 0, 0): aux.append(3)
            elif (r, g, b) == (0, 0, 255): aux.append(2)
        maze.append(aux)
    return np.array(maze)

def find_neighbours(node, mapa, diagonal = False):
    neighbours = []
    y, x = node.pos
    directions = [
        (y, x - 1),
        (y, x + 1),
        (y - 1, x),
        (y + 1, x)
    ]
    for direction in directions:
        if mapa.mapa[direction] == 0 or mapa.mapa[direction] == 3:
            neighbour = Node(direction, node, node.g + 1)
            neighbours.append(neighbour)
            if mapa.mapa[direction] != 3:
                mapa.mapa[direction] = 4
    return neighbours

def find(path, show = False):
    mapa = Map(create_map(path))
    if show == True:
        from tkinter import Tk, Canvas
        tk = Tk()
        tk.overrideredirect(True)
        width, height = min(600 / mapa.x, 600 / mapa.y), min(600 / mapa.x, 600 / mapa.y)
        canvas = Canvas(tk, bg = 'black', width = mapa.x * width, height = mapa.y * height)
        canvas.pack()
    parents = [mapa.start]
    childs = []
    path = []
    while True:
        if len(parents) == 0: return None, None
        else:
            for p in range(len(parents)):
                parent = parents.pop(0)
                if show == True:
                    y, x = parent.pos
                    canvas.create_rectangle(x * width, y * height, (x + 1) * width, (y + 1) * height, fill = 'white', outline = 'white')
                    tk.update()
                if parent.pos == mapa.end: 
                    node = parent
                    for g in range(parent.g):
                        path.append(node.pos)
                        node = node.parent
                    path.reverse()
                    return mapa, path
                childs += find_neighbours(parent, mapa)
        parents, childs = childs, parents
    if show == True:
        tk.mainloop()

mapa, path = find('C:\\Users\\Usuario\\Python\\Maze8.png', show = True)
if path != None:
    x, y = mapa.size
    width, height = min(600 / x, 600 / y), min(600 / x, 600 / y)
    from tkinter import *
    tk = Tk()
    tk.overrideredirect(True)
    canvas = Canvas(tk, bg = 'grey', width = x * width, height = y * height)
    canvas.pack()

    x, y = mapa.size
    for Y in range(y):
        for X in range(x):
            if mapa.mapa[Y, X] == 1: canvas.create_rectangle(X * width, Y * height, (X + 1) * width, (Y + 1) * height, fill = 'black', outline = 'black')
            elif mapa.mapa[Y, X] == 2: canvas.create_rectangle(X * width, Y * height, (X + 1) * width, (Y + 1) * height, fill = 'cyan', outline = 'cyan')
            elif mapa.mapa[Y, X] == 3: canvas.create_rectangle(X * width, Y * height, (X + 1) * width, (Y + 1) * height, fill = 'orange', outline = 'orange')
        tk.update()

    for p in path:
        y, x = p
        canvas.create_rectangle(x * width, y * height, (x + 1) * width, (y + 1) * height, fill = 'cyan', outline = 'cyan')
        tk.update()
    tk.mainloop()
else: print('no hay solucion')