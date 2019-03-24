from curve_base_class.DiscreteEllipticCurve import DiscreteEllipticCurve as EllipticCurve
import gmpy2
import random

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
d_B = gmpy2.next_prime(random.randint(0xcef147652aa90162e1fff9cf07f2605ea05529ca215a04350a98ecc24aa34342,
                                      0xffff47652aa90162e1fff9cf07f2605ea05529ca215a04350a98ecc24aa34342))
H_B = E.get_scalar_multiplication(d_B, G)

S_A = E.get_scalar_multiplication(d_A, H_B)
S_B = E.get_scalar_multiplication(d_B, H_A)

print("""Curve: secp256k1
Alice's private key: {}
Alice's public key: {}
Bob's private key: {}
Bob's public key: {}
Shared secret calculate by Alice : {}
Shared secret calculate by Bob : {}
""".format(d_A, H_A, d_B, H_B, S_A, S_B))
