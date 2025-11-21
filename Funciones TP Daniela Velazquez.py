# ===============================================
# Bloque 1: Funciones Básicas (Actividades 1-3)
# ===============================================

# 1. Función sin parámetros que imprime un mensaje
def imprimir_hola_mundo():
    """Imprime el mensaje 'Hola Mundo!'"""
    print("Hola Mundo!")

# 2. Función que recibe un parámetro y devuelve un saludo
def saludar_usuario(nombre):
    """Recibe un nombre y devuelve un saludo personalizado."""
    return f"Hola {nombre}!"

# 3. Función que recibe múltiples parámetros e imprime información
def informacion_personal(nombre, apellido, edad, residencia):
    """Recibe datos personales e imprime una presentación."""
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# --- Programa Principal (Llamadas a funciones) ---

print("--- Actividad 1 ---")
imprimir_hola_mundo()

print("\n--- Actividad 2 ---")
# Solicitar el nombre al usuario
nombre_usuario = input("Por favor, ingresa tu nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)

print("\n--- Actividad 3 ---")
# Pedir los datos al usuario
nombre_p = input("Ingresa tu nombre: ")
apellido_p = input("Ingresa tu apellido: ")
edad_p = input("Ingresa tu edad: ")
residencia_p = input("Ingresa tu residencia: ")
# Llamar a la función con los valores ingresados
informacion_personal(nombre_p, apellido_p, edad_p, residencia_p)

# ===============================================
# Bloque 2: Cálculos y Estructuras (Actividades 4-6)
# ===============================================
import math # Necesario para usar math.pi

# 4. Función para calcular el área del círculo
def calcular_area_circulo(radio):
    """Recibe el radio y devuelve el área del círculo (π * radio^2)."""
    return math.pi * (radio ** 2)

# 4. Función para calcular el perímetro del círculo
def calcular_perimetro_circulo(radio):
    """Recibe el radio y devuelve el perímetro del círculo (2 * π * radio)."""
    return 2 * math.pi * radio

# 5. Función de conversión de segundos a horas
def segundos_a_horas(segundos):
    """Recibe segundos y devuelve la cantidad de horas correspondientes."""
    return segundos / 3600

# 6. Función para imprimir la tabla de multiplicar
def tabla_multiplicar(numero):
    """Recibe un número e imprime su tabla de multiplicar del 1 al 10."""
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# --- Programa Principal (Llamadas a funciones) ---

print("\n--- Actividad 4 ---")
try:
    radio = float(input("Ingresa el radio del círculo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"Área del círculo: {area:.2f}")
    print(f"Perímetro del círculo: {perimetro:.2f}")
except ValueError:
    print("Error: El radio debe ser un número.")

print("\n--- Actividad 5 ---")
try:
    segundos_input = int(input("Ingresa una cantidad de segundos: "))
    horas = segundos_a_horas(segundos_input)
    print(f"{segundos_input} segundos equivalen a {horas:.4f} horas.")
except ValueError:
    print("Error: La cantidad de segundos debe ser un número entero.")

print("\n--- Actividad 6 ---")
try:
    num_multiplicar = int(input("Ingresa un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(num_multiplicar)
except ValueError:
    print("Error: El número debe ser un entero.")

    # ===============================================
# Bloque 3: Múltiples Retornos y Cálculos (Actividades 7-10)
# ===============================================

# 7. Función que devuelve una tupla con operaciones básicas
def operaciones_basicas(a, b):
    """Recibe dos números y devuelve una tupla con suma, resta, multiplicación y división."""
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    # División segura
    division = a / b if b != 0 else "Indefinida (División por cero)"
    return (suma, resta, multiplicacion, division)

# 8. Función para calcular el Índice de Masa Corporal (IMC)
def calcular_imc(peso, altura):
    """Recibe peso (kg) y altura (metros) y devuelve el IMC (peso / altura^2)."""
    return peso / (altura ** 2)

# 9. Función de conversión de Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    """Recibe una temperatura en Celsius y devuelve su equivalente en Fahrenheit."""
    return (celsius * 9/5) + 32

# 10. Función para calcular el promedio
def calcular_promedio(a, b, c):
    """Recibe tres números y devuelve su promedio."""
    return (a + b + c) / 3

# --- Programa Principal (Llamadas a funciones) ---

print("\n--- Actividad 7 ---")
try:
    num1_op = float(input("Ingresa el primer número para operaciones: "))
    num2_op = float(input("Ingresa el segundo número para operaciones: "))
    # Desempaquetar la tupla devuelta
    suma, resta, multi, div = operaciones_basicas(num1_op, num2_op)
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multi}")
    print(f"División: {div}")
except ValueError:
    print("Error: Ambos valores deben ser números.")

print("\n--- Actividad 8 ---")
try:
    peso_kg = float(input("Ingresa tu peso en kilogramos (ej: 70.5): "))
    altura_m = float(input("Ingresa tu altura en metros (ej: 1.75): "))
    imc = calcular_imc(peso_kg, altura_m)
    print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")
except ValueError:
    print("Error: El peso y la altura deben ser números.")
except ZeroDivisionError:
    print("Error: La altura no puede ser cero.")

print("\n--- Actividad 9 ---")
try:
    temp_celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
    print(f"{temp_celsius}°C equivalen a {temp_fahrenheit:.2f}°F.")
except ValueError:
    print("Error: La temperatura debe ser un número.")

print("\n--- Actividad 10 ---")
try:
    num_a = float(input("Ingresa el primer número: "))
    num_b = float(input("Ingresa el segundo número: "))
    num_c = float(input("Ingresa el tercer número: "))
    promedio = calcular_promedio(num_a, num_b, num_c)
    print(f"El promedio de los tres números es: {promedio:.2f}")
except ValueError:
    print("Error: Todos los valores deben ser números.")
    