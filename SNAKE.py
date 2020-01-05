from tkinter import ALL, Canvas, Tk
from keyboard import is_pressed, KEY_DOWN, KEY_UP
from random import randint
from time import sleep

tk = Tk()
tk.overrideredirect(True)
# width, height = tk.winfo_screenwidth(), tk.winfo_screenheight()
width, height = 600, 600
canvas = Canvas(tk, bg = 'black', width = width, height = height)
canvas.pack()

KEY_LEFT = 'left arrow'
KEY_RIGHT = 'right arrow'
size = 20
increment = 1

class Snake:
    def __init__(self, x, y, color = 'white'):
        self.pos = [x, y]
        self.color = color
        self.size = size
        self.dir = [1, 0]
        self.snake = 0
    def show(self):
        canvas.delete(self.snake)
        finalPos = [i + self.size for i in self.pos]
        self.snake = canvas.create_rectangle(self.pos, finalPos, fill = self.color)
        self.snake
    def move(self):
        self.pos[0] += self.dir[0] * self.size
        self.pos[1] += self.dir[1] * self.size
    def setDirection(self, direction):
        self.dir = direction
    def colision(self, obstacle):
        if self.pos == obstacle.pos: return True
        return False

class Food:
    def __init__(self, color = 'red'):
        self.size = size
        self.pos = [randint(0, (width / self.size) - 1) * self.size, randint(0, (height / self.size) - 1) * self.size]
        self.food = 0
        self.color = color
        self.show()
    def show(self):
        canvas.delete(self.food)
        finalPos = [self.pos[0] + self.size, self.pos[1] + self.size]
        self.food = canvas.create_rectangle(self.pos, finalPos, fill = self.color)
#posicion random, crear cabeza, crear comida
x, y = randint(0, width / size) * size, randint(0, height / size) * size
snake = [Snake(x, y, color = 'green')]
food = Food()
while True:
    #colision con el cuerpo
    for index in range(1, len(snake)):
        if snake[0].colision(snake[index]): print('True')
    #colision con comida
    if snake[0].colision(food): 
        canvas.delete(food.food)
        food = Food()
        for add in range(increment):
            lenght = len(snake)
            x, y = snake[lenght - 1].pos[0] - size, snake[lenght - 1].pos[1]
            snake.append(Snake(x, y))
    #mostrar snake
    directions = [piece.dir for piece in snake]
    for pieces in snake:
        pieces.show()
        pieces.move()
    #teclado
    while True:
        try:
            if is_pressed(KEY_UP) and snake[0].dir != [0, 1]: snake[0].setDirection([0, -1])
            elif is_pressed(KEY_DOWN) and snake[0].dir != [0, -1]: snake[0].setDirection([0, 1])
            elif is_pressed(KEY_LEFT) and snake[0].dir != [1, 0]: snake[0].setDirection([-1, 0])
            elif is_pressed(KEY_RIGHT) and snake[0].dir != [-1, 0]: snake[0].setDirection([1, 0])
            for index in range(1, len(snake)):
                snake[index].setDirection(directions[index - 1])
            break
        except:
            break
    sleep(size / 500)
    tk.update()
tk.mainloop()