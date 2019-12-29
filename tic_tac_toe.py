from tkinter import *
from random import *
import math
import mouse
import keyboard
import win32api
import time

tk = Tk()
tk.overrideredirect(True)
#w, h = tk.winfo_screenwidth(), tk.winfo_screenheight()
w, h = 600, 600
tk.geometry("%dx%d+0+0" % (w, h))
canvas = Canvas(tk, bg = 'black', width = w, height = h)
canvas.pack()

rows, columns = 3, 3
available = ''

def make_game():
    game = []
    temp = []
    for row in range(rows):
        for column in range(columns):
            temp.append('')
        game.append(temp)
        temp = []
    return game

def draw_grid(color):
    height, width = h / rows, w / columns
    for row in range(rows):
        for column in range(columns):
            canvas.create_line(0, row * height, w, row * height, fill = color, width = 5)
            canvas.create_line(column * width, 0, column * width, h, fill = color, width = 5)

board = make_game()
players = ['X', 'O']

def next_move(player):
    height, width = h / rows, w / columns
    while True:
        x, y = win32api.GetCursorPos()
        if mouse.is_pressed(button = 'left'):
            for row in range(rows):
                for column in range(columns):
                    if x > column * width and x < (column + 1) * width:
                        if y > row * height and y < (row + 1) * height:
                            if board[row][column] is available:
                                actual_row, actual_column = row, column
                                board[actual_row][actual_column] = player
                                return ''

def draw_game():
    height, width = h / rows, w / columns
    offset = width / 2
    for row in range(rows):
        for column in range(columns):
            x, y = column * width, row * height
            canvas.create_text(x + offset, y + offset, text = board[row][column], font = 'Times {} italic bold'.format(round(width * .6)), fill = 'white')

def IA(player):
    while True:
        row, column = randint(0, rows - 1), randint(0, columns - 1)
        if board[row][column] is available: 
            board[row][column] = player
            break

def check_win(player):
    horizontal, vertical, diagonal1, diagonal2 = 0, 0, 0, 0
    for row in range(rows):
        for column in range(columns):
            if board[row][column] == player: horizontal += 1
            if board[column][row] == player: vertical += 1
        if board[row][row] == player: diagonal1 += 1
        if board[row][rows - row - 1] == player: diagonal2 += 1
        if horizontal == columns: return player
        else: horizontal = 0
        if vertical == rows: return player
        else: vertical = 0
    if diagonal1 == rows: return player
    else: diagonal1 = 0
    if diagonal2 == rows: return player
    else: diagonal2 = 0
    for row in range(rows):
        for column in range(columns):
            if board[row][column] is available: return False
    return 'tie'
    
draw_grid('white')   
tk.update()         
for rounds in range(9):
    currentPlayer = rounds % 2
    if currentPlayer == 0: next_move(players[currentPlayer])
    else: IA(players[currentPlayer])
    draw_game()
    if check_win(players[currentPlayer]) != False:
        print(check_win(players[currentPlayer]))
        break
    tk.update()

tk.mainloop()
