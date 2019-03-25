import numpy as np
from matplotlib import pyplot as plt
import sympy
from misc import bits
from misc import cipolla_alg
# from gmpy2 import powmod
from misc import quick_powmod
from misc import egcd
from misc import fool_solve
from misc import positive_mod


class DiscreteEllipticCurve(object):
    def __init__(self, a, b, p, GF=None):
        if 4 * a ** 3 + 27 * b ** 2 == 0:
            raise Warning(BaseException, "curve contains singularities")
        self.a = a
        self.b = b
        self.p = p
        self.x_range = [0, p + 1]
        self.x = []
        self.y_positive = np.array([], dtype='int32')
        self.y_negtive = np.array([], dtype="int32")
        self.x_y = []
        # for speed , will not calculate all the points in EllipticCurve
        self.P = (0, 0)
        self.Q = (0, 0)
        self.R = (0, 0)
        self.know_GF = False
        self.GF = 0
        if GF is not None:
            self.get_GF(GF)

    def get_GF(self, GF):
        '''
        我是windows的电脑，算这个有些捉襟见肘
        :return:
        '''
        self.GF = GF
        self.know_GF = True

    def __gen_x_y(self):
        '''
        note: for x that value is so small will fail to get sqrt
        :return:
        '''
        y_p = []
        for x in range(0, self.p):
            y_double = pow(x, 3) + x * self.a + self.b
            if quick_powmod(y_double, int((self.p - 1) / 2), self.p) == 1:
                y_p.append(cipolla_alg(y_double, self.p))
                self.x.append(x)
            elif y_double % self.p == 0:
                self.x.append(x)
                y_p.append(0)
        self.y_positive = np.array(y_p, dtype='int32')
        self.y_negtive = self.p * np.ones(self.y_positive.shape) - self.y_positive
        self.x = np.array(self.x, dtype='int32')

        for index in range(self.x.__len__()):
            self.x_y.append((self.x[index], self.y_positive[index]))
            self.x_y.append((self.x[index], self.y_negtive[index]))

    def draw_curve(self, xlim=None, ylim=None, save=False):
        self.__gen_x_y()
        if ylim is None:
            ylim = [0, self.p - 1]
        if xlim is None:
            xlim = [0, self.p - 1]
        plt.scatter(self.x, self.y_positive, color='red')
        plt.scatter(self.x, self.y_negtive, color='red')
        plt.xlim(xlim)
        plt.ylim(ylim)
        plt.grid()
        if save == False:
            plt.show()
        else:
            plt.savefig('../picture/discreteEC_{a}_{b}_{p}_{time}.png'.format(
                a=self.a,
                b=self.b,
                p=self.p,
                time=__import__('datetime').datetime.now().strftime("%I_%M%p")
            ))

    def __check_on_curve(self, point):
        return True if (point[0] ** 3 + self.a * point[0] + self.b - point[1] ** 2) % self.p == 0 else False

    def is_on_curve(self, point):
        return True if (point[0] ** 3 + self.a * point[0] + self.b - point[1] ** 2) % self.p == 0 else False

    def __check_on_line(self, point, k, b):
        return True if (k * point[0] + b - point[1]) % self.p == 0 else False

    def __cal_R(self, P, Q, solve):
        solve.pop(solve.index(P))
        solve.pop(solve.index(Q))
        return positive_mod(solve[0][0], self.p), positive_mod(self.p - solve[0][1], self.p)

    def get_scalar_multiplication(self, n, P):
        """
        Returns the result of n * x, computed using
        the double and add algorithm.
        """
        assert self.__check_on_curve(P)
        if n == 0: return 0, 0
        if n < 0: return self.get_scalar_multiplication(-n, (P[0], -P[1] % self.p))
        if self.know_GF:
            n = n % self.GF
            self.R = (0, 0)
            self.P = P
            for bit in bits(n):
                if bit == 1:
                    self.R = self.get_three_pionts(self.P, self.R)
                self.P = self.get_three_pionts(self.P, self.P)
            return self.R
        else:
            self.R = (0, 0)
            self.P = P
            for bit in bits(n):
                if bit == 1:
                    self.R = self.get_three_pionts(self.P, self.R)
                self.P = self.get_three_pionts(self.P, self.P)
            return self.R

    def get_three_pionts(self, P, Q):
        '''
        :param P: (x,y)
        :param Q: (x,y)
        :return:
        '''
        if P == (0, 0) or Q == (0, 0):
            return Q if P == (0, 0) else P
        try:
            if self.__check_on_curve(P) and self.__check_on_curve(Q):
                # CASE 1 P == Q
                # 利用导数计算斜率
                if P == Q:
                    k = (3 * P[0] ** 2 + self.a) * egcd(2 * P[1], self.p)
                    k %= self.p
                    b = P[1] - k * P[0]
                    b %= self.p
                    x = k ** 2 - P[0] - Q[0]
                    y = k * x + b
                    R = (positive_mod(x, self.p), positive_mod(self.p - y, self.p))
                else:
                    # CASE 2 P != Q
                    k = (P[1] - Q[1]) * egcd(P[0] - Q[0], self.p)
                    k %= self.p
                    b = P[1] - k * P[0]
                    b %= self.p
                    x = k ** 2 - P[0] - Q[0]
                    y = k * x + b
                    R = (positive_mod(x, self.p), positive_mod(self.p - y, self.p))
                return R
            else:
                raise ValueError
        except AssertionError as e:
            return 0, 0

    def __str__(self):
        return "$$ y^2 \equiv x^3 + {a}x + {b} (mod \;{p})$$".format(a=self.a, b=self.b, p=self.p)

# if __name__ == '__main__':
#     E1 = DiscreteEllipticCurve(2, 3, 97)
#     TMP = E1.get_scalar_multiplication(8, (3, 6))
#     print(TMP)
