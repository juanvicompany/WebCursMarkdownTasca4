def factorial(n):
    # Caso base
    if n == 0 or n == 1:
        return 1
    
    # Llamada recursiva
    return n * factorial(n - 1)
