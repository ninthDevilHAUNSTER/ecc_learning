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
    def __init__(self, a, b, p):
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
        self.__gen_x_y()
        self.P = (0, 0)
        self.Q = (0, 0)
        self.R = (0, 0)

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
        if point in self.x_y:
            return True
        else:
            return False

    def __check_on_line(self, point, k, b):
        if (k * point[0] + b - point[1]) % self.p == 0:
            return True
        else:
            return False

    def __cal_R(self, P, Q, solve):
        solve.pop(solve.index(P))
        solve.pop(solve.index(Q))
        return positive_mod(solve[0][0], self.p), positive_mod(self.p - solve[0][1], self.p)

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
        我这个算法鲁棒性还有点问题，碰上inf的点会直接炸掉因为
                assert (n * x + p * y) % p == gcd
        总之如果assert 了一定就是单位元点了（无限远点）
        :param P: (x,y)
        :param Q: (x,y)
        :return:
        '''
        R = (0, 0)
        if P == (0, 0) or Q == (0, 0):
            return Q if P == (0, 0) else P

        if self.__check_on_curve(P) and self.__check_on_curve(Q):
            # CASE 1 P == Q
            # 利用导数计算斜率
            if P == Q:
                k = (3 * P[0] ** 2 + self.a) * egcd(2 * P[1], self.p)
                k %= self.p
                b = P[1] - k * P[0]
                b %= self.p
                solve = fool_solve(
                    A=1, B=-k ** 2, C=self.a - 2 * k * b, D=self.b - b ** 2, p=self.p, k=k, b=b
                )
                solve.append(P)
                R = self.__cal_R(P, Q, solve)
            else:
                # CASE 2 P != Q 且 P + Q = -R
                k = (P[1] - Q[1]) * egcd(P[0] - Q[0], self.p)
                k %= self.p
                b = P[1] - k * P[0]
                b %= self.p
                solve = fool_solve(
                    A=1, B=-k ** 2, C=self.a - 2 * k * b, D=self.b - b ** 2, p=self.p, k=k, b=b
                )
                if solve.__len__() == 2:
                    # CASE 3 P != Q 但 P + Q = -P 或 P + Q = -Q 则 P 或者 Q 为曲线的切点
                    if ((3 * P[0] ** 2 + self.a) * egcd(2 * P[1], self.p) - k) % self.p == 0:
                        return P[0], positive_mod(self.p - P[1], self.p)
                    if ((3 * Q[0] ** 2 + self.a) * egcd(2 * Q[1], self.p) - k) % self.p == 0:
                        return Q[0], positive_mod(self.p - Q[1], self.p)
                else:
                    R = self.__cal_R(P, Q, solve)
            return R
        else:
            raise ValueError

    def __str__(self):
        return "$$ y^2 \equiv x^3 + {a}x + {b} (mod \;{p})$$".format(a=self.a, b=self.b, p=self.p)


if __name__ == '__main__':
    E1 = DiscreteEllipticCurve(2, 3, 97)
    # print(E1)
    # TMP = E1.get_three_pionts((3, 6), (80, 10))
    for n in range(6,10):
        TMP = E1.get_scalar_multiplication(n, (3, 6))
        print(TMP)
