# Trabajo Práctico 7: Recursividad Cornejo Diego

# 1) Factorial recursivo y mostrar del 1 al n
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def mostrar_factoriales_hasta_n(n):
    for i in range(1, n + 1):
        print(f"{i}! = {factorial(i)}")

# 2) Fibonacci recursivo y mostrar la serie
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_serie_fibonacci(n):
    for i in range(n + 1):
        print(f"F({i}) = {fibonacci(i)}")

# 3) Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

# 4) Decimal a binario recursivo
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

def convertir_a_binario(n):
    if n == 0:
        return "0"
    return decimal_a_binario(n)

# 5) Verificar palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# 6) Suma de dígitos
def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

# 7) Contar bloques en pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# 8) Contar dígito en número
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)
