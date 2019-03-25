## 0x05 一些实践

### XUSTCTF 2016
```python
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
```

算是一个非常常规的题目了。直接用自己写的轮子就可出了
```python
from curve_base_class import EllipticCurve
E = EllipticCurve(p=15424654874903, a=16546484, b=4548674875)
K = E.get_scalar_multiplication(546768,(6478678675,5636379357093))
print("XUSTCTF{%s}"%(K[0]+K[1]))
```

### TUM CTF 2016 Heicss
> 我改编了一些东西
虽然归属了椭圆曲线的tag。但是只是涉及了一些基本的操作

主要代码如下
```python
Give me the flag. This is an order!
def decode(bs):
    if len(bs) < 0x40:
        return None
    s, m = int(bs[:0x40], 16), bs[0x40:]
    if s >= q:
        print('\x1b[31mbad signature\x1b[0m')
        return None
    S = s, sqrt(pow(s, 3, q) + a * s + b, q)
    if S[1] is None:
        print('\x1b[31mbad signature:\x1b[0m {:#x}'.format(S[0]))
        return None
    h = int(SHA256.new(m.encode()).hexdigest(), 16)
    if mul(q, a, b, e, S)[0] == h:
        return m
    else:
        print('\x1b[31mbad signature:\x1b[0m ({:#x}, {:#x})'.format(*S))
```

不难发现，输入的被拆为 前64和后64到最后的两个部分，第二部分通过了 SHA256 加密生成了 h。

首先来跟踪前40位的部分

- 再输入长度超过64位，并且签名错误的情况下
- 如果 s >= q 那么会打印bad signature
- 如果 s <  q 那么会打印bad signature 以及 前半部分还有后半部分经过一个函数变换后的值。

就好像盲注一样，s已知可以通过二分`盲注`来爆破出q的值
这个不会非常困难。由于我没有环境部署这个题目，就暂且跳过了。爆出来的q是这样的

```python
q = 0x247ce416cf31bae96a1c548ef57b012a645b8bff68d3979e26aa54fc49a2c297
```

随后，记 s 为 S 的横坐标，随后会计算S的纵坐标（我姑且这么解释），纵坐标就是以下方程的一个解
$$y ^ 2 \equiv x^3 + ax +b \; mod \; q $$

当然，由于横坐标可以任意定。如果取0的话，那么y就变成了
$$ y^2 \equiv b\; mod \; q $$
这个y是可以打印出来的
```python
>> 00000000000000000000000000000000000000000000000000000000000000001
>> bad signature: (0x0, 0x18aae6ca595e2b030870f49d1aa143f4b46864eceab492f6f5a0f0efc9c90e51)

b = pow(0x18aae6ca595e2b030870f49d1aa143f4b46864eceab492f6f5a0f0efc9c90e51, 2, q)
```

这样的话，就可以计算出b的值
```python
b = 8575167449093451733644615491327478728087226005203626331099704278682109092640
```
如果尝试输入1，那么会使得y无法算出来，应该是 GCD == 1 了。

那么，如果输入的横坐标是2的话，那么y就变成了
$$ y^2 \equiv (8 + 2a + b)\; mod \; q $$
这样的话，就可以计算出a的值
```python
>> 00000000000000000000000000000000000000000000000000000000000000021
>> bad signature: (0x2, 0x20d599b9106e16f43d0c0a54e78517f5834bf15ef0206a5ce37080e4cad4f359)

a = (((pow(0x20d599b9106e16f43d0c0a54e78517f5834bf15ef0206a5ce37080e4cad4f359, 2, q) - b - 8) % q) / 2) 
# a = 5079713781418039671549386476218981709382212150018593601284925328028384622133
```
目前得出了椭圆曲线的几个参数，分别是$ a,b,p,$还有生成元$S$。

- S的横坐标是输入的x,纵坐标是将x带入曲线方程中得到的y

那么就要来观察一下签名部分了。
已知签名的内容来自于输入的字符串从第64位开始到最后，采用了 SHA256的加密得到 $h$

如果 $(h S )x== h$ 那么会返回m。我们需要的是让m为order，也就是做上面的那串字符串。

在此之前，

