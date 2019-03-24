# draw_curve/draw.py
from matplotlib import pyplot as plt
import numpy as np


def continuous_curve():
    a = -2
    b = 3
    y, x = np.ogrid[-5:5:100j, -5:5:100j]
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0])
    plt.grid()
    plt.legend()
    plt.show()


def discrete_curve():
    a = -2
    b = 3
    p = 19
    X = np.linspace(-p, p, p * 2 + 1)
    Y = []
    Z = []
    for x in X:
        Z.append(
            np.sqrt(pow(x, 3) + x * a + b) % p)
        Y.append(- (
                np.sqrt(pow(x, 3) + x * a + b) % p))
    plt.scatter(X, Z, color='red')
    # plt.scatter(X, Y, color='red')
    plt.xlim([-p - 1, p + 1])
    plt.ylim([0, p + 1])
    plt.show()


if __name__ == '__main__':
    discrete_curve()
