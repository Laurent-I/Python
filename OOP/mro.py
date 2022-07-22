# MRO Methods Resolution Order
class A:
    num1 = 10


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.num1)
print(D.mro())


class X:
    pass


class Y:
    pass


class Z:
    pass


class P(X, Y):
    pass


class Q(X, Z):
    pass


class R(Q, P, Z):
    pass


print(R.__mro__)
