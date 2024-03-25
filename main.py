def test():
    a = 'bool'
    b = 121
    print(a, b)


test()


def test2(a, b, *, c):
    print(a, b, c)


test2(346, 'iwan', c=187)
