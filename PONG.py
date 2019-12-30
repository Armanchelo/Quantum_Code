from tkinter import *
from keyboard import *

tk = Tk()
tk.overrideredirect(True)
w, h = tk.winfo_screenwidth(), tk.winfo_screenheight()
tk.geometry("%dx%d+0+0" % (w, h))
canvas = Canvas(tk, bg = 'black', width = w, height = h)
canvas.pack()

class Paddle:
    height, thick, velocity = 50, 10, 1
    def __init__(self, x, y, scorex, scorey, color):
        self.x, self.y, self.color, self.top, self.bottom, self.points, self.scorex, self.scorey, self.score = x, y, color, y - self.height, y + self.height, -1, scorex, scorey, 0
        self.add_point()
        self.paddle = canvas.create_line(self.x, self.y - self.height, self.x, self.y + self.height, fill = self.color, width = self.thick)
        self.show()
    def show(self):
        self.paddle
    def move(self, y):
        y *= self.velocity
        canvas.move(self.paddle, 0, y)
        self.y += y
        self.top += y
        self.bottom += y
    def add_point(self):
        self.points += 1
        canvas.delete(self.score)
        self.score = canvas.create_text(self.scorex, self.scorey, text = self.points, fill = self.color, font = 'Times 30 italic bold')
        self.score
        tk.update()

class Ball:
    radius, xspeed, yspeed = 15, 1, 1
    def __init__(self, x, y, color):
        self.x, self.y, self.color, self.left, self.right, self.top, self.bottom = x, y, color, x - self.radius, x + self.radius, y - self.radius, y + self.radius
        self.ball = canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, fill = self.color)
        self.show()
    def show(self):
        self.ball
    def move(self, x, y):
        x *= self.xspeed
        y *= self.yspeed
        canvas.move(self.ball, x, y)
        self.x += x
        self.y += y
        self.left += x
        self.right += x
        self.top += y
        self.bottom += y
    def destroy(self):
        canvas.delete(self.ball)

paddle_left = Paddle(50, h / 2, w / 2 - 50, 50, 'red')
paddle_right = Paddle(w - 50, h / 2, w / 2 + 50, 50, 'blue')
ball = Ball(w / 2, h / 2, 'white')
vel = .3
ball.xspeed, ball.yspeed = vel, vel

while True:
    if ball.top < 0 or ball.bottom > h: ball.yspeed *= -1
    if ball.left < paddle_left.x and ball.y > paddle_left.top and ball.y < paddle_left.bottom: ball.xspeed *= -1
    if ball.right > paddle_right.x and ball.y > paddle_right.top and ball.y < paddle_right.bottom: ball.xspeed *= -1
    if ball.left < 0:
        ball.destroy()
        ball = Ball(w / 2, h / 2, 'red')
        ball.xspeed, ball.yspeed = vel, vel
        paddle_right.add_point()
    if ball.right > w:
        ball.destroy()
        ball = Ball(w / 2, h / 2, 'red')
        ball.xspeed, ball.yspeed = -vel, vel
        paddle_left.add_point()
    ball.move(1, 1)
    while True:
        try:
            if is_pressed('w') and paddle_left.top > 0: paddle_left.move(-1)
            if is_pressed('s') and paddle_left.bottom < h: paddle_left.move(1)
            if is_pressed(KEY_UP) and paddle_right.top > 0: paddle_right.move(-1)
            if is_pressed(KEY_DOWN) and paddle_right.bottom < h: paddle_right.move(1)
            if is_pressed('q'): canvas.destroy()
            break
        except: break
    tk.update()
tk.mainloop()