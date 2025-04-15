#Trabajo practico 5 - Funciones Cornejo Diego

# -------------------------------------
import math

# 1. Función que imprime "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Función que saluda al usuario por su nombre
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# 3. Función que muestra información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4. Área y perímetro del círculo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 5. Convertir segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Tabla de multiplicar
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinido (división por cero)"
    return suma, resta, multiplicacion, division

# 8. Calcular IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 9. Convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 10. Calcular promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3


# Programa principal

# 1
imprimir_hola_mundo()

# 2
nombre_usuario = input("\nIngrese su nombre: ")
print(saludar_usuario(nombre_usuario))

# 3
nombre = input("\nNombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# 4
radio = float(input("\nIngrese el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"Área del círculo: {area:.2f}")
print(f"Perímetro del círculo: {perimetro:.2f}")

# 5
segundos = int(input("\nIngrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"Equivale a {horas:.2f} horas.")

# 6
numero_tabla = int(input("\nIngrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero_tabla)

# 7
a = float(input("\nIngrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
suma, resta, mult, div = operaciones_basicas(a, b)
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {mult}")
print(f"División: {div}")

# 8
peso = float(input("\nIngrese su peso (kg): "))
altura = float(input("Ingrese su altura (m): "))
imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc:.2f}")

# 9
temp_celsius = float(input("\nIngrese la temperatura en °C: "))
temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
print(f"{temp_celsius}°C equivalen a {temp_fahrenheit:.2f}°F")

# 10
n1 = float(input("\nIngrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))
promedio = calcular_promedio(n1, n2, n3)
print(f"El promedio es: {promedio:.2f}")
