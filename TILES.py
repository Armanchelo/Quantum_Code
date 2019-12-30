import tkinter as Tk
import mouse
import win32api

tk = Tk.Tk()
tk.overrideredirect(True)
# w, h = tk.winfo_screenwidth(), tk.winfo_screenheight()
w, h = 600, 600
tk.geometry("%dx%d+0+0" % (w, h))
canvas = Tk.Canvas(tk, bg = 'black', width = w, height = h)
canvas.pack()

rows, columns = 10, 10
width, height = w / columns, h / rows
available = ''

def init_game():
    game, temp = [], []
    for row in range(rows):
        for column in range(columns):
            current = (column + 1) + (row * columns)
            temp.append(current)
        game.append(temp)
        temp = []
    game[rows - 1][columns - 1] = available
    return game

board = init_game()

def draw_game():
    for row in range(rows):
        for column in range(columns):
            x, y = column * width, row * height
            offset = width / 2
            if board[row][column] is not available:
                canvas.create_rectangle(x, y, x + width, y + height, fill = 'white')
                canvas.create_text(x + offset, y + offset, text = board[row][column], font = 'Times {} italic bold'.format(round(width * .6)))
            else:
                canvas.create_rectangle(x, y, x + width, y + height, fill = 'black')

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
            break       

while True:
    draw_game()
    tk.update()
    next_move()

tk.mainloop()

