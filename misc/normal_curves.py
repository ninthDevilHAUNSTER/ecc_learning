from curve_base_class.DiscreteEllipticCurve import DiscreteEllipticCurve as EllipticCurve

curves = {
    'prime192v1': EllipticCurve(

        p=0xfffffffffffffffffffffffffffffffeffffffffffffffff,
        a=0xfffffffffffffffffffffffffffffffefffffffffffffffc,
        b=0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1,
    ),
    'secp224r1': EllipticCurve(

        p=0xffffffffffffffffffffffffffffffff000000000000000000000001,
        a=0xfffffffffffffffffffffffffffffffefffffffffffffffffffffffe,
        b=0xb4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4,
    ),
    'secp384r1': EllipticCurve(

        p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffff0000000000000000ffffffff,
        a=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffff0000000000000000fffffffc,
        b=0xb3312fa7e23ee7e4988e056be3f82d19181d9c6efe8141120314088f5013875ac656398d8a2ed19d2a85c8edd3ec2aef,
    ),
    'secp521r1': EllipticCurve(

        p=0x01ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff,
        a=0x01fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc,
        b=0x0051953eb9618e1c9a1f929a21a0b68540eea2da725b99b315f3b8b489918ef109e156193951ec7e937b1652c0bd3bb1bf073573df883d2c34f1ef451fd46b503f00,
    ),
    'prime192v2': EllipticCurve(

        p=0xfffffffffffffffffffffffffffffffeffffffffffffffff,
        a=0xfffffffffffffffffffffffffffffffefffffffffffffffc,
        b=0xcc22d6dfb95c6b25e49c0d6364a4e5980c393aa21668d953,
    ),
    'prime192v3': EllipticCurve(

        p=0xfffffffffffffffffffffffffffffffeffffffffffffffff,
        a=0xfffffffffffffffffffffffffffffffefffffffffffffffc,
        b=0x22123dc2395a05caa7423daeccc94760a7d462256bd56916,
    ),
    'prime239v1': EllipticCurve(

        p=0x7fffffffffffffffffffffff7fffffffffff8000000000007fffffffffff,
        a=0x7fffffffffffffffffffffff7fffffffffff8000000000007ffffffffffc,
        b=0x6b016c3bdcf18941d0d654921475ca71a9db2fb27d1d37796185c2942c0a,
    ),
    'prime239v2': EllipticCurve(

        p=0x7fffffffffffffffffffffff7fffffffffff8000000000007fffffffffff,
        a=0x7fffffffffffffffffffffff7fffffffffff8000000000007ffffffffffc,
        b=0x617fab6832576cbbfed50d99f0249c3fee58b94ba0038c7ae84c8c832f2c,
    ),
    'prime239v3': EllipticCurve(

        p=0x7fffffffffffffffffffffff7fffffffffff8000000000007fffffffffff,
        a=0x7fffffffffffffffffffffff7fffffffffff8000000000007ffffffffffc,
        b=0x255705fa2a306654b1f4cb03d6a750a30c250102d4988717d9ba15ab6d3e,
    ),
    'prime256v1': EllipticCurve(

        p=0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff,
        a=0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc,
        b=0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b,
    ),
    'secp112r1': EllipticCurve(

        p=0xdb7c2abf62e35e668076bead208b,
        a=0xdb7c2abf62e35e668076bead2088,
        b=0x659ef8ba043916eede8911702b22,
    ),
    'secp112r2': EllipticCurve(

        p=0xdb7c2abf62e35e668076bead208b,
        a=0x6127c24c05f38a0aaaf65c0ef02c,
        b=0x51def1815db5ed74fcc34c85d709,
    ),
    'secp128r1': EllipticCurve(

        p=0xfffffffdffffffffffffffffffffffff,
        a=0xfffffffdfffffffffffffffffffffffc,
        b=0xe87579c11079f43dd824993c2cee5ed3,
    ),
    'secp128r2': EllipticCurve(

        p=0xfffffffdffffffffffffffffffffffff,
        a=0xd6031998d1b3bbfebf59cc9bbff9aee1,
        b=0x5eeefca380d02919dc2c6558bb6d8a5d,
    ),
    'secp160r1': EllipticCurve(

        p=0x00ffffffffffffffffffffffffffffffff7fffffff,
        a=0x00ffffffffffffffffffffffffffffffff7ffffffc,
        b=0x001c97befc54bd7a8b65acf89f81d4d4adc565fa45,
    ),
    'secp160r2': EllipticCurve(

        p=0x00fffffffffffffffffffffffffffffffeffffac73,
        a=0x00fffffffffffffffffffffffffffffffeffffac70,
        b=0x00b4e134d3fb59eb8bab57274904664d5af50388ba,
    ),
    # This is prime192v1 with a wrong value for 
    'wrong192v1': EllipticCurve(

        p=0xfffffffffffffffffffffffffffffffeffffffffffffffff,
        a=0xfffffffffffffffffffffffffffffffefffffffffffffffc,
        b=0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1,
    ),
    # This is prime192v1 with a wrong value for p.
    'wrong192v2': EllipticCurve(

        p=0x123,
        a=0xfffffffffffffffffffffffffffffffefffffffffffffffc,
        b=0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1,
    ),
    # This is prime192v1 with a wrong value for a.
    'wrong192v3': EllipticCurve(

        p=0xfffffffffffffffffffffffffffffffeffffffffffffffff,
        a=0x123,
        b=0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1,
    ),
    # This is prime192v1 with a wrong value for b.
    'wrong192v4': EllipticCurve(

        p=0xfffffffffffffffffffffffffffffffeffffffffffffffff,
        a=0xfffffffffffffffffffffffffffffffefffffffffffffffc,
        b=0x123,
    ),
}
