A = 658974
p = 962280654317
P = (518459267012, 339109212996)

from curve_base_class import EllipticCurve

B = (-P[0] ** 3 - A * P[0] + P[1] ** 2) % p
print(B)
B = 618
E = EllipticCurve(a=A, b=B, p=p, GF=p)

# use
import chunk

solutions = [6779788669, 8284328472, 7383328479, 3276798769, 8232676583, 6932707382, 8384325810, 8472738332, 7377657169,
             3267797884, 6573788332, 8472693270, 7665714432, 8482893284, 7932716984, 3273841084, 7269328385, 6677738484,
             6968327076, 6571327785, 8384326669, 3273783284, 7273833270, 7982776584, 5832107076, 6571456967, 9187726584,
             3289798539, 7676327073, 7868327378, 3284726932, 7377657169, 9310737765, 7169328582, 7658107284, 8480584747,
             6782898084, 7946678470, 8369678582, 7378698483, 4667797747, 4947838469, 7145806582, 8446807871]
# large_string = "".join([str(ki) for ki in solutions])
for i in solutions:
    for j in range(0, 10, 2):
        print(chr(int(str(i)[j:j + 2])), end="")
