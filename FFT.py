from tkinter import *
from tkinter.filedialog import askopenfilename
from math import sin, cos, pi, atan2, radians, e
from random import random
from win32api import GetCursorPos
from keyboard import is_pressed as key

tk = Tk()
tk.overrideredirect(True)
canvas = Canvas(tk, bg = 'black', width = 600, height = 600)
canvas.pack()

time = 0

class Center:
    def __init__(self):
        self.pos = (0, 0)
    def traslate(self, x, y):
        self.pos = (x, y)
center = Center()

class vector:
    def __init__(self, x, y):
        self.pos = (x, y)
        self.x = x
        self.y = y
    
    def normalice(self):
        radius = (self.x ** 2 + self.y ** 2) ** .5
        self.x /= radius
        self.y /= radius
        self.pos = (self.x, self.y)

def ellipse(x, y, a, b = 0, fill = 'black'):
    centerx, centery = center.pos
    if b == 0: b = a
    canvas.create_oval(x - a + centerx, y - b + centery, x + a + centerx, y + b + centery, outline = 'white', fill = fill)

def line(ax, ay, bx, by):
    centerx, centery = center.pos
    canvas.create_line(ax + centerx, ay + centery, bx + centerx, by + centery, fill = 'white')

def traslate(x, y): center.traslate(x, y)

def point(x, y):
    ellipse(x, y, 1, fill = 'white')

def dft(x):
    N = len(x)
    X = [0 for n in range(N)]
    for k in range(N):
        print(k)
        re, im = 0, 0
        for n in range(N):
            phi = (2 * pi * k * n) / N
            re += x[n] * cos(phi)
            im -= x[n] * sin(phi)
        re = re / N
        im = im / N

        freq = k
        amp = (re ** 2 + im ** 2) ** .5
        phase = atan2(im, re)
        X[k] = {
            're': re,
            'im': im, 
            'freq': freq,
            'amp': amp,
            'phase': phase
        }

    return X

def epiCycles(x, y, rotation, fourier):
    for i in range(len(fourierY)):
        prevx, prevy = x, y
        freq = fourier[i]['freq']
        radius = fourier[i]['amp']
        phase = fourier[i]['phase']
        x += radius * cos(freq * time + phase + rotation)
        y += radius * sin(freq * time + phase + rotation)

        # ellipse(prevx, prevy, radius)
        # line(prevx, prevy, x, y)
    return vector(x, y)

path = []
speed = 5

def square(freq):
    x = [i - 100 for i in range(360)]
    y = []
    for i in range(360):
        sumy = 0
        for m in range(freq):
            n = m * 2 + 1
            rad = 150 * (4 / (n * pi))
            sumy += rad * sin(radians(i * n))
        y += [sumy]
    return x, y

def draw():
    x, y = [], []
    while not key('e'):
        if key(' '):
            X, Y = GetCursorPos()
            ellipse(X, Y, 1)
            x += [X - 300]
            y += [Y - 300]
        tk.update()
    return x, y

def triangle(freq):
    x = [i - 100 for i in range(360)]
    y = []
    for i in range(360):
        sumy = 0
        for m in range(freq):
            n = 2 * m + 1
            sign = (-1) ** (m + 1)
            den = sign * ((n * pi) ** 2)
            rad = 8 / den
            sumy += 150 * rad * sin(radians(i * n))
        y += [sumy]
    return x, y

def stickman():
    x, y = [], []
    for i in range(360):
        x += [25 * cos(radians(i + 90))]
        y += [25 * sin(radians(i + 90))]
    for i in range(25):
        x += [i]
        y += [25 + i]
    for i in range(25):
        x += [-i]
        y += [25 + i]
    for i in range(75):
        x += [0]
        y += [25 + i]
    for i in range(25):
        x += [i]
        y += [100 + i]
    for i in range(25):
        x += [-i]
        y += [100 + i]

    return x, y

# x, y = train()
Y = lambda t, a: (e ** -t) * sin(t) * (e ** (-a * t))
x = [n for n in range(-180, 360)]
y = [50 * Y(radians(n), -1) + 50 for n in x]
fourierY = dft(y)
fourierX = dft(x)
dt = 2 * pi / len(fourierY)

tk.update()
while True:
    # traslate(150, 300)
    canvas.delete(ALL)
    vx = epiCycles(300, 100, 0, fourierX)
    vy = epiCycles(100, 300, pi / 2, fourierY)
    v = vector(vx.x, vy.y)
    path.insert(0, v)
    # line(vx.x, vx.y, v.x, v.y)
    # line(vy.x, vy.y, v.x, v.y)
    for i in range(len(path)):
        try: line(path[i].x, path[i].y, path[i + 1].x, path[i + 1].y) 
        except IndexError: break

    tk.update()
    time += dt * speed
    
tk.mainloop()