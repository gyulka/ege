k = 43  # после чего игра заканчивается


def f(s, m):
    if s > k:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s + 1, m - 1), f(s + 4, m - 1), f(s * 3, m - 1)]  # описываются все ходы
    return any(h) if m % 2 == 0 else all(h)
