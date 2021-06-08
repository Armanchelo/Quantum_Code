from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

def com1():
    print('boton')

class product:
    def __init__(self, window):
        self.window = window
        self.window.title('MAFER')

        ruta = 'C:\\Users\\Usuario\\Desktop\\mafer.png'
        im1 = Image.open(ruta)
        background_image = ImageTk.PhotoImage(im1)
        background_label = Label(self.window, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0)
        w = background_image.width()
        h = background_image.height()
        self.window.geometry('%dx%d+0+0' % (w,h))

        self.usuario = Entry(self.window)
        # self.usuario.insert(0, 'USER')
        self.usuario.focus()
        self.usuario.place(x = int(round(w / 2)) - 67, y = int(round(h / 2)) - 20)
        self.password = Entry(self.window, text = 'PASSWORD')
        self.password.place(x = int(round(w / 2)) - 67, y = int(round(h / 2)))

        ttk.Button(self.window, text = 'LOGIN', command = self.User).place(x = int(round(w / 2)) - 42, y = int(round(h / 2)) + 20)

    def User(self):
        print(f'Usuario: {self.usuario.get()}')
        print(f'contraseña: {self.password.get()}')

if __name__ == '__main__':
    window = Tk()
    aplicacion = product(window)
    window.mainloop()