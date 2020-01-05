from tkinter import Tk, Canvas, ALL
from math import cos, sin, radians, pi
from time import sleep

tk = Tk()
tk.overrideredirect(True)
width, height = 600, 600
canvas = Canvas(tk, bg = 'black', width = width, height = height)
canvas.pack()

nums = 500
radius = 300
points = []

canvas.create_oval(0, 0, radius * 2, radius * 2, outline = 'green')

for angle in range(1, nums + 1):
    pos = [cos((angle / nums) * 2 * pi) * radius + radius, sin((angle / nums) * 2 * pi) * radius + radius]
    finalPos = [cos(((angle + 1) / nums) * 2 * pi) * radius + radius, sin(((angle + 1) / nums) * 2 * pi) * radius + radius]
    points.append(pos)

for table in range(2, 100):
    for point in range(1, len(points)):
        finalPos = (point * table) % nums
        canvas.create_line(points[point - 1], points[finalPos - 1], fill = 'green', width = 1)
        tk.update()
    sleep(1)
    canvas.delete(ALL)

tk.mainloop()