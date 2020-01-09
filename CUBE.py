from tkinter import Canvas, Tk, ALL
from MATMUL import matMul, projection, rotateX, rotateY, rotateZ

tk = Tk()
tk.overrideredirect(True)
width, height = 600, 600
canvas = Canvas(tk, bg = 'black', width = width, height = height)
canvas.pack()
offsetx =  width / 2
offsety = height / 2

angle = 0
increment = .001

radius = 100
strokeWeight = 10

points = [
    [[-radius], [-radius], [radius]],
    [[radius], [-radius], [radius]],
    [[radius], [radius], [radius]],
    [[-radius], [radius], [radius]],
    [[-radius], [-radius], [-radius]],
    [[radius], [-radius], [-radius]],
    [[radius], [radius], [-radius]],
    [[-radius], [radius], [-radius]]
]

while True:
    draw = []
    canvas.delete(ALL)
    #puntos
    for p in range(len(points)):
        if p < 4: color = 'red'
        else: color = 'green'
        # start = rotateY(pi / 3, points[p])
        start = rotateX(angle, points[p])
        start = matMul(projection, start)
        start[0][0] += offsetx
        start[1][0] += offsety
        draw.append(start)
        canvas.create_oval(start[0][0] - (strokeWeight / 2), start[1][0] - (strokeWeight / 2), start[0][0] + (strokeWeight / 2), start[1][0] + (strokeWeight / 2), fill = color)

    #aristas
    for i in range(4):
        canvas.create_line(draw[i], draw[(i + 1) % 4], fill = 'white', width = strokeWeight / 8)
        canvas.create_line(draw[i + 4], draw[((i + 1) % 4) + 4], fill = 'white', width = strokeWeight / 8)
        canvas.create_line(draw[i], draw[i + 4], fill = 'white', width = strokeWeight / 8)
    tk.update()
    angle += increment

tk.mainloop()
