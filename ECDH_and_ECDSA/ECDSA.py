from curve_base_class.DiscreteEllipticCurve import DiscreteEllipticCurve as EllipticCurve
import gmpy2
import random
from binascii import b2a_hex, a2b_hex
from binascii import hexlify, unhexlify
from misc import egcd
from misc import quick_mulmod, quick_powmod

p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
a = 0
b = 7
xG = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
yG = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
h = 1

E = EllipticCurve(a=a, b=b, p=p)
E.get_GF(GF=n)
G = (xG, yG)

d_A = gmpy2.next_prime(random.randint(0xe32868331fa8ef0138de0de85478346aec5e3912b6029ae71691c384237a3eeb,
                                      0xfff868331fa8ef0138de0de85478346aec5e3912b6029ae71691c384237a3eeb))
H_A = E.get_scalar_multiplication(d_A, G)

z = 0x48656c6c6f21
k = gmpy2.next_prime(random.randint(0x132868331fa8ef0138de0de85478346aec5e3912b6029ae71691c384237a3eeb,
                                    0xfff868331fa8ef0138de0de85478346aec5e3912b6029ae71691c384237a3eeb))

P = E.get_scalar_multiplication(k, G)
r = P[0] % n
assert r != 0
s = quick_mulmod(egcd(k, n), (z + r * d_A), n)
assert s != 0
signature = (r, s)

u1 = quick_mulmod(egcd(s, n), z, n)
u2 = quick_mulmod(egcd(s, n), r, n)
P0 = E.get_three_pionts(
    E.get_scalar_multiplication(u1, G),
    E.get_scalar_multiplication(u2, H_A))
assert P0 == P

print("""Curve: secp256k1
Private key: {}
Public key: {}

Message: {}
Signature: {}
Verification: signature matches
""".format(d_A,H_A,z,signature))