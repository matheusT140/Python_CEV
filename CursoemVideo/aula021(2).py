def fatorial(n):
    if n == 1:
        return n
    else:
        n *= fatorial(n - 1)
        return n

n = 5
print(fatorial(n))
