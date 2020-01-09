from math import cos, sin, pi
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

projection = [
    [1, 0, 0],
    [0, 1, 0]
]

def rotateX(angle, point):
    rotatex = [
        [1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)]
    ]
    rotatex = matMul(rotatex, point)
    return rotatex

def rotateY(angle, point):
    rotatey = [
        [cos(angle), 0, sin(angle)],
        [0, 1, 0],
        [-sin(angle), 0, cos(angle)]
    ]
    rotatey = matMul(rotatey, point)
    return rotatey

def rotateZ(angle, point):
    rotatez = [
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1]
    ]
    rotatez = matMul(rotatez, point)
    return rotatez