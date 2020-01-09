from tkinter import Canvas, Tk, ALL
from math import cos, sin, pi, atan

tk = Tk()
tk.overrideredirect(True)
width, height = 600, 600
canvas = Canvas(tk, bg = 'black', width = width, height = height)
canvas.pack()
offsetx =  width / 2
offsety = height / 2

angle = 0
increment = .001

projection = [
    [1, 0, 0],
    [0, 1, 0]
]

radius = 75
strokeWeight = 10

points = [
    [[-radius], [-radius], [0]],
    [[radius], [-radius], [0]],
    [[radius], [radius], [0]],
    [[-radius], [radius], [0]],
    [[0], [0], [-radius * 3]]
]

def matMul(matrix, point):
    colsA = len(matrix[0])
    rowsA = len(matrix)
    colsB = len(point[0])
    rowsB = len(point)
    suma = 0
    result = []

    if rowsB != colsA:
        return 'colsA must match rowsB'

    for i in range(rowsA):
        for j in range(colsA):
            suma += matrix[i][j] * point[j][0]
        result.append([suma])
        suma = 0

    return result

def rotateX(angle, point):
    rotatex = [
        [1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)]
    ]
    rotatex = matMul(rotatex, point)
    return rotatex

def rotateY(angle, point):
    rotatey = [
        [cos(angle), 0, sin(angle)],
        [0, 1, 0],
        [-sin(angle), 0, cos(angle)]
    ]
    rotatey = matMul(rotatey, point)
    return rotatey

def rotateZ(angle, point):
    rotatez = [
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1]
    ]
    rotatez = matMul(rotatez, point)
    return rotatez

while True:
    draw = []
    canvas.delete(ALL)
    #puntos
    for p in range(len(points)):
        start = rotateX(angle, points[p])
        draw.append(start)
        canvas.create_oval(offsetx + start[0][0] - (strokeWeight / 2), offsety + start[1][0] - (strokeWeight / 2), offsetx + start[0][0] + (strokeWeight / 2), offsety + start[1][0] + (strokeWeight / 2), fill = 'white')

    #aristas
    canvas.create_line(draw[0][0][0] + offsetx, draw[0][1][0] + offsety, draw[1][0][0] + offsetx, draw[1][1][0] + offsety, fill = 'white', width = strokeWeight / 8)
    canvas.create_line(draw[1][0][0] + offsetx, draw[1][1][0] + offsety, draw[2][0][0] + offsetx, draw[2][1][0] + offsety, fill = 'white', width = strokeWeight / 8)
    canvas.create_line(draw[2][0][0] + offsetx, draw[2][1][0] + offsety, draw[3][0][0] + offsetx, draw[3][1][0] + offsety, fill = 'white', width = strokeWeight / 8)
    canvas.create_line(draw[3][0][0] + offsetx, draw[3][1][0] + offsety, draw[0][0][0] + offsetx, draw[0][1][0] + offsety, fill = 'white', width = strokeWeight / 8)
    canvas.create_line(draw[4][0][0] + offsetx, draw[4][1][0] + offsety, draw[0][0][0] + offsetx, draw[0][1][0] + offsety, fill = 'white', width = strokeWeight / 8)
    canvas.create_line(draw[4][0][0] + offsetx, draw[4][1][0] + offsety, draw[1][0][0] + offsetx, draw[1][1][0] + offsety, fill = 'white', width = strokeWeight / 8)
    canvas.create_line(draw[4][0][0] + offsetx, draw[4][1][0] + offsety, draw[2][0][0] + offsetx, draw[2][1][0] + offsety, fill = 'white', width = strokeWeight / 8)
    canvas.create_line(draw[4][0][0] + offsetx, draw[4][1][0] + offsety, draw[3][0][0] + offsetx, draw[3][1][0] + offsety, fill = 'white', width = strokeWeight / 8)
    tk.update()
    angle += increment

tk.mainloop()
