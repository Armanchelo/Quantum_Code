import tkinter as Tk
import keyboard
import random
import win32api

tk = Tk.Tk()
tk.overrideredirect(True)
w, h = tk.winfo_screenwidth(), tk.winfo_screenheight()
# w, h = 600, 600
tk.geometry("%dx%d+0+0" % (w, h))
canvas = Tk.Canvas(tk, bg = 'black', width = w, height = h)
canvas.pack()

background = Tk.PhotoImage(file = 'flappy_ground.png')

class Bird:
    radius = 20
    def __init__(self, x, y, color = 'yellow'):
        self.x = x
        self.y = y
        self.velocity = 0
        self.gravity = .005
        self.up = 0
        self.color = color
        self.bird = 0
        self.top = self.y - self.radius
        self.bottom = self.y + self.radius
        self.right = self.x + self.radius
        self.left = self.x - self.radius

    def update(self, jump = False):
        self.velocity += self.gravity
        self.velocity = min(2, max(-1, self.velocity))
        self.y += self.velocity
        if jump:
            self.up += .05
            self.velocity -= self.up
            self.y += self.velocity
            self.show()
        self.up = 0   
        if self.bottom <= 0: self.y = self.radius
        if self.y >= h: self.y = h - self.radius 

    def show(self):
        canvas.delete(self.bird)
        x, y, radius = self.x, self.y, self.radius
        self.bird = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill = self.color)
        self.bird
        tk.update()

    def colision(self, obstacle):
        if self.right > obstacle.x and self.left < obstacle.x:
            if self.y < obstacle.top[1] or self.y > obstacle.bottom[0]:
                obstacle.color = 'red'
                

class Obstacle():
    width = 70
    def __init__(self, x, color = 'green'):
        self.x = x
        self.space = 150
        self.top = (0, random.randint(0, h - self.space - 20))
        self.bottom = (self.top[1] + self.space, h)
        self.obstacleTop = 0
        self.obstacleBottom = 0
        self.color = color
        self.velocity = 1
    
    def show(self):
        canvas.delete(self.obstacleTop)
        canvas.delete(self.obstacleBottom)
        self.obstacleTop = canvas.create_line(self.x, self.top[0], self.x, self.top[1], fill = self.color, width = self.width * 2)
        self.obstacleBottom = canvas.create_line(self.x, self.bottom[0], self.x, self.bottom[1], fill = self.color, width = self.width * 2) 
        self.obstacleTop
        self.obstacleBottom

    def update(self):
        self.x -= self.velocity

space = 2
canvas.create_image(0, 0, image = background)

bird = Bird(200, h / 2, color = 'black')
obstacle = [Obstacle((w / space) + (nums * (w / space))) for nums in range(3)]
bird.show()
while True:
    # x, y = win32api.GetCursorPos()
    for obstacles in obstacle:
        obstacles.show()
        tk.update()
        bird.colision(obstacles)
        obstacles.update()
        if obstacles.x < -obstacles.width: 
            obstacle.pop(0)
            canvas.delete(obstacles.obstacleTop)
            canvas.delete(obstacles.obstacleBottom)
            obstacle.append(Obstacle(w + (w / space)))
    if keyboard.is_pressed(' '):
        bird.update(jump = True)
    else:
        bird.update()
    # bird.y = y
    bird.show()

tk.mainloop()

