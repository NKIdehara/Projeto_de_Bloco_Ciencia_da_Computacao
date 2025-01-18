import time

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_memoria(n, memoria):
    if n in memoria:
        return memoria[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    resultado = fibonacci_memoria(n - 1, memoria) + fibonacci_memoria(n - 2, memoria)
    memoria[n] = resultado
    return resultado


for n in range(41):
    t_1 = time.time()
    f1 = fibonacci(n)
    t_2 = time.time()
    print(f"n = {n}\tfibonacci({n}) = {f1}\ttempo = {(t_2 - t_1):.2f}", end="")
    f2 = fibonacci_memoria(n, {})
    t_3 = time.time()
    print(f", fibonacci com memória = {f2}\ttempo = {(t_3 - t_2):.2f}")