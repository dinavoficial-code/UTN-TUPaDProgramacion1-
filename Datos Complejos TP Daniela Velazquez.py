# Ejercicio 1: Añadir Frutas al Diccionario
# Diccionario inicial
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir las nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario después de la adición:")
print(precios_frutas)

# Ejercicio 2: Actualizar Precio de una Fruta
# Diccionario del Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

# Actualizar precios (la clave se sobrescribe si ya existe)
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("2) Diccionario después de la actualización:")
print(precios_frutas)

#Ejercicio 3: Crear Lista de Frutas
# Diccionario del Ejercicio 2
precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

# Convertir la vista de claves a una lista tradicional
lista_frutas = list(precios_frutas.keys())

print("3) Lista de frutas (solo claves):")
print(lista_frutas)

#Ejercicio 4: Agenda de Números Telefónicos
contactos = {}
NUM_CONTACTOS = 5

# --- Carga de 5 Contactos ---
print(f"\n4) --- Carga de {NUM_CONTACTOS} contactos ---")
for i in range(NUM_CONTACTOS):
    nombre = input(f"Ingrese el nombre del contacto {i + 1}: ")
    numero = input(f"Ingrese el número telefónico de {nombre}: ")
    contactos[nombre] = numero

print("\n--- Consulta ---")
# --- Consulta de Contacto ---
nombre_a_consultar = input("Ingrese el nombre del contacto que desea consultar: ")

# Muestra el número si la clave (nombre) existe
if nombre_a_consultar in contactos:
    numero_encontrado = contactos[nombre_a_consultar]
    print(f"El número de {nombre_a_consultar} es: {numero_encontrado}")
else:
    print(f"Error: El contacto '{nombre_a_consultar}' no se encuentra en la agenda.")


#Ejercicio 5: Análisis de Frase: Palabras Únicas y Recuento

frase = input("\n5) Ingrese una frase: ")

# Convertir a minúsculas y dividir en palabras
palabras = frase.lower().split()

# 1. Palabras Únicas (Set elimina duplicados)
palabras_unicas = set(palabras) 

# 2. Recuento de Palabras (Diccionario)
recuento = {}
for palabra in palabras:
    # Usa .get() para obtener el valor actual (o 0 si no existe) y suma 1
    recuento[palabra] = recuento.get(palabra, 0) + 1

print("\n--- Salida ---")
print(f"Palabras únicas: {palabras_unicas}")
print(f"Recuento: {recuento}")

#Ejercicio 6: Promedio de Notas de Alumnos
alumnos = {}
NUM_ALUMNOS = 3

# --- Carga de Alumnos y Notas ---
print(f"\n6) --- Carga de {NUM_ALUMNOS} alumnos y sus notas ---")
for i in range(NUM_ALUMNOS):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("Ingrese la nota 3: "))

    # Almacenar las notas como una TUPLA, ya que las notas no cambian
    alumnos[nombre] = (nota1, nota2, nota3)

print("\n--- Promedios ---")
# --- Cálculo y Muestra del Promedio ---
for nombre, notas in alumnos.items():
    # sum(notas) suma los elementos de la tupla
    # len(notas) obtiene la cantidad de elementos (3)
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio:.2f}")

#Ejercicio 7: Operaciones con Sets de Estudiantes (Parcial 1 y Parcial 2)
parcial1 = {101, 105, 110, 115, 120, 125}
parcial2 = {101, 108, 115, 122, 125, 130}

print("\n7) Resultados de Sets:")
print(f"Aprobaron Parcial 1: {parcial1}")
print(f"Aprobaron Parcial 2: {parcial2}")
print("---")

# 1. Aprobaron ambos parciales (Intersección: &)
ambos_parciales = parcial1 & parcial2
print(f"Estudiantes que aprobaron ambos parciales: {ambos_parciales}")

# 2. Aprobaron solo uno de los dos (Diferencia Simétrica: ^)
solo_uno = parcial1 ^ parcial2
print(f"Estudiantes que aprobaron solo uno de los dos: {solo_uno}")

# 3. Total de estudiantes que aprobaron al menos un parcial (Unión: |)
al_menos_uno = parcial1 | parcial2
print(f"Total de estudiantes que aprobaron al menos uno: {al_menos_uno}")

#Ejercicio 8: Gestión de Stock de Productos (Diccionario)
stock = {"Leche": 50, "Pan": 100, "Huevos": 30}
print(f"\n8) Stock inicial: {stock}")

producto = input("Ingrese el nombre del producto: ").strip()

# Consultar, Agregar unidades o Nuevo producto
if producto in stock:
    print(f"El producto '{producto}' existe. Stock actual: {stock[producto]}")
    opcion = input("Desea agregar stock? (s/n): ").lower()
    
    if opcion == 's':
        try:
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            stock[producto] += cantidad  # Agregar unidades
            print(f"Stock actualizado de {producto}: {stock[producto]}")
        except ValueError:
            print("Cantidad no válida.")

else:
    # Agregar un nuevo producto
    print(f"El producto '{producto}' no existe.")
    opcion = input("Desea agregarlo al stock? (s/n): ").lower()
    
    if opcion == 's':
        try:
            cantidad = int(input(f"Ingrese el stock inicial de {producto}: "))
            stock[producto] = cantidad
            print(f"Producto '{producto}' agregado con stock inicial de {cantidad}.")
        except ValueError:
            print("Cantidad no válida.")

print("\nStock final:")
print(stock)

#Ejercicio 9: Agenda con Claves de Tuplas
agenda = {
    ("lunes", "10:00"): "Reunión de proyecto",
    ("martes", "15:00"): "Clase de inglés",
    ("viernes", "18:30"): "Entrenamiento de fútbol"
}

# --- Consulta ---
print("\n9) --- Consulta de Agenda ---")
dia = input("Ingrese el día (ej. lunes): ").lower().strip()
hora = input("Ingrese la hora (formato HH:MM, ej. 10:00): ").strip()

# Crear la clave de tupla (inmutable) a partir de las entradas
clave_consulta = (dia, hora)

if clave_consulta in agenda:
    evento = agenda[clave_consulta]
    print(f"El evento programado para el {dia} a las {hora} es: {evento}")
else:
    print(f"No hay ninguna actividad programada para el {dia} a las {hora}.")

#Ejercicio 10: Inversión de Diccionario (Clave/Valor)
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "España": "Madrid",
    "Japón": "Tokio"
}

# Usamos una Comprensión de Diccionario para invertir los pares:
# La capital pasa a ser la clave (key) y el país pasa a ser el valor (value)
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

print("\n10) Diccionario Original (País: Capital):")
print(paises_capitales)

print("\nDiccionario Invertido (Capital: País):")
print(capitales_paises)

