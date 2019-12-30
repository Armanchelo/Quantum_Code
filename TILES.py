import tkinter as Tk
import mouse
import win32api
import time
import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument('columns')
parser.add_argument('rows')
args = parser.parse_args()

tk = Tk.Tk()
tk.overrideredirect(True)
w, h = 600, 600
tk.geometry("%dx%d+0+0" % (w, h))
canvas = Tk.Canvas(tk, bg = 'black', width = w, height = h)
canvas.pack()

rows, columns, available = int(args.columns), int(args.rows), ''
width, height = w / max(rows, columns), w / max(rows, columns) 

def init_game():
    game, temp = [], []
    for row in range(rows):
        for column in range(columns):
            if row == 0 and column == 0: current = available
            else: current = (column) + (row * columns)
            temp.append(current)
        game.append(temp)
        temp = []
    return game

board = init_game()

def draw_game(color = 'white'):
    canvas.delete(Tk.ALL)
    for row in range(rows):
        for column in range(columns):
            x, y = column * width, row * height
            offset = width / 2
            if board[row][column] is not available:
                canvas.create_rectangle(x, y, x + width, y + height, fill = color)
                canvas.create_text(x + offset, y + offset, text = board[row][column], font = 'Times {} italic bold'.format(round(width * .4)))
            else: canvas.create_rectangle(x, y, x + width, y + height, fill = 'black')
    tk.update()

def next_move():
    while True:
        x, y = win32api.GetCursorPos()
        if mouse.is_pressed(button= 'left'):
            for row in range(rows):
                for column in range(columns):
                    north = board[row - 1][column] if row > 0 else 0
                    south = board[row + 1][column] if row < rows - 1 else 0
                    east = board[row][column + 1] if column < columns - 1 else 0
                    west = board[row][column - 1] if column > 0 else 0
                    if x > column * width and x < (column + 1) * width:
                        if y > row * height and y < (row + 1) * height:
                            if board[row][column] is not available:
                                if south is not 0 and south is available:
                                    board[row][column], board[row + 1][column] =  board[row + 1][column], board[row][column]
                                elif north is not 0 and north is available:
                                    board[row][column], board[row - 1][column] =  board[row - 1][column], board[row][column]
                                elif west is not 0 and west is available:
                                    board[row][column], board[row][column - 1] = board[row][column - 1], board[row][column]
                                elif east is not 0 and east is available:
                                    board[row][column], board[row][column + 1] = board[row][column + 1], board[row][column]
                            return ''       

def scramble(moves):
    offset = (width / columns) / 2
    for move in range(moves):
        column, row = random.randint(0, columns - 1), random.randint(0, rows - 1)
        north = board[row - 1][column] if row > 0 else 0
        south = board[row + 1][column] if row < rows - 1 else 0
        east = board[row][column + 1] if column < columns - 1 else 0
        west = board[row][column - 1] if column > 0 else 0
        if board[row][column] is not available:
            if south is not 0 and south is available:
                board[row][column], board[row + 1][column] =  board[row + 1][column], board[row][column]
            elif north is not 0 and north is available:
                board[row][column], board[row - 1][column] =  board[row - 1][column], board[row][column]
            elif west is not 0 and west is available:
                board[row][column], board[row][column - 1] = board[row][column - 1], board[row][column]
            elif east is not 0 and east is available:
                board[row][column], board[row][column + 1] = board[row][column + 1], board[row][column]

def check_solve():
    current = ''
    for row in range(rows):
        for column in range(columns):
            if board[row][column] != current: return False
            current = column + (row * columns) + 1
    return True

scramble(columns ** 5)
while True:
    draw_game()
    if check_solve():
        draw_game(color ='red')
        time.sleep(1)
        scramble(columns ** 5)
    next_move()
tk.mainloop()
