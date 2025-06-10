# 1) Diccionario de precios de frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2) Actualización de precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3) Lista con nombres de frutas solamente
frutas = list(precios_frutas.keys())
print("Frutas:", frutas)

# 4) Agenda telefónica
agenda = {}
for _ in range(5):
    nombre = input("Ingresá el nombre del contacto: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    agenda[nombre] = numero

buscar = input("¿Qué contacto querés buscar?: ")
if buscar in agenda:
    print(f"El número de {buscar} es {agenda[buscar]}")
else:
    print(f"{buscar} no está en la agenda.")

# 5) Frase a palabras únicas y conteo
frase = input("Ingresá una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

conteo = {}
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1
print("Cantidad de veces que aparece cada palabra:", conteo)

# 6) Promedio de 3 alumnos con tuplas de 3 notas
alumnos = {}
for _ in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(float(input(f"Ingresá nota {i+1} de {nombre}: ")) for i in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {nombre}: {promedio:.2f}")

# 7) Sets de estudiantes que aprobaron parciales
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7, 8}

print("Aprobaron ambos:", parcial1 & parcial2)
print("Aprobaron solo uno:", parcial1 ^ parcial2)
print("Aprobaron al menos uno:", parcial1 | parcial2)

# 8) Gestión de stock
stock = {
    "Arroz": 10,
    "Fideos": 20,
    "Leche": 15
}

producto = input("Ingresá el nombre del producto para consultar: ")
if producto in stock:
    print(f"Stock de {producto}: {stock[producto]}")
    agregar = int(input("¿Cuántas unidades querés agregar?: "))
    stock[producto] += agregar
    print(f"Nuevo stock de {producto}: {stock[producto]}")
else:
    nuevo_stock = int(input("Producto no encontrado. ¿Cuántas unidades querés agregar?: "))
    stock[producto] = nuevo_stock
    print(f"{producto} agregado al stock con {nuevo_stock} unidades.")

# 9) Agenda de eventos con tuplas (día, hora)
agenda_eventos = {
    ('Lunes', '10:00'): 'Reunión',
    ('Martes', '14:00'): 'Clase de Inglés',
    ('Viernes', '09:00'): 'Médico'
}

dia = input("Ingresá el día para consultar: ")
hora = input("Ingresá la hora para consultar (formato HH:MM): ")
clave = (dia, hora)
if clave in agenda_eventos:
    print(f"Actividad programada: {agenda_eventos[clave]}")
else:
    print("No hay actividad programada en ese día y hora.")

# 10) Invertir diccionario de países y capitales
paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}

capitales_a_paises = {capital: pais for pais, capital in paises.items()}
print("Diccionario invertido (capital -> país):", capitales_a_paises)
