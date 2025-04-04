import random
from statistics import mode, median, mean

#TRABAJO PRACTICO 3 - CORNEJO DIEGO

# 1) Verificar si es mayor de edad
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad.")

# 2) Evaluar si aprobó
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Permitir solo números pares
numero = int(input("Ingrese un número par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")

# 4) Clasificación por edad
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5) Validar longitud de contraseña
contraseña = input("Ingrese una contraseña: ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

# 6) Análisis estadístico de una lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
if media > mediana > moda:
    print("Sesgo positivo.")
elif media < mediana < moda:
    print("Sesgo negativo.")
else:
    print("Sin sesgo.")

# 7) Agregar signo de exclamación si termina en vocal
frase = input("Ingrese una frase o palabra: ")
if frase[-1].lower() in "aeiou":
    print(frase + "!")
else:
    print(frase)

# 8) Transformar nombre según opción del usuario
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 para mayúsculas, 2 para minúsculas, 3 para capitalizar: "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida.")

# 9) Clasificar terremotos según la escala de Richter
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

# 10) Determinar la estación del año
hemisferio = input("Ingrese 'N' para hemisferio norte o 'S' para hemisferio sur: ").upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes: "))
if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
    estacion_norte, estacion_sur = "Invierno", "Verano"
elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
    estacion_norte, estacion_sur = "Primavera", "Otoño"
elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
    estacion_norte, estacion_sur = "Verano", "Invierno"
elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
    estacion_norte, estacion_sur = "Otoño", "Primavera"
print("Estación actual:", estacion_norte if hemisferio == 'N' else estacion_sur)