#!/usr/bin/env python3

# This script makes use of another module: common.py, which can be
# found on GitHub:
#
#  https://github.com/andreacorbellini/ecc/blob/master/logs/common.py
#
# You must place that module on the same directory of this script
# prior to running it.

import math
import random
from curve_base_class import EllipticCurve as curve


def log(p, q):
    assert curve.is_on_curve(p)
    assert curve.is_on_curve(q)

    sqrt_n = int(math.sqrt(curve.n)) + 1

    # Compute the baby steps and store them in the 'precomputed' hash table.
    r = None
    precomputed = {None: 0}

    for a in range(1, sqrt_n):
        r = curve.add(r, p)
        precomputed[r] = a

    # Now compute the giant steps and check the hash table for any
    # matching point.
    r = q
    s = curve.mult(sqrt_n, curve.neg(p))

    for b in range(sqrt_n):
        try:
            a = precomputed[r]
        except KeyError:
            pass
        else:
            steps = sqrt_n + b
            logarithm = a + sqrt_n * b
            return logarithm, steps

        r = curve.get_three_pionts(r, s)

    raise AssertionError('logarithm not found')
