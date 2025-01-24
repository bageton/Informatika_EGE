from functools import lru_cache

@lru_cache

def F(n):
    s = []
    s.append(2 * n + 1)
    if n > 1:
        s.append(3 * n - 8)
        s += F(n - 1)
        s += F(n - 4)
    return s

for i in range(-10000, 10000):
    if sum(F(i)) > 5000000:
        print(i, sum(F(i)))
        break
