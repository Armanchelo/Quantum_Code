from math import pi, cos, sin
import win32api, win32con, win32gui
from chempy import balance_stoichiometry
from bs4 import BeautifulSoup
import requests
import wget

projection = [
    [1, 0, 0],
    [0, 1, 0]
]

creators = ['Armando Chaparro Rocha', 'Javier Alejandro Vázquez Saenz', 'Io Fernanda Resendez','Jorge Demian Muñoz Marín', 'en colaboracion del doctor Adrián Domínguez Rodríguez']

def matMul(matrixA, matrixB):
    colsA = len(matrixA[0])
    rowsA = len(matrixA)
    colsB = len(matrixB[0])
    rowsB = len(matrixB)
    result = []
    temp = []
    if colsA != rowsB: return 'not match'
    for i in range(rowsA):
        for k in range(colsB):
            suma = 0
            for j in range(colsA):
                suma += matrixA[i][j] * matrixB[j][k]
            temp.append(suma)
        result.append(temp)
        temp = []
    return result

def matAdd(matrixA, matrixB):
    colsA = len(matrixA[0])
    rowsA = len(matrixA)
    colsB = len(matrixB[0])
    rowsB = len(matrixB)
    result = []
    if colsA == colsB and rowsA == rowsB:
        for i in range(rowsA):
            temp = []
            for j in range(colsA):
                temp.append(matrixA[i][j][0] + matrixB[i][j][0])
            result.append(temp)
    return result

def matSub(matrixA, matrixB):
    colsA = len(matrixA[0])
    rowsA = len(matrixA)
    colsB = len(matrixB[0])
    rowsB = len(matrixB)
    result = []
    if colsA == colsB and rowsA == rowsB:
        for i in range(rowsA):
            temp = []
            for j in range(colsA):
                temp.append(matrixA[i][j][0] - matrixB[i][j][0])
            result.append(temp)
    return result

def project(points):
    result = []
    for i in range(len(points)):
        result.append(matMul(projection, points[i]))
    return result

def rotateX(angle, points):
    result = []
    rotatex = [
        [1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)]
    ]
    for point in points:
        result.append(matMul(rotatex, point))
    return result

def rotateY(angle, points):
    result = []
    rotatey = [
        [cos(angle), 0, sin(angle)],
        [0, 1, 0],
        [-sin(angle), 0, cos(angle)]
    ]
    for point in points:
        result.append(matMul(rotatey, point))
    return result

def rotateZ(angle, points):
    result = []
    rotatez = [
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1]
    ]
    for point in points:
        result.append(matMul(rotatez, point))
    return result

def coordsToArray(coords):
    result = []
    for i in range(len(coords)):
        x = coords[i][0]
        y = coords[i][1]
        z = coords[i][2]
        result.append([[x], [y], [z]])
    return result

def arrayToCoords(arrays):
    result = []
    for i in range(len(arrays)):
        x = arrays[i][0][0]
        y = arrays[i][1][0]
        z = arrays[i][2][0]
        result.append([x, y, z])
    return result

ironmanOriginal = r'C:\Users\Usuario\favorite ironman.jpg'
ironmanNew = r'C:\Users\Usuario\Iron-Man-Wallpaper.jpg'
def setWallpaper(path):
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    # win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "0")
    # win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, 1+2)

def chemBalance(formula):
    formula = formula.replace(' ', '')
    formula = formula.split('=')
    reactivos = formula[0].split('+')
    productos = formula[1].split('+')
    reac, prod = balance_stoichiometry(reactivos, productos)
    reacs = ''
    index = 0
    for reactivo in reactivos:
        if reac.get(reactivo) != 1:
            reacs += str(reac.get(reactivo))
        reacs += reactivo
        if index < len(reactivos) - 1:
            reacs += ' + '
        index += 1
    reacs += ' = '
    index = 0
    for producto in productos:
        if prod.get(producto) != 1:
            reacs += str(prod.get(producto))
        reacs += producto
        if index < len(productos) - 1:
            reacs += ' + '
        index += 1
    print(reacs)

def main():
    print('hola')

if __name__ == '__main__':
    main()