from misc.CipollaAlg import p_mod


def fool_solve(A, B, C, D, p, k, b):
    '''
    Ax^3 + Bx^2 + Cx + D == 0 (mod p)
    Burping Alg
    :param A:
    :param B:
    :param C:
    :param D:
    :param p:
    :return:
    '''
    # solution = []
    # for x in range(0, p):
    #     if (A * x ** 3 + B * x ** 2 + C * x + D) % p == 0:
    #         solution.append((x, (k * x + b) % p))
    # assert solution.__len__() != 0
    # return solution

    # 为了让结果尽可能小,计算尽可能快采用绝对值最小剩余系
    # 已知p为素数
    solution = []
    for x in range(int(-(p + 1) / 2), int((p - 1) / 2)):
        if (A * x ** 3 + B * x ** 2 + C * x + D) % p == 0:
            solution.append((
                p_mod(x, p),
                p_mod((k * x + b) % p, p))
            )
            assert solution.__len__() != 0
    return solution
