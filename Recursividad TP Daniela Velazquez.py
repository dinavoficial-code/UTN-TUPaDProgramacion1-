import sys
# Aumentar el límite de recursión para números grandes, útil para ejercicios como el de Fibonacci
# ¡Asegúrate de entender por qué esto podría ser necesario y sus implicaciones!
sys.setrecursionlimit(2000)

## ----------------------------------------------------
## 1) Factorial
## ----------------------------------------------------

def factorial_recursivo(n):
    """
    Calcula el factorial de un número n de forma recursiva.
    n! = n * (n-1)!
    Caso Base: 0! = 1 y 1! = 1
    """
    if n < 0:
        return "Error: El factorial solo está definido para números no negativos."
    if n == 0 or n == 1:
        return 1  # Caso Base
    else:
        # Caso Recursivo: n * factorial_recursivo(n - 1)
        return n * factorial_recursivo(n - 1)

def ejercicio_1():
    """
    Pide un número al usuario y muestra el factorial de todos los números entre 1 y ese número.
    """
    print("\n--- EJERCICIO 1: Factorial ---")
    try:
        max_num = int(input("Ingresa un número entero positivo para calcular factoriales hasta él: "))
        if max_num < 1:
            print("Por favor, ingresa un número entero positivo.")
            return

        print(f"\nFactoriales de 1 hasta {max_num}:")
        for i in range(1, max_num + 1):
            resultado = factorial_recursivo(i)
            print(f"El factorial de {i} ({i}!) es: {resultado}")

    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")

## ----------------------------------------------------
## 2) Serie de Fibonacci
## ----------------------------------------------------

def fibonacci_recursivo(posicion):
    """
    Calcula el valor de la serie de Fibonacci en la posición indicada de forma recursiva.
    F(n) = F(n-1) + F(n-2)
    Caso Base: F(0) = 0, F(1) = 1 (o F(1)=1, F(2)=1 dependiendo de si se empieza en 0 o 1)
    """
    if posicion < 0:
        return -1 # Indicador de error o posición inválida
    if posicion == 0:
        return 0  # Caso Base 1
    elif posicion == 1:
        return 1  # Caso Base 2
    else:
        # Caso Recursivo: La suma de los dos valores anteriores
        return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)

def ejercicio_2():
    """
    Pide una posición al usuario y muestra la serie de Fibonacci completa hasta esa posición.
    """
    print("\n--- EJERCICIO 2: Serie de Fibonacci ---")
    try:
        max_posicion = int(input("Ingresa la posición máxima (N) de Fibonacci que quieres ver (ej: 8): "))
        if max_posicion < 0:
            print("La posición debe ser un número entero no negativo.")
            return

        serie = []
        for i in range(max_posicion + 1):
            valor = fibonacci_recursivo(i)
            serie.append(str(valor))

        print(f"\nSerie de Fibonacci hasta la posición {max_posicion}:")
        print(" -> ".join(serie))

    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")

## ----------------------------------------------------
## 3) Potencia de un Número
## ----------------------------------------------------

def potencia_recursiva(base, exponente):
    """
    Calcula la potencia de un número base elevado a un exponente de forma recursiva.
    Fórmula: n^m = n * n^(m-1) [cite: 17]
    Caso Base: n^0 = 1
    """
    if exponente == 0:
        return 1 # Caso Base: Cualquier número elevado a 0 es 1
    elif exponente < 0:
        # Manejo de exponentes negativos (Opcional, pero buena práctica)
        # n^(-m) = 1 / n^m
        return 1 / potencia_recursiva(base, -exponente)
    else:
        # Caso Recursivo: base * potencia_recursiva(base, exponente - 1)
        return base * potencia_recursiva(base, exponente - 1)

def ejercicio_3():
    """
    Prueba la función de potencia con un algoritmo general.
    """
    print("\n--- EJERCICIO 3: Potencia de un Número ---")
    try:
        base = float(input("Ingresa la base (n): "))
        exponente = int(input("Ingresa el exponente (m): "))

        resultado = potencia_recursiva(base, exponente)
        print(f"\nEl resultado de {base} elevado a la {exponente} es: {resultado}")

    except ValueError:
        print("Entrada inválida.")
    except RecursionError:
        print("Error de recursión (límite alcanzado).")

## ----------------------------------------------------
## 4) Decimal a Binario
## ----------------------------------------------------

def decimal_a_binario_recursivo(n):
    """
    Convierte un número entero positivo en base decimal a su representación en binario
    como una cadena de texto, usando el método de división por 2 y recursión. [cite: 19, 20]
    Caso Base: Si el cociente llega a 0. [cite: 23]
    """
    if n == 0:
        return "0"
    
    # La parte recursiva debe construir la cadena de restos LEÍDOS DE ABAJO HACIA ARRIBA 
    
    # Caso Base: n // 2 == 0 (solo queda un bit)
    if n // 2 == 0:
        # Si el número es 1, retorna "1"
        return str(n % 2) 
    else:
        # Caso Recursivo: Llamada con el cociente (n // 2) y se concatena el resto (n % 2)
        # La llamada recursiva (que obtiene los restos "superiores") debe ir PRIMERO
        # para que los restos se concatenen en el orden correcto (de abajo hacia arriba)
        
        # resto = n % 2
        # nuevo_cociente = n // 2
        # return decimal_a_binario_recursivo(nuevo_cociente) + str(resto)

        return decimal_a_binario_recursivo(n // 2) + str(n % 2)

def ejercicio_4():
    """
    Prueba la función de conversión de decimal a binario.
    """
    print("\n--- EJERCICIO 4: Decimal a Binario ---")
    try:
        decimal = int(input("Ingresa un número entero positivo en base decimal (ej: 10): "))
        if decimal < 0:
            print("Por favor, ingresa un número entero positivo.")
            return

        if decimal == 0:
            binario = "0"
        else:
            binario = decimal_a_binario_recursivo(decimal)

        print(f"\nEl número decimal {decimal} en binario es: \"{binario}\"")
        # Ejemplo de la guía para verificar: 10 -> 1010 [cite: 33, 38]
        # print(f"Ejemplo de verificación (10): {decimal_a_binario_recursivo(10)}")

    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")


## ----------------------------------------------------
## 5) Palíndromo
## ----------------------------------------------------

def es_palindromo_recursivo(palabra):
    """
    Implementa una función recursiva para verificar si una cadena de texto es un palíndromo. [cite: 39]
    Restricciones: No usar [::-1] ni reversed(). [cite: 42]
    Caso Base 1: Una cadena vacía ("") es un palíndromo (True).
    Caso Base 2: Una cadena de un solo carácter es un palíndromo (True).
    """
    
    # Caso Base 1 y 2: Cadena vacía o de un solo carácter
    if len(palabra) <= 1:
        return True

    # Caso Recursivo:
    # 1. Comprobar si el primer y el último carácter son iguales.
    # 2. Si son iguales, se llama recursivamente a la función con el subsegmento
    #    que excluye el primer y el último carácter (palabra[1:-1]).
    # 3. Si no son iguales, inmediatamente se devuelve False.
    
    if palabra[0].lower() == palabra[-1].lower():
        return es_palindromo_recursivo(palabra[1:-1]) # Llamada con la subcadena
    else:
        return False

def ejercicio_5():
    """
    Prueba la función es_palindromo_recursivo.
    """
    print("\n--- EJERCICIO 5: Palíndromo ---")
    
    # Nota: El ejercicio pide una cadena SIN ESPACIOS NI TILDES [cite: 39]
    cadena_original = input("Ingresa una palabra (sin espacios ni tildes): ")
    cadena = cadena_original.lower() # Normalizar a minúsculas para la verificación

    resultado = es_palindromo_recursivo(cadena)
    
    if resultado:
        print(f"'{cadena_original}' es un palíndromo.")
    else:
        print(f"'{cadena_original}' NO es un palíndromo.")

## ----------------------------------------------------
## 6) Suma de Dígitos
## ----------------------------------------------------

def suma_digitos_recursiva(n):
    """
    Calcula la suma de los dígitos de un número entero positivo de forma recursiva. [cite: 43]
    Restricción: Usar operaciones matemáticas (%, //) y recursión. No convertir a string. [cite: 45, 46]
    
    Descomposición:
    * Último dígito: n % 10
    * Resto del número: n // 10
    
    Caso Base: Si n < 10 (es un solo dígito), la suma es el propio n.
    """
    if n < 0:
        n = abs(n) # Aseguramos trabajar con el valor absoluto, aunque el enunciado pide positivo.

    if n < 10:
        return n  # Caso Base: Si es un solo dígito (ej: 9) [cite: 49, 50]
    else:
        # Caso Recursivo: (Último dígito) + suma_digitos_recursiva(Resto del número)
        # Ejemplo: 1234 -> 4 + suma_digitos_recursiva(123)
        return (n % 10) + suma_digitos_recursiva(n // 10)

def ejercicio_6():
    """
    Prueba la función suma_digitos_recursiva.
    """
    print("\n--- EJERCICIO 6: Suma de Dígitos ---")
    try:
        numero = int(input("Ingresa un número entero positivo (ej: 1234): "))
        if numero < 0:
            print("Por favor, ingresa un número entero positivo.")
            return

        resultado = suma_digitos_recursiva(numero)
        print(f"\nLa suma de los dígitos de {numero} es: {resultado}")
        
        # Ejemplos de verificación:
        # print(f"Suma de dígitos de 1234: {suma_digitos_recursiva(1234)}") # -> 10 [cite: 48]
        # print(f"Suma de dígitos de 305: {suma_digitos_recursiva(305)}")   # -> 8 [cite: 51]

    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")

## ----------------------------------------------------
## 7) Contar Bloques de una Pirámide
## ----------------------------------------------------

def contar_bloques_recursivo(n):
    """
    Calcula el total de bloques necesarios para construir una pirámide,
    donde el nivel más bajo tiene 'n' bloques y cada nivel superior tiene uno menos. [cite: 52, 53]
    Esto es equivalente a la suma de los primeros n números naturales (n + (n-1) + ... + 1).
    Caso Base: n=1, total de bloques es 1. [cite: 55]
    """
    if n == 1:
        return 1 # Caso Base: El último nivel (o el primero si n=1) tiene 1 bloque.
    
    if n <= 0:
        return 0 # Si se ingresa 0 o menos, no hay bloques.

    # Caso Recursivo: El número de bloques del nivel actual (n) + 
    #                el número de bloques de la pirámide reducida (contar_bloques_recursivo(n - 1))
    # Ejemplo: contar_bloques(4) = 4 + contar_bloques(3)
    return n + contar_bloques_recursivo(n - 1)

def ejercicio_7():
    """
    Prueba la función contar_bloques_recursivo.
    """
    print("\n--- EJERCICIO 7: Contar Bloques de una Pirámide ---")
    try:
        n = int(input("Ingresa el número de bloques en el nivel más bajo (n, ej: 4): "))
        if n < 1:
            print("El número de bloques debe ser al menos 1.")
            return

        resultado = contar_bloques_recursivo(n)
        print(f"\nEl total de bloques necesarios para la pirámide de base {n} es: {resultado}")
        
        # Ejemplos de verificación:
        # print(f"contar_bloques(1): {contar_bloques_recursivo(1)}") # -> 1 [cite: 55]
        # print(f"contar_bloques(2): {contar_bloques_recursivo(2)}") # -> 3 [cite: 57]
        # print(f"contar_bloques(4): {contar_bloques_recursivo(4)}") # -> 10 [cite: 58]

    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")

## ----------------------------------------------------
## 8) Contar Dígito
## ----------------------------------------------------

def contar_digito_recursivo(numero, digito):
    """
    Cuenta cuántas veces aparece un dígito (0-9) dentro de un número entero positivo. [cite: 60]
    
    Descomposición (similar a suma_digitos):
    * Último dígito del número: numero % 10
    * Resto del número: numero // 10
    
    Caso Base: Si el número llega a 0, la cuenta es 0.
    """
    if numero == 0:
        return 0 # Caso Base: No hay más dígitos para revisar.

    # Obtener el último dígito del número actual
    ultimo_digito = numero % 10

    # Comprobar si el último dígito es igual al dígito buscado (digito)
    contador = 1 if ultimo_digito == digito else 0

    # Caso Recursivo: La cuenta actual (0 o 1) + la cuenta recursiva del resto del número (numero // 10)
    return contador + contar_digito_recursivo(numero // 10, digito)

def ejercicio_8():
    """
    Prueba la función contar_digito_recursivo.
    """
    print("\n--- EJERCICIO 8: Contar Dígito ---")
    try:
        numero = int(input("Ingresa el número entero positivo (ej: 12233421): "))
        digito = int(input("Ingresa el dígito a contar (0-9, ej: 2): "))

        if numero < 0 or not (0 <= digito <= 9):
            print("Asegúrate de que el número sea positivo y el dígito esté entre 0 y 9.")
            return

        # Caso especial si el número es 0, ya que el caso base de la función es para número=0
        if numero == 0 and digito == 0:
            resultado = 1
        elif numero == 0:
            resultado = 0
        else:
            resultado = contar_digito_recursivo(numero, digito)

        print(f"\nEl dígito {digito} aparece {resultado} veces en el número {numero}.")
        
        # Ejemplos de verificación:
        # print(f"Contar 2 en 12233421: {contar_digito_recursivo(12233421, 2)}") # -> 3 [cite: 63]
        # print(f"Contar 7 en 123456: {contar_digito_recursivo(123456, 7)}")     # -> 0 [cite: 70]

    except ValueError:
        print("Entrada inválida. Por favor, ingresa números enteros.")

## ----------------------------------------------------
## Programa Principal para Ejecutar los Ejercicios
## ----------------------------------------------------

def main():
    print("==================================================")
    print("         TP - Aplicación de la Recursividad       ")
    print("==================================================")

    while True:
        print("\nSelecciona el ejercicio a ejecutar (1-8) o 's' para salir:")
        opcion = input("Opción: ").strip().lower()

        if opcion == 's':
            print("\nSaliendo del programa. ¡Buen trabajo!")
            break

        if opcion.isdigit():
            ejercicio = int(opcion)
            if ejercicio == 1:
                ejercicio_1()
            elif ejercicio == 2:
                ejercicio_2()
            elif ejercicio == 3:
                ejercicio_3()
            elif ejercicio == 4:
                ejercicio_4()
            elif ejercicio == 5:
                ejercicio_5()
            elif ejercicio == 6:
                ejercicio_6()
            elif ejercicio == 7:
                ejercicio_7()
            elif ejercicio == 8:
                ejercicio_8()
            else:
                print("Opción no válida. Por favor, selecciona un número entre 1 y 8.")
        else:
            print("Opción no válida. Por favor, ingresa un número o 's'.")

if __name__ == "__main__":
    main()