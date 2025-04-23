#Trabajo Practico 5.1 - Listas Cornejo Diego 

# 1) Lista con múltiplos de 4 del 1 al 100
multiples_de_4 = list(range(4, 101, 4))
print("1)", multiples_de_4)

# 2) Mostrar el penúltimo elemento de una lista con cinco elementos
gustos = ["pizza", "helado", "cine", "playa", "música"]
print("2)", gustos[-2])  # penúltimo elemento

# 3) Lista vacía y agregar 3 palabras
lista_vacia = []
lista_vacia.append("hola")
lista_vacia.append("mundo")
lista_vacia.append("python")
print("3)", lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista "animales"
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("4)", animales)

# 5) (Solo es de análisis, no hay código)

# 6) Lista de números del 10 al 30 en saltos de 5 y mostrar los dos primeros
numeros = list(range(10, 31, 5))
print("6)", numeros[:2])

# 7) Reemplazar los valores centrales de la lista "autos"
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["fiat", "ford"]
print("7)", autos)

# 8) Lista vacía y agregar dobles
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("8)", dobles)

# 9) Manipular listas anidadas de "compras"
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")  # a)
compras[1][1] = "tallarines"  # b)
compras[0].remove("pan")  # c)
print("9)", compras)

# 10) Lista anidada con elementos específicos
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print("10)", lista_anidada)
