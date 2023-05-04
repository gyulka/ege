# № 7681 (Уровень: Базовый) с компегэ

import sys
from functools import lru_cache


@lru_cache()
def f(n):
    if n <= 4:
        return 1
    return f(n - 1) + f(n - 3) + g(n - 2)


@lru_cache()
def g(n):
    if n > 1500:
        return 5
    return g(n + 1) + g(n + 2) + 1


sys.setrecursionlimit(3000)
print(g(100))
print(f(120))
print(f(2*120))
print(f(4*120))
print(f(8*120))



print((f(1200) + g(100)) % 10000)
