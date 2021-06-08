import img2pdf
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
from zipfile import ZipFile

path = 'C:\\users\\Usuario\\Desktop\\'

Tk().withdraw()
filesdir = askopenfilenames()
filesdir = sorted(filesdir)

if filesdir[0].endswith('.zip'):
    for f in filesdir:
        z = ZipFile(f, 'r')
        z.extractall(path = r'C:/Users/Usuario/Downloads/')
        zip_images = ['C:\\Users\\Usuario\\Downloads\\' + image for image in z.namelist()]
        zip_images = sorted(zip_images)
        z.close()
else: zip_images = sorted(filesdir)

name = 'Zip2Pdf'
newname = input('Guardar como: ')
if newname: name = newname

with open(path + name + '.pdf', 'wb') as f:
    f.write(img2pdf.convert(zip_images))