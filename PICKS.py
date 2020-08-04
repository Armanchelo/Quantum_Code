from tkinter import *
tk = Tk()
tk.overrideredirect(True)
canvas = Canvas(tk, bg = 'black', width = 600, height = 600)
canvas.pack()

class Toothpick:
    def __init__(self, x, y, dir = 1):
        size = 10
        self.dir = dir
        if dir == 1:
            self.ax = x - size
            self.bx = x + size
            self.ay, self.by = y, y
        elif dir == -1:
            self.ay = y - size
            self.by = y + size
            self.ax, self.bx = x, x
        self.A = (self.ax, self.ay)
        self.B = (self.bx, self.by)

    def checkEnds(self, toothpicks):
        A, B = True, True
        for toothpick in toothpicks:
            if self != toothpick:
                if self.A == toothpick.B and A == True: A = False
                if self.B == toothpick.A and B == True: B = False
        return [A, B]

toothpicks = [Toothpick(300, 300, dir = -1)]

while True:
    size = len(toothpicks)
    A, B = 0, 0
    for t in range(size):
        toothpick = toothpicks[t]
        ends = toothpick.checkEnds(toothpicks)
        if ends[0]: toothpicks += [Toothpick(toothpick.ax, toothpick.ay, dir = -toothpick.dir)]
        if ends[1]: toothpicks += [Toothpick(toothpick.bx, toothpick.by, dir = -toothpick.dir)]
        canvas.create_line(toothpick.A, toothpick.B, fill = 'white')
    tk.update()
    toothpicks = toothpicks[size:]

tk.mainloop()