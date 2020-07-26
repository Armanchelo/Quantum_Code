from tkinter import * 
from time import sleep

tk = Tk()
tk.overrideredirect(True)
canvas = Canvas(tk, bg = 'black', width = 600, height = 600)
canvas.pack()

def create_circle(x, y, r):
    if r > .1:
        r = int(round(r))
        canvas.create_oval(x - r, y - r, x + r, y + r, outline = 'white')
        tk.update()
        create_circle(x - r, y, r / 2)
        create_circle(x + r, y, r / 2)
        create_circle(x, y - r, r / 2)
        # sleep(.01)

create_circle(300, 600, 300)
tk.mainloop()