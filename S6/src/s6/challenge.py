def factorial(n):
    if n < 0:
        raise ValueError("O factorial não pode ser negativo")
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))

