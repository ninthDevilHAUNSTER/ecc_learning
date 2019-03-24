import numpy as np
from matplotlib import pyplot as plt
import sympy
from misc import bits


class ContinuousEllipticCurve(object):
    def __init__(self, a, b, x_range=(-10, 10)):
        if 4 * a ** 3 + 27 * b ** 2 == 0:
            raise Warning(BaseException, "curve contains singularities")
        self.a = a
        self.b = b
        self.x_range = x_range
        self.x = np.ogrid[x_range[0]:x_range[1]:0.01]
        self.y_positive = np.array([], dtype='float32')
        self.__gen_x_y()
        self.P = (0, 0)
        self.Q = (0, 0)
        self.R = (0, 0)

    def __gen_x_y(self):
        '''
        note: for x that value is so small will fail to get sqrt
        :return:
        '''
        self.y_positive = np.sqrt(
            pow(self.x, 3) + self.x * self.a + self.b)

    def draw_curve(self, xlim=None, ylim=None):
        if ylim is None:
            ylim = [-5, 5]
        if xlim is None:
            xlim = [-5, 5]
        plt.plot(self.x, self.y_positive, color='red')
        plt.plot(self.x, -self.y_positive, color='red')
        plt.xlim(xlim)
        plt.ylim(ylim)
        plt.show()

    def __check_on_curve(self, point):
        if abs(point[1] - np.sqrt(pow(point[0], 3) + point[0] * self.a + self.b)) <= 0.01 \
                or \
                abs(point[1] + np.sqrt(pow(point[0], 3) + point[0] * self.a + self.b)) <= 0.01:
            return True
        else:
            return False

    def __cal_R(self, P, Q, solve):
        R = solve.copy()
        # print(solve)
        for item in solve:
            if (np.abs(P[0] - item[0]) < 0.01
                and np.abs(P[1] - item[1]) < 0.01) or \
                    (np.abs(Q[0] - item[0]) < 0.01
                     and np.abs(Q[1] - item[1]) < 0.01):
                R.pop(R.index(item))
        return (float(R[0][0]), -float(R[0][1]))

    def get_scalar_multiplication(self, n, P):
        """
        Returns the result of n * x, computed using
        the double and add algorithm.
        """
        self.R = (0, 0)
        self.P = P
        for bit in bits(n):
            if bit == 1:
                self.R = self.get_three_pionts(self.P, self.R)
            self.P = self.get_three_pionts(self.P, self.P)
        return self.R

    def get_three_pionts(self, P, Q):
        '''
        Calculte the third point in curve
        :param P: (x,y)
        :param Q: (x,y)
        :return:
        '''
        if P == (0, 0) or Q == (0, 0):
            return Q if P == (0, 0) else P

        if self.__check_on_curve(P) and self.__check_on_curve(Q):
            if P == Q:
                # CASE 1
                k = (3 * P[0] ** 2 + self.a) / (2 * P[1])
                b = P[1] - k * P[0]
                x = k ** 2 - P[0] - Q[0]
                y = k * x + b
                R = (x, -y)
            else:
                # CASE 2
                k = (P[1] - Q[1]) / (P[0] - Q[0])
                b = P[1] - k * P[0]
                x = k ** 2 - P[0] - Q[0]
                y = k * x + b
                R = (x, -y)
            return R
        else:
            raise ValueError

    def __str__(self):
        return "$$ y^2 = x^3 + {a}x + {b} $$".format(a=self.a, b=self.b)


# 计算$R_x \equiv k^2 - x1 - x2 (mod \;p $

if __name__ == '__main__':
    E1 = ContinuousEllipticCurve(-7, 10)
    E1.get_scalar_multiplication(8, (1, 2))
    print(E1.R)
