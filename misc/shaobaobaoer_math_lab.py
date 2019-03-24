# ll mul_mod(ll a, ll b, ll c) {
#     ll res = 0;
#     while(b) {
#         if(b & 1) res = (res + a) % c;
#         a = (2 * a) % c;
#         b >>= 1;
#     }
#     return res;
# }
#
# ll pow_mod(ll a, ll b, ll c) {
#     ll res = 1;
#     while(b) {
#         if(b & 1) res = (res * a) % c;
#         a = (a * a) % c;
#         b >>= 1;
#     }
#     return res;
# }
def quick_mulmod(a,b,c):
    '''
    python 快速乘取膜
    :param a:
    :param b:
    :param c:
    :return:
    '''
    a = a % c
    ans = 0
    # 这里我们不需要考虑b<0，因为分数没有取模运算
    while b != 0:
        if b & 1:
            ans = (ans + a) % c
        b >>= 1
        a = (2 * a) % c
    return ans


def quick_powmod(a, b, c):
    '''
    python 快速幂取膜
    :param a:
    :param b:
    :param c:
    :return:
    '''
    a = a % c
    ans = 1
    # 这里我们不需要考虑b<0，因为分数没有取模运算
    while b != 0:
        if b & 1:
            ans = (ans * a) % c
        b >>= 1
        a = (a * a) % c
    return ans

def egcd(a, b):
    '''
    扩展欧几里得算法（egcd）：
    基本思路：对于不全为 0 的非负整数 a，b，gcd（a，b）表示 a，b 的最大公约数，必然存在整数对 x，y ，使得 gcd（a，b）=ax+by。

    证明：设 a>b。
　　1，显然当 b=0，gcd（a，b）=a。此时 x=1，y=0；
　　2，ab!=0 时
　　设 ax1+by1=gcd(a,b);
　　bx2+(a mod b)y2=gcd(b,a mod b);
　　根据朴素的欧几里德原理有 gcd(a,b)=gcd(b,a mod b);
　　则:ax1+by1=bx2+(a mod b)y2;
　　即:ax1+by1=bx2+(a-(a/b)*b)y2=ay2+bx2-(a/b)*by2;
　　根据恒等定理得：x1=y2; y1=x2-(a/b)*y2;

    这样我们就得到了求解 x1,y1 的方法：x1，y1 的值基于 x2，y2
　  上面的思想是以递归定义的，因为 gcd 不断的递归求解一定会有个时候 b=0，所以递归可以结束。
    :param a:
    :param b:
    :return:
    '''
    if b == 0:
        return 1, 0
    else:
        x, y = egcd(b, a % b)
        return y, x - a / b * y


def gcd(a, b):
    '''
    欧几里德算法(gcd)又称辗转相除法，用于计算两个整数a,b的最大公约数。
    基本思路：设a=qb+r，其中a，b，q，r都是整数，则gcd(a,b)=gcd(b,r)，即gcd(a,b)=gcd(b,a%b)。
    :param a:
    :param b:
    :return:
    '''
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def ext_euclid(a, b):
    if (b == 0):
        return 1, 0, a
    else:
        x, y, q = ext_euclid(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y, q


def bits(n):
    """
    Generates the binary digits of n, starting
    from the least significant bit.

    bits(151) -> 1, 1, 1, 0, 1, 0, 0, 1
    """
    while n:
        yield n & 1
        n >>= 1


def double_and_add(n, x):
    """
    Returns the result of n * x, computed using
    the double and add algorithm.
    """
    result = 0
    addend = x

    for bit in bits(n):
        if bit == 1:
            result += addend
        addend *= 2

    return result

## 这个EGCD 是作者写的，就用这个好了

def extended_euclidean_algorithm(a, b):
    """
    Returns a three-tuple (gcd, x, y) such that
    a * x + b * y == gcd, where gcd is the greatest
    common divisor of a and b.

    This function implements the extended Euclidean
    algorithm and runs in O(log b) in the worst case.

    """
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def inverse_of(n, p):
    """
    Returns the multiplicative inverse of
    n modulo p.

    This function returns an integer m such that
    (n * m) % p == 1.
    """
    gcd, x, y = extended_euclidean_algorithm(n, p)
    assert (n * x + p * y) % p == gcd

    if gcd != 1:
        # Either n is 0, or p is not a prime number.
        raise ValueError(
            '{} has no multiplicative inverse '
            'modulo {}'.format(n, p))
    else:
        return x % p
