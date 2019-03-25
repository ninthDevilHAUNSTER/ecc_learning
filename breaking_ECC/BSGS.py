from curve_base_class.DiscreteEllipticCurve import DiscreteEllipticCurve as EllipticCurve

'''
BSGS
Q = xP
Q = amP + bP
Q - amP = bP
'''

# TEST negative function
# E = EllipticCurve(2, 3, 97)
# TMP = E.get_scalar_multiplication(-2, (3, 6))
# print(TMP)
import math


def BSGS(E, p, q):
    # B
    step = 0
    hash_table = {}
    m = math.floor(math.sqrt(E.GF))
    for i in range(m):
        tmp = E.get_scalar_multiplication(i, p)
        hash_table[tmp] = i
    hash_list = hash_table.keys()
    # G
    for a in range(m):
        amP = E.get_scalar_multiplication(-a * m, p)
        Q_amP = E.get_three_pionts(amP, q)
        if Q_amP in hash_list:
            return hash_table[Q_amP] + a * m, step
        else:
            step += 1
    return 0, 0


if __name__ == '__main__':
    E = EllipticCurve(a=1, b=-1, p=10177, GF=10331)
    p = (0x1, 0x1)
    q = (0x1a28, 0x8fb)
    k = 325
    k0, step = BSGS(E, p, q)
    print(k0, step)
