# -------------------------------------
# 1) Imprimir del 0 al 100
for i in range(101):
    print(i)

# -------------------------------------
# 2) Contar la cantidad de dígitos de un número
numero = int(input("Ingresá un número entero: "))
digitos = len(str(abs(numero)))
print("Cantidad de dígitos:", digitos)

# -------------------------------------
# 3) Sumar los números entre dos valores (excluyendo extremos)
a = int(input("Ingresá el primer número: "))
b = int(input("Ingresá el segundo número: "))
inicio = min(a, b) + 1
fin = max(a, b)
suma = 0
for i in range(inicio, fin):
    suma += i
print("Suma entre los números:", suma)

# -------------------------------------
# 4) Sumar números hasta que el usuario ingrese 0
suma = 0
while True:
    num = int(input("Ingresá un número (0 para terminar): "))
    if num == 0:
        break
    suma += num
print("Suma total:", suma)

# -------------------------------------
# 5) Juego de adivinar un número del 0 al 9
import random
secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adiviná el número (entre 0 y 9): "))
    intentos += 1
    if intento == secreto:
        print("¡Correcto! Adivinaste en", intentos, "intentos.")
        break
    else:
        print("No, intentá de nuevo.")

# -------------------------------------
# 6) Números pares del 100 al 0 (decreciente)
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# -------------------------------------
# 7) Suma desde 0 hasta un número positivo ingresado
n = int(input("Ingresá un número entero positivo: "))
suma = 0
for i in range(n + 1):
    suma += i
print("Suma total:", suma)

# -------------------------------------
# 8) Contar pares, impares, positivos y negativos en 100 números
pares = impares = positivos = negativos = 0
cantidad = 100  # Cambiá este valor para probar con menos números
for _ in range(cantidad):
    num = int(input("Ingresá un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num >= 0:
        positivos += 1
    else:
        negativos += 1
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# -------------------------------------
# 9) Calcular la media de 100 números
suma = 0
cantidad = 100  # Podés usar un valor menor para probar
for _ in range(cantidad):
    num = int(input("Ingresá un número: "))
    suma += num
media = suma / cantidad
print("Media:", media)

# -------------------------------------
# 10) Invertir los dígitos de un número
numero = int(input("Ingresá un número: "))
numero_invertido = int(str(abs(numero))[::-1])
if numero < 0:
    numero_invertido *= -1
print("Número invertido:", numero_invertido)
