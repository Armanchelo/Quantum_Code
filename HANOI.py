from tkinter import ALL, Canvas, Tk
from time import sleep
from random import choice

tk = Tk()
tk.overrideredirect(True)
width, height = 600, 600
canvas = Canvas(tk, bg = 'black', width = width, height = height)
canvas.pack()

disks = 3
diskWidth = (width / 3) / disks
diskHeight = diskWidth
disky = 500
delay = 1
a, b, c = 100, 300, 500
B, C = [], []
colors = [
    'red', 'white', 'yellow',
    'cyan', 'blue', 'purple'
]

canvas.create_rectangle(0, disky, width, disky + 10, fill = 'brown')
canvas.create_rectangle(a - (diskWidth / 2) + 2, disky - (diskHeight * (disks + 2)), a + (diskWidth / 2) - 2, disky, fill = 'green')
canvas.create_rectangle(b - (diskWidth / 2) + 2, disky - (diskHeight * (disks + 2)), b + (diskWidth / 2) - 2, disky, fill = 'green')
canvas.create_rectangle(c - (diskWidth / 2) + 2, disky - (diskHeight * (disks + 2)), c + (diskWidth / 2) - 2, disky, fill = 'green')

class Circle:
    def __init__(self, width, height, color = 'white'):
        self.width = width
        self.height = height
        self.circle = 0
        self.color = color

    def show(self, x, y):
        canvas.delete(self.circle)
        self.circle = canvas.create_rectangle(x - self.width / 2, y - self.height / 2, x + self.width / 2, y + self.height / 2, fill = self.color)
        self.circle
        tk.update()

A = [Circle(diskWidth * n, diskHeight, choice(colors)) for n in range(1, disks + 1)]
A.reverse()

def draw(A, B, C):
    for n in range(len(A) - 1, -1, -1):
        h = len(A) * diskHeight
        A[n].show(a, disky - (diskHeight * n) - (diskHeight / 2))
        tk.update
        sleep(delay)
    for n in range(len(B) - 1, -1, -1):
        h = len(B) * diskHeight
        B[n].show(b, disky - (diskHeight * n) - (diskHeight / 2))
        tk.update()
        sleep(delay)
    for n in range(len(C) - 1, -1, -1):
        h = len(C) * diskHeight
        C[n].show(c, disky - (diskHeight * n) - (diskHeight / 2))
        tk.update
        sleep(delay)

def move(n, start, end, aux):
    if n > 0:
        move(n - 1, start, aux, end)
        draw(A, B, C)
        end.append(start.pop())
        move(n - 1, aux, end, start)

move(disks, A, C, B)
draw(A, B, C)

tk.mainloop()