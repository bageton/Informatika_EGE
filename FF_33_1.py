def f(n):
    if n < 2:
        return 1
    if n % 2 == 0 and n > 1:
        return 2 * f(n-1)
    if n % 2 != 0 and n > 1:
        return 4 * n + f(n-2)
print(f(45))