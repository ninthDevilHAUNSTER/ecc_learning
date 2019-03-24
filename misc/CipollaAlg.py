import gmpy2
import math
import random
from misc.shaobaobaoer_math_lab import quick_powmod


class T(object):
    def __init__(self, p, d):
        self.p = p
        self.d = d


# 二次域乘法
def multi_er(a, b, m, w):
    ans = T(0, 0)
    ans.p = (a.p * b.p % m + a.d * b.d % m * w % m) % m
    ans.d = (a.p * b.d % m + a.d * b.p % m) % m
    return ans


# 二次域快速幂
def power(a, b, m, w):
    ans = T(1, 0)
    while (b):
        if (b & 1):
            ans = multi_er(ans, a, m, w)
            b -= 1
        b = b >> 1
        a = multi_er(a, a, m, w)
    return ans


# 求解勒让德符号
def legendre(a, p):
    return quick_powmod(a, (p - 1) >> 1, p)


def p_mod(a, m):
    a %= m
    if a < 0: a += m
    return a


def solve(n, p):
    if (p == 2): return 1
    if (legendre(n, p) + 1 == p): return -1
    while (1):
        a = random.randint(0, p + 1)
        t = a * a - n
        w = p_mod(t, p)
        if (legendre(w, p) + 1 == p): break
    tmp = T(a, 1)
    ans = power(tmp, (p + 1) >> 1, p, w)
    return min(p - ans.p, ans.p)


if __name__ == '__main__':
    print(solve(512163, 97))
