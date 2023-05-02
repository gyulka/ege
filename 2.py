from itertools import product, permutations


def f(x, y, z, w):
    return ((not y) and (x <= ((not z) == w))) or z


for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = [(0, a1, 0, 0), (a2, 0, 1, 0), (a3, 0, 0, a4)]
    if len(table) != len(set(table)):
        continue
    for r in permutations('xyzw'):
        if [f(**dict(zip(r, i))) for i in table] == [0, 0, 0]:
            print(r)
