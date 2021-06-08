from FUNCTIONS import *
import argparse
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

parser = argparse.ArgumentParser(description='Determinate mode')
parser.add_argument('-mode', default = '', help = 'Definir el modo de operacion de MAFER')
args = parser.parse_args()
mode = args.mode
if mode.startswith('m'): mode = 'manual'

Internet = hayInternet()

funciones = [
    'cuentame sobre', 'crear reporte sobre', 'apagar en', 'cancelar apagado', 'reiniciar en', 'cancelar reinicio',
    'crear nota numero', 'abrir nota numero', 'eliminar nota numero', 'traducir texto', 'traducir', 'graficar', 
    'buscar', 'balancear ecuacion quimica', 'presentate', 'modo manual', 'manos libres', 'adios'
]

def Comando():
    cambiarModo = mode
    if mode != 'manual':
        comando = escuchar('es')
    else:
        decir('introduce tu comando', False)
        comando = input('introduce tu comando: ')
    funcion = esFuncion(funciones, comando)
    if funcion != 'no es funcion':
        busqueda = comando.replace(funcion + ' ', '')
    else:
        busqueda = ''
        comando = traducir(comando, 'en')
        wolfram(comando)
    if busqueda != '':
        if funcion == 'cuentame sobre': cuentameSobre(busqueda)
        elif funcion == 'crear reporte sobre': crearReporte(busqueda)
        elif funcion == 'apagar en': apagar(busqueda)
        elif funcion == 'cancelar apagado': cancelarApagado()
        elif funcion == 'reiniciar en': reiniciar(busqueda)
        elif funcion == 'cancelar reinicio': cancelarApagado()
        elif funcion == 'crear nota numero': tomarNota(busqueda)
        elif funcion == 'abrir nota numero': abrirNota(busqueda)
        elif funcion == 'traducir documento': traducir('documento')
        elif funcion == 'traducir texto': traducir('texto')
        elif funcion == 'traducir': decir(traducir(busqueda, language = 'en'))
        elif funcion == 'graficar': graficar()
        elif funcion == 'buscar': buscar(busqueda)
        elif funcion == 'balancear ecuacion quimica': chemBalance()
        elif funcion == 'presentate': presentacion()
        elif funcion == 'adios': despedida()
        elif funcion == 'modo manual': cambiarModo = 'manual'
        elif funcion == 'manos libres': cambiarModo = ''
    return cambiarModo

# class product:
#     def __init__(self, window):
#         self.window = window
#         self.window.title('MAFER')

#         ruta = 'C:\\Users\\Usuario\\Desktop\\mafer.png'
#         im1 = Image.open(ruta)
#         background_image = ImageTk.PhotoImage(im1)
#         background_label = Label(self.window, image=background_image)
#         background_label.image = background_image
#         background_label.place(x=0, y=0)
#         w = background_image.width()
#         h = background_image.height()
#         self.window.geometry('%dx%d+0+0' % (w,h))
#         fondo = '#0F0F0F'
#         btn = Button(self.window, 
#                 bg=fondo,
#                 fg='#7E307F',
#                 relief='flat',
#                 text = 'COMANDO',
#                 font = 'Times 20',
#                 width=20, command = comando)
#         btn.place(x = int(round(w / 2)) - 170, y = int(round(h / 2)))
#         # boton = ttk.Button(self.window, text = 'COMANDO', command = comando)
#         # boton.place(x = int(round(w / 2)) - 42, y = int(round(h / 2)))
if Internet == False:
    mode = 'manual'
    decir('cambie a modo manual debido a que no tengo internet')    

while True:
    nuevoModo = Comando()
    if nuevoModo != mode:
        decir('cambiando de modo')
        mode = nuevoModo