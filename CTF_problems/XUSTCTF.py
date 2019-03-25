'''
已知椭圆曲线加密Ep(a,b)参数为

p = 15424654874903
a = 16546484
b = 4548674875
G(6478678675,5636379357093)

私钥为
k = 546768
求公钥K(x,y)
提示：K=kG
提交格式XUSTCTF{x+y}(注意，大括号里面是x和y加起来求和，不是用加号连接)
'''

from curve_base_class import EllipticCurve
E = EllipticCurve(p=15424654874903, a=16546484, b=4548674875)
K = E.get_scalar_multiplication(546768,(6478678675,5636379357093))
print("XUSTCTF{%s}"%(K[0]+K[1]))
