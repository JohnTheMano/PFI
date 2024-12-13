import sqlite3
from funciones import *
from colorama import Fore, Style, init

# Inicializamos Colorama (opcional, especialmente útil en Windows)
init(autoreset=True)

def inicializar_bbdd():
    conexion = sqlite3.connect('E:\\proyecto_2024\\Prueba_Proyecto_Final_Python_Axel\\inventario.db')
    cursor = conexion.cursor()

    # Para crear tabla:
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            CÓDIGO TEXT UNIQUE,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL CHECK (cantidad >= 0),
            precio REAL NOT NULL CHECK (precio > 0),
            categoria TEXT)            
    ''')

    conexion.commit()
    conexion.close()

inicializar_bbdd()

while True: 
    print(Fore.CYAN + Style.BRIGHT + "\n------- Menú de opciones -------")  # Título llamativo con fondo y texto brillante
    mostrar_menu()

    try:
        opcion = int(input(Fore.MAGENTA + Style.BRIGHT + 'Ingrese una opción entre 1-7: '))  # Entrada en magenta brillante

        if opcion < 1 or opcion > 7:
            print(Fore.RED + Style.BRIGHT + ' \nLa opción debe estar entre 1 y 7. Por favor, intente nuevamente.')  # Mensaje de error en rojo brillante
            continue  # Volver al inicio del ciclo sin ejecutar el resto del código si la opción es inválida

        if opcion == 7:
            input(Fore.GREEN + Style.BRIGHT + '\nPresione una tecla para salir del programa')  # Salida en verde brillante
            print(Fore.GREEN + "\n¡Hasta Pronto!\n")
            break  # Salir del ciclo si la opción es 7
        
        elif opcion == 1:
            print(Fore.YELLOW + Style.BRIGHT + "\n Registro de producto seleccionado...")
            registro_producto()
        elif opcion == 2:
            print(Fore.YELLOW + Style.BRIGHT + "\n Búsqueda de producto seleccionada...")
            buscar_producto()
        elif opcion == 3:
            print(Fore.YELLOW + Style.BRIGHT + "\n Actualización de producto seleccionada...")
            actualizar_producto()
        elif opcion == 4:
            print(Fore.YELLOW + Style.BRIGHT + "\n Eliminación de producto seleccionada...")
            eliminar_producto()
        elif opcion == 5:
            print(Fore.YELLOW + Style.BRIGHT + "\n Listado de productos seleccionado...")
            listado_productos()
        elif opcion == 6:
            print(Fore.YELLOW + Style.BRIGHT + "\n Revisión de bajo stock seleccionada...")
            bajo_stock()

    except ValueError:
        print(Fore.RED + Style.BRIGHT + '\n No ha ingresado un número entre 1 y 7, intente nuevamente...')  # Mensaje de error en rojo brillante


