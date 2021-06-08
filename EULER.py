from math import pi, exp, sqrt
from tkinter import *
import mss
import mss.tools
from time import sleep

digits = 4
euler = lambda z: (1 / sqrt(2 * pi)) * exp(-.5 * z ** 2)
Z = lambda a: round((a[0] - a[1]) / a[2], ndigits = digits)
steps = 10000

def area_bajo_curva(a, b):
    deltax = (b - a) / steps
    area = 0
    for i in range(1, steps): area += deltax * euler(a + i * deltax)
    return round(area, ndigits=digits)

def graficar(a, b, name, index, color = '#00ae94', show = False, c = None, d = None):
    tk = Tk()
    tk.overrideredirect(True)
    width, height = tk.winfo_screenwidth(), tk.winfo_screenheight()
    canvas = Canvas(tk, bg = 'black', width = width, height = height)
    canvas.pack()

    izquierda = f'Probabilidad es: {area_bajo_curva(a, b) * 100}%'
    rng = f'{a}-{b}'
    area = f'{area_bajo_curva(-10, b)}-({area_bajo_curva(-10, a)}) = {area_bajo_curva(a, b)}'
    spacex = 60
    spacey = 30
    minx, maxx = -3, 3
    miny, maxy = -.5, .5
    deltax = (maxx - minx) / (width // spacex)
    deltay = (maxy - miny) / (height // spacey)
    for x in range(0, width, spacex):
        canvas.create_line(x, 0, x, height, fill = 'grey')
        if x != width // 2: canvas.create_text(x, height // 2 + 10, text = f'{round(minx + (x / spacex) * deltax, ndigits=3)}', font = 'Times 10 italic bold', fill = 'white')
        if show: tk.update()
    for y in range(0, height, spacey):
        canvas.create_line(0, height - y, width, height - y, fill = 'grey')
        if y != height // 2: canvas.create_text(width // 2 + 20, height - y - 5, text = f'{round(miny + (y / spacey) * deltay, ndigits=3)}', font = 'Times 10 italic bold', fill = 'white')
        if show: tk.update()
    canvas.create_line(width // 2, 0, width // 2, height, fill = 'white', width = 5)
    canvas.create_line(0, height // 2, width, height // 2, fill = 'white', width = 5)
    deltax = (maxx - minx) / width
    for x in range(width):
        canvas.create_line(x, height // 2 - euler(minx + x * deltax) * (spacey / deltay), x + 1, height // 2 - euler(minx + (x + 1) * deltax) * (spacey / deltay), fill = 'white', width = 5)
        if show: tk.update()
    z1 = (a / deltax)
    z2 = (b / deltax)
    for x in range(int(width / 2 + z1), int(width / 2 + z2)):
        canvas.create_line(x, height // 2, x, height // 2 - euler(minx + x * deltax) * (spacey / deltay) + 2, fill = color, width = 5)
        if show: tk.update()
    if c and d:
        z1 = (c / deltax)
        z2 = (d / deltax)
        for x in range(int(width / 2 + z1), int(width / 2 + z2)):
            canvas.create_line(x, height // 2, x, height // 2 - euler(minx + x * deltax) * (spacey / deltay) + 2, fill = color, width = 5)
            if show: tk.update()
        rng += f' y {c}-{d}'
        area = f'{area_bajo_curva(a, b)}+({area_bajo_curva(c, d)}) = {area_bajo_curva(a, b) + area_bajo_curva(c, d)}'
        izquierda = f'Probabilidad es: {(area_bajo_curva(a, b) + area_bajo_curva(c, d)) * 100}%'

    canvas.create_text(width * .75, height * .75 - 60, text = f'range = {rng}', font = 'Times 20 italic bold', fill = 'white')
    canvas.create_text(width * .75, height * .75 - 30, text = area, font = 'Times 20 italic bold', fill = 'white')
    canvas.create_text(width * .75, height * .75, text = izquierda, font = 'Times 20 italic bold', fill = 'white')
    canvas.create_text(width * .25, height * .25, text = f'grafica {name}', font = 'Times 20 italic bold', fill = 'white')

    tk.update()
    sleep(1)
    filedir = f'c:/users/usuario/desktop/graphs/{index}.jpg'
    print(filedir)
    with mss.mss() as sct:
        region = {'top': 0, 'left': 0, 'width': width, 'height': height}
        img = sct.grab(region)
        mss.tools.to_png(img.rgb, img.size, output=filedir)
    tk.destroy()
    tk.mainloop()

graficas12 = [
    [(1.57, 1.65, 0.65), (10, 0, 1), '1a'], #1a
    [(-10, 1.65, 0.65), (1.70, 1.65, 0.65), '1b'], #1b
    [(1.57, 1.65, 0.65), (1.70, 1.65, 0.65), '1c'], #1c
    [(2.9, 2.4, 0.8), (10, 0, 1), '2'], #2
    [(952, 950, 10), (957, 950, 10), '3'], #3
    [(-10, 0, 1), (38000, 35000, 3000), '4'], #4
    [(4.998, 5, 0.001), (5.002, 5, 0.001), '5a'], #5a
    [(-10, 0, 1), (4.998, 5, 0.001), '5b'], #5b
    [(5.002, 5, 0.001), (10, 0, 1), '5c'], #5c
    [(100, 128.45, 18.26), (10, 0, 1), '6a'], #6a
    [(150, 128.45, 18.26), (10, 0, 1), '6b'], #6b
    [(-10, 0, 1), (120, 128.45, 18.26), '6c'], #6c
    [(7000, 7000, 520), (7600, 7000, 520), '7a'], #7a
    [(6500, 7000, 520), (7600, 7000, 520), '7b'], #7b
    [(7600, 7000, 520), (10, 0, 1), '7c'], #7c
    [(225, 215, 18), (10, 0, 1), '8'], #8
    [(0.12, 0.13, 0.005), (0.14, 0.13, 0.005), '9'],#9
    [(3.47, 3.5, 0.02), (3.53, 3.5, 0.02), '10'], #10
    [(72, 78, 6), (10, 0, 1), '11a'], #11a
    [(85.68, 78, 6), (10, 0, 1), '11b'], #11b
    [(-10, 0, 1), (179.195, 175, 8), '12'], #12
    [(-10, 0, 1), (462.256, 385, 25), '13'], #13
    [(-10, 0, 1), (7.51, 6.2, 0.8), '14'], #14
    [(-10, 0, 1), (810.2, 759, 40), '15'], #15
    [(-10, 0, 1), (4.3, 3.8, 0.31), '16'], #16
    [(-10, 0, 1), (122.95, 116, 9), '17'], #17
    [(-10, 0, 1), (1017.95, 950, 100), '18'] #18
]

graficas11 = [
    [(-10, 0, 1), (0.47, 0, 1), 1],
    [(-1.13, 0, 1), (10, 0, 1), 2],
    [(0.54, 0, 1), (1.91, 0, 1), 3],
    [(0, 0, 1), (1.11, 0, 1), 4],
    [(-1.96, 0, 1), (0, 0, 1), 5],
    [(-1.23, 0, 1), (2.01, 0, 1), 6],
    [(-2.07, 0, 1), (-0.96, 0, 1), 7],
    [(1.26, 0, 1), (2, 0, 1), 8],
    [(-0.74, 0, 1), (10, 0, 1), 9],
    [(-10, 0, 1), (0.54, 0, 1), 10],
    [[(-10, 0, 1), (0.83, 0, 1)], [(1.98, 0, 1), (10, 0, 1)], 11],
    [(1.33, 0, 1), (10, 0, 1), 12],
    [[(-10, 0, 1), (-1.85, 0, 1)], [(1.66, 0, 1), (10, 0, 1)], 13],
    [(0.93, 0, 1), (1.7, 0, 1), 14],
    [(-10, 0, 1), (0.3, 0, 1), 15],
    [(-1.84, 0, 1), (10, 0, 1), 16],
    [(-1.03, 0, 1), (10, 0, 1), 17],
    [(0, 0, 1), (2, 0, 1), 18],
]

green = '#00ae94'
for index, grafica in enumerate(graficas12):
    a, b, name = grafica
    if len(a) == 2:
        print(a, len(a))
        c, d = a
        e, f = b
        graficar(Z(c), Z(d), name, index, green, show = False, c = Z(e), d = Z(f))
    else:
        graficar(Z(a), Z(b), name, index, green, show = False)

