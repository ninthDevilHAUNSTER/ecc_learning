'''
不难发现，前40个被拆为 前40和后40的部分
后40通过了 SHA256 加密生成了 h

首先来跟踪前40位的部分

如果s > q 那么会打印bad signature

就好像盲注一样，可以通过二分`盲注`来爆破出q的值；
这个不会非常困难。由于我没有环境部署这个题目，就暂且跳过了。

随后，会计算S，这个S的来源有点古怪。
'''


# just elliptic-curve addition, nothing to see here
def add(q, a, b, P, Q):
    if () in (P, Q):
        return (P, Q)[P == ()]
    (Px, Py), (Qx, Qy) = P, Q
    try:
        if P != Q:
            lam = (Qy - Py) * gmpy2.invert(Qx - Px, q) % q
        else:
            lam = (3 * Px ** 2 + a) * gmpy2.invert(2 * Py, q) % q
    except ZeroDivisionError:
        return ()
    Rx = (lam ** 2 - Px - Qx) % q
    Ry = (lam * Px - lam * Rx - Py) % q
    return int(Rx), int(Ry)


# just elliptic-curve scalar multiplication, nothing to see here
def mul(q, a, b, n, P):
    R = ()
    while n:
        if n & 1: R = add(q, a, b, R, P)
        P, n = add(q, a, b, P, P), n // 2
    return R


def sqrt(n, p):
    if p % 4 != 3: raise NotImplementedError()
    return pow(n, (p + 1) // 4, p) if pow(n, (p - 1) // 2, p) == 1 else None


# q = 0x247ce416cf31bae96a1c548ef57b012a645b8bff68d3979e26aa54fc49a2c297
# q = 247ce416cf31bae96a1c548ef57b012a645b8bff68d3979e26aa54fc49a2c2
# q = 10feab68fea4ecbc95e2f7c67ebcf83e75fc0e0357006ca2429559f4aa83fce8
payload = "0" * 0x3F + "1" * 2
print(payload)

from Crypto.Hash import SHA256

msg = 'Give me the flag. This is an order!    '

q = 16503925798136106726026894143294039201809205899921475051089186096065043153559
a = 5079713781418039671549386476218981709382212150018593601284925328028384622133
b = 8575167449093451733644615491327478728087226005203626331099704278682109092640
field_order = 16503925798136106726026894143294039201930439456987742756395524593191976084900

import gmpy2

e = 65537
hx = int(SHA256.new(msg.encode()).hexdigest(), 16)
hy = sqrt(pow(hx, 3, q) + a * hx + b, q)
e_inv = gmpy2.invert(e, field_order)
S = mul(q, a, b, e_inv, (hx, hy))
check = mul(q, a, b, e, S)
assert check[0] == hx

print(hex(S[0]).replace('0x','') + msg)
# 7686967761062894595574008932965670857507945812015974344642518006035151846632
# 10feab68fea4ecbc95e2f7c67ebcf83e75fc0e0357006ca2429559f4aa83fce8
