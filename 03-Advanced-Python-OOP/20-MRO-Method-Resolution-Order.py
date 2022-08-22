# MRO - Method Resolution Order

"""
MRO or method resolution order is a rule that Python follows to determine when you run a method
which one to run when you have such complicated inheritance structure.

"""


"""
        A
       / \
      /   \
     B     C
      \    /
       \  /
         D
"""


class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.num)

# Check MRO
print(
    D.mro()
)  # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


# -------------------------------------------------------------------
# https://data-flair.training/blogs/python-multiple-inheritance/
# -------------------------------------------------------------------

# http://www.srikanthtechnologies.com/blog/python/mro.aspx

# Depth First Search Algorithm


class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.__mro__)
