from functools import lru_cache

@lru_cache

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1) - 2 * g(n-1)

def g(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1) + g(n-1) + n

k = 0
for i in str(g(36)):
    k += int(i)
print(k)