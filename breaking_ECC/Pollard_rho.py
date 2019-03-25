from curve_base_class.DiscreteEllipticCurve import DiscreteEllipticCurve as EllipticCurve
from misc import egcd
import random


class PollardRhoSequence:

    def __init__(self, point1, point2, E):
        self.point1 = point1
        self.point2 = point2
        self.E = E

        self.add_a1 = random.randrange(1, E.GF)
        self.add_b1 = random.randrange(1, E.GF)
        self.add_x1 = E.get_three_pionts(
            E.get_scalar_multiplication(self.add_a1, point1),
            E.get_scalar_multiplication(self.add_b1, point2),
        )

        self.add_a2 = random.randrange(1, E.GF)
        self.add_b2 = random.randrange(1, E.GF)
        self.add_x2 = E.get_three_pionts(
            E.get_scalar_multiplication(self.add_a2, point1),
            E.get_scalar_multiplication(self.add_b2, point2),
        )

    def __iter__(self):
        partition_size = self.E.p // 3 + 1

        x = (0, 0)
        a = 0
        b = 0

        while True:
            if x == (0, 0):
                i = 0
            else:
                i = x[0] // partition_size

            if i == 0:
                # x is either the point at infinity (None), or is in the first
                # third of the plane (x[0] <= curve.p / 3).
                a += self.add_a1
                b += self.add_b1
                x = self.E.get_three_pionts(x, self.add_x1)
            elif i == 1:
                # x is in the second third of the plane
                # (curve.p / 3 < x[0] <= curve.p * 2 / 3).
                a *= 2
                b *= 2
                x = self.E.get_scalar_multiplication(2, x)
            elif i == 2:
                # x is in the last third of the plane (x[0] > curve.p * 2 / 3).
                a += self.add_a2
                b += self.add_b2
                x = self.E.get_three_pionts(x, self.add_x2)
            else:
                raise AssertionError(i)

            a = a % self.E.GF
            b = b % self.E.GF

            yield x, a, b


def log(p, q, curve, counter=None):
    assert curve.is_on_curve(p)
    assert curve.is_on_curve(q)

    # Pollard's Rho may fail sometimes: it may find a1 == a2 and b1 == b2,
    # leading to a division by zero error. Because PollardRhoSequence uses
    # random coefficients, we have more chances of finding the logarithm
    # if we try again, without affecting the asymptotic time complexity.
    # We try at most three times before giving up.
    for i in range(3):
        sequence = PollardRhoSequence(p, q, curve)

        tortoise = iter(sequence)
        hare = iter(sequence)

        # The range is from 0 to curve.n - 1, but actually the algorithm will
        # stop much sooner (either finding the logarithm, or failing with a
        # division by zero).
        for j in range(curve.GF):
            x1, a1, b1 = next(tortoise)
            x2, a2, b2 = next(hare)
            x2, a2, b2 = next(hare)

            if x1 == x2:
                if b1 == b2:
                    # This would lead to a division by zero. Try with
                    # another random sequence.
                    break

                x = (a1 - a2) * egcd(b2 - b1, curve.GF)
                logarithm = x % curve.GF
                steps = i * curve.GF + j + 1
                return logarithm, steps

    raise AssertionError('logarithm not found')


if __name__ == '__main__':
    E = EllipticCurve(a=1, b=-1, p=10177, GF=10331)
    p = (0x1, 0x1)
    q = (0x1a28, 0x8fb)
    k = 325
    print(log(p, q, E))
