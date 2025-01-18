def fatoria(n):
    if n == 1:
        return 1
    return n * fatoria(n - 1)

for n in range(1, 100):
    print(f"n = {n}, fatorial({n}) = {fatoria(n)}")