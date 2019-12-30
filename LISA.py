from tkinter import*
import math
import time
angulo = 0
ancho_de_linea = 1
tamaño_de_figura = 200
velocidadx = int(input())
velocidady = int(input())
tk = Tk()
tk.overrideredirect(True)
canvas = Canvas(tk, bg = "black", width = 600, height = 600)
canvas.pack()
for x in range(1, velocidadx + 1):
    for y in range(1, velocidady + 1):
        canvas.delete(ALL)
        canvas.create_text(50, 50, text = x, fill = "white")
        canvas.create_text(50, 60, text = y, fill = "white")
        for g in range(0, 361):
            xp1 = math.cos(math.radians(g * x) - (math.pi / 2)) * tamaño_de_figura
            yp1 = math.sin(math.radians(g * y) - (math.pi / 2)) * tamaño_de_figura
            xp2 = math.cos(math.radians((g + 1) * x) - (math.pi / 2)) * tamaño_de_figura
            yp2 = math.sin(math.radians((g + 1) * y) - (math.pi / 2)) * tamaño_de_figura
            canvas.create_line(xp1 + 300, yp1 + 300, xp2 + 300, yp2 + 300, width = ancho_de_linea, fill = 'white')
            tk.update()
        time.sleep(1)
tk.mainloop()




