from matplotlib import pyplot as plt
import numpy as np
from math import *
def PLOT():
    x = np.arange(-10, 10, 0.01)
    y = x**2
    plt.plot(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("x**2")
    plt.grid()
    plt.show()
