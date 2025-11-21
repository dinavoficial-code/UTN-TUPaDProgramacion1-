import os

NOMBRE_ARCHIVO = "productos.txt"

# --- Funciones de Archivo y Persistencia ---

def crear_archivo_inicial(nombre_archivo):
    """
    Actividad 1: Crea el archivo productos.txt con tres productos iniciales si no existe.
    """
    if not os.path.exists(nombre_archivo):
        print(f"Creando archivo inicial: {nombre_archivo}...")
        try:
            # Usamos el modo 'w' para escribir el contenido inicial.
            with open(nombre_archivo, 'w') as archivo:
                # Cada línea debe tener: nombre, precio, cantidad [cite: 18]
                archivo.write("Lapicera,120.5,30\n")
                archivo.write("Cuaderno A4,350.75,15\n")
                archivo.write("Resaltador,85.0,50\n")
            print("Archivo inicial creado con éxito.")
        except Exception as e:
            print(f"Error al crear el archivo: {e}")
    else:
        # Validar situaciones comunes como evitar sobrescritura accidental [cite: 15]
        print(f"El archivo '{nombre_archivo}' ya existe. Saltando creación inicial.")


def cargar_productos_de_archivo(nombre_archivo):
    """
    Actividad 2 y 4: Lee el archivo, procesa cada línea y la carga en una 
    lista de diccionarios[cite: 22].
    """
    productos = []
    print(f"\nLeyendo productos desde '{nombre_archivo}'...")
    try:
        # Aplicar el uso de with open() para el manejo correcto de archivos [cite: 15]
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                # Procesar con .strip() y .split(",") [cite: 19]
                datos = linea.strip().split(',')
                
                if len(datos) == 3:
                    try:
                        # Cada elemento debe ser un diccionario con claves: nombre, precio, cantidad [cite: 22]
                        producto = {
                            'nombre': datos[0].strip(),
                            'precio': float(datos[1].strip()),
                            'cantidad': int(datos[2].strip())
                        }
                        productos.append(producto)
                    except ValueError:
                        print(f"Advertencia: Error al convertir datos numéricos en la línea: '{linea.strip()}'")
                
        print(f"Se cargaron {len(productos)} productos en memoria.")
        return productos
    
    except FileNotFoundError:
        # Validar situaciones comunes como errores de apertura [cite: 15]
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado. La lista de productos está vacía.")
        return []


def guardar_productos(productos, nombre_archivo):
    """
    Actividad 6: Sobrescribe el archivo productos.txt escribiendo nuevamente 
    todos los productos actualizados desde la lista[cite: 33].
    """
    print(f"\nGuardando productos actualizados en '{nombre_archivo}'...")
    try:
        # Modo 'w' para sobrescribir (reescribir) el archivo [cite: 33]
        with open(nombre_archivo, 'w') as archivo:
            for prod in productos:
                # Escribir en el formato: nombre,precio,cantidad
                linea = f"{prod['nombre']},{prod['precio']},{prod['cantidad']}\n"
                archivo.write(linea)
        print("Productos guardados con éxito.")
    except Exception as e:
        print(f"Error al intentar guardar los productos: {e}")


def agregar_producto_al_archivo(producto, nombre_archivo):
    """
    Función auxiliar para la Actividad 3, usando modo 'a' (append) para 
    añadir la nueva línea al final del archivo sin borrar el contenido existente[cite: 21].
    """
    try:
        # Modo 'a' para agregar al archivo sin borrar el contenido existente [cite: 21]
        with open(nombre_archivo, 'a') as archivo:
            linea = f"\n{producto['nombre']},{producto['precio']},{producto['cantidad']}"
            archivo.write(linea)
    except Exception as e:
        print(f"Error al añadir producto al archivo temporalmente: {e}")

# --- Funciones de Manipulación de Datos ---

def mostrar_productos(productos):
    """
    Actividad 2: Muestra los productos en el formato solicitado[cite: 19, 20].
    """
    if not productos:
        print("La lista de productos está vacía.")
        return

    print("\n--- Listado de Productos en Stock ---")
    for prod in productos:
        # Mostrar los productos en el formato: Producto: Lapicera | Precio: $120.5 | Cantidad: 30 [cite: 20]
        print(f"Producto: {prod['nombre']} | Precio: ${prod['precio']:.2f} | Cantidad: {prod['cantidad']}")
    print("--------------------------------------\n")


def agregar_producto_desde_teclado(productos):
    """
    Actividad 3: Pide al usuario que ingrese un nuevo producto y lo añade 
    a la lista en memoria y al archivo.
    """
    print("\n--- Agregar Nuevo Producto ---")
    try:
        # Pedir al usuario que ingrese un nuevo producto (nombre, precio, cantidad) [cite: 21]
        nombre = input("Ingrese nombre del producto: ").strip()
        precio = float(input("Ingrese precio (ej: 120.5): "))
        cantidad = int(input("Ingrese cantidad: "))

        if nombre and precio >= 0 and cantidad >= 0:
            nuevo_producto = {
                'nombre': nombre,
                'precio': precio,
                'cantidad': cantidad
            }
            # Añadir a la lista en memoria
            productos.append(nuevo_producto)
            
            # Agregarlo al archivo sin borrar el contenido existente [cite: 21]
            agregar_producto_al_archivo(nuevo_producto, NOMBRE_ARCHIVO)
            
            print(f"Producto '{nombre}' agregado exitosamente.")
        else:
            print("Datos inválidos. El producto no fue agregado.")
    except ValueError:
        print("Error de entrada: El precio o la cantidad deben ser números.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def buscar_producto_por_nombre(productos):
    """
    Actividad 5: Pide un nombre, busca en la lista y muestra sus datos o un mensaje.
    """
    print("\n--- Buscar Producto por Nombre ---")
    # Pedir al usuario que ingrese el nombre de un producto [cite: 30]
    nombre_buscado = input("Ingrese el nombre del producto a buscar: ").strip().lower()

    encontrado = False
    # Recorrer la lista de productos [cite: 31]
    for prod in productos:
        if prod['nombre'].lower() == nombre_buscado:
            # Si lo encuentra, mostrar todos sus datos [cite: 31]
            print("\nProducto encontrado!")
            print(f"Nombre: {prod['nombre']}")
            print(f"Precio: ${prod['precio']:.2f}")
            print(f"Cantidad en Stock: {prod['cantidad']}")
            encontrado = True
            break
    
    if not encontrado:
        # Si no existe, mostrar un mensaje de error [cite: 32]
        print(f"\nProducto '{nombre_buscado}' no encontrado en el inventario.")


# --- Función Principal ---

def menu_principal():
    """
    Ejecuta el flujo completo del programa.
    """
    # 1. Crear archivo inicial (si no existe)
    crear_archivo_inicial(NOMBRE_ARCHIVO)

    # 2. y 4. Leer, procesar y cargar la lista de diccionarios
    productos_en_memoria = cargar_productos_de_archivo(NOMBRE_ARCHIVO)
    
    while True:
        print("\n==================================")
        print("      PROGRAMA DE INVENTARIO      ")
        print("==================================")
        print("1. Mostrar todos los productos")
        print("2. Agregar nuevo producto")
        print("3. Buscar producto por nombre")
        print("4. Guardar cambios y Salir")
        print("5. Salir sin guardar")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_productos(productos_en_memoria)
        
        elif opcion == '2':
            # La función maneja la adición tanto a la lista en memoria como al archivo
            agregar_producto_desde_teclado(productos_en_memoria)
        
        elif opcion == '3':
            buscar_producto_por_nombre(productos_en_memoria)
        
        elif opcion == '4':
            # 6. Guardar los productos actualizados y salir [cite: 33]
            guardar_productos(productos_en_memoria, NOMBRE_ARCHIVO)
            print("\nPrograma finalizado. ¡Adiós!")
            break
            
        elif opcion == '5':
            print("\nSaliendo sin guardar cambios. ¡Adiós!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()