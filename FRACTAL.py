from tkinter import *
from random import *

tk = Tk()
tk.overrideredirect(True)
w, h = tk.winfo_screenwidth(), tk.winfo_screenheight()
# w, h = 600, 600
tk.geometry("%dx%d+0+0" % (w, h))
canvas = Canvas(tk, bg = 'black', width = w, height = h)
canvas.pack()

colors = ['white', 'red', 'green', 'yellow', 'blue', 'pink', 'orange', 'cyan']

def draw_circle(x, y, r):
    if r > 1:
        canvas.create_oval(x - r, y - r, x + r, y + r, outline = choice(colors))
        draw_circle(x + r, y, r * .5)
        draw_circle(x - r, y, r * .5)
        draw_circle(x, y + r, r * .5)
        # draw_circle(x, y - r, r * .5)

draw_circle(w / 2, 0, 300)
tk.mainloop()