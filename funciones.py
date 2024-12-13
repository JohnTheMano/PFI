import sqlite3
from colorama import Fore

def contiene_numeros(texto):
    return any(char.isdigit() for char in texto)

def producto_existe_en_inventario(nombre, conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM productos WHERE nombre = ?", (nombre,))
    return cursor.fetchone()[0] > 0

def registro_producto():
    conexion = sqlite3.connect('E:\\proyecto_2024\\Prueba_Proyecto_Final_Python_Axel\\inventario.db')
    cursor = conexion.cursor()

    while True:
        try:
            nombre = input("Ingrese nombre del producto: ").strip().capitalize()
            if contiene_numeros(nombre):
                print(Fore.RED +"El nombre no puede contener números.")
            elif producto_existe_en_inventario(nombre, conexion):
                print(Fore.RED +"El producto ingresado ya existe")
            else:
                break
        except ValueError:
            print(Fore.RED +"El nombre no puede contener números")

    while True:
        try:
            descripcion = input("Ingrese la descripción del producto (máximo 30 caracteres): ")
            descripcion = descripcion[:30]  # Limitamos a 30 caracteres
            break    
        except ValueError:
            print(Fore.RED +"La descripción debe contener letras")

    while True:
        try:
            cantidad = float(input("Ingrese la cantidad del producto: ").strip().replace(',', '.'))
            cantidad = round(cantidad, 2) 
            break
        except ValueError:
            print(Fore.RED +"La cantidad ingresada es inválida, debe contener sólo números")        

    while True:
        try:
            precio = float(input("Ingrese el precio del producto: ").strip().replace(',', '.'))
            precio = round(precio, 2) 
            break
        except ValueError:
            print(Fore.RED +"El precio ingresado es inválido, debe contener sólo números")

    while True:
        try:    
            categoria = input("Ingrese la categoría del producto: ").strip().capitalize()
            if contiene_numeros(categoria):
                print(Fore.RED +"La categoría no puede contener números.")
            else:
                break
        except ValueError:
            print(Fore.RED +"La categoría debe contener sólo letras")

    # Insertamos el producto en la base de datos
    try:
        cursor.execute('''INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
                          VALUES (?, ?, ?, ?, ?)''', 
                       (nombre, descripcion, cantidad, precio, categoria))
        conexion.commit()  # Confirmamos los cambios
        print(f"Producto {nombre} registrado exitosamente.")
    except sqlite3.Error as e:
        print(Fore.RED +f"Error al registrar el producto: {e}")
    
    # Preguntar si desea registrar otro producto
    while True:
        respuesta = input(Fore.YELLOW + "¿Desea registrar otro producto? (s/n): ").strip().lower()
        if respuesta == 's':
            registro_producto()  # Llamamos de nuevo a la función para registrar otro producto
            break
        elif respuesta == 'n':
            print(Fore.GREEN +"Proceso de registro terminado.")
            break
        else:
            print(Fore.RED +"Respuesta no válida, por favor ingrese 's' para continuar o 'n' para salir.")
    
    # Cerramos la conexión a la base de datos
    conexion.close()

def eliminar_producto():
    # Mostrar opciones de búsqueda para eliminar
    print("Opciones de eliminación:")
    print("1. Eliminar por ID")
    print("2. Eliminar por Nombre")
    print("3. Eliminar por Categoría")

    while True:
        try:
            # Solicitar al usuario que elija un criterio
            opcion = int(input(Fore.YELLOW + "Seleccione el número de la opción que desea utilizar (1, 2, 3): ").strip())
            if opcion not in [1, 2, 3]:
                print(Fore.RED + "Opción no válida. Por favor elija 1, 2 o 3.")
            else:
                break
        except ValueError:
            print(Fore.RED + "Por favor, ingrese un número válido (1, 2 o 3).")

    # Conectamos a la base de datos
    conexion = sqlite3.connect('E:\\proyecto_2024\\Prueba_Proyecto_Final_Python_Axel\\inventario.db')
    cursor = conexion.cursor()

    if opcion == 1:
        # Eliminar por ID
        while True:
            try:
                producto_id = int(input(Fore.YELLOW + "Ingrese el ID del producto que desea eliminar: ").strip())
                if producto_id < 1:
                    print(Fore.RED + "El ID debe ser un número positivo mayor a cero.")
                else:
                    break
            except ValueError:
                print(Fore.RED + "Por favor, ingrese un ID válido (número entero).")

        # Verificar si el producto existe por ID
        cursor.execute("SELECT id, nombre FROM productos WHERE id = ?", (producto_id,))
        producto = cursor.fetchone()

    elif opcion == 2:
        # Eliminar por Nombre
        nombre_buscar = input(Fore.YELLOW + "Ingrese el nombre del producto que desea eliminar: ").strip().lower()
        cursor.execute("SELECT id, nombre FROM productos WHERE LOWER(nombre) LIKE ?", ('%' + nombre_buscar + '%',))
        producto = cursor.fetchone()

    elif opcion == 3:
        # Eliminar por Categoría
        categoria_buscar = input(Fore.YELLOW + "Ingrese la categoría del producto que desea eliminar: ").strip().lower()
        cursor.execute("SELECT id, nombre FROM productos WHERE LOWER(categoria) LIKE ?", ('%' + categoria_buscar + '%',))
        producto = cursor.fetchone()

    if producto:
        # Mostrar el nombre del producto que se va a eliminar
        print(Fore.CYAN + f"Producto a eliminar: {producto[1]} (ID: {producto[0]})")

        # Confirmar la eliminación
        while True:
            confirmar = input(Fore.RED + f"¿Está seguro de que desea eliminar el producto '{producto[1]}'? (S/N): ").strip().upper()
            if confirmar == "S":
                # Eliminar el producto
                cursor.execute("DELETE FROM productos WHERE id = ?", (producto[0],))
                conexion.commit()
                print(Fore.GREEN + f"Producto '{producto[1]}' con ID {producto[0]} eliminado exitosamente.")
                break
            elif confirmar == "N":
                print(Fore.RED + "Eliminación cancelada.")
                break
            else:
                print(Fore.RED + "Por favor ingrese 'S' para confirmar o 'N' para cancelar.")
    else:
        # Si no se encuentra el producto
        print(Fore.RED + "No se encontró el producto con los criterios proporcionados.")

    # Cerramos la conexión
    conexion.close()

def actualizar_producto():
    while True:
        try:
            producto_id = int(input("Ingrese el ID del producto que desea actualizar: ").strip())
            if producto_id < 1:
                print(Fore.RED + "El ID debe ser un número positivo mayor a cero.")
            else:
                break
        except ValueError:
            print(Fore.RED + "Por favor, ingrese un ID válido (número entero).")

    # Conectar a la base de datos
    conexion = sqlite3.connect('E:\\proyecto_2024\\Prueba_Proyecto_Final_Python_Axel\\inventario.db')
    cursor = conexion.cursor()

    # Verificar si el producto existe en la base de datos
    cursor.execute("SELECT id, nombre, cantidad FROM productos WHERE id = ?", (producto_id,))
    producto = cursor.fetchone()

    if producto:
        # Si el producto existe, mostramos su información actual
        print(f"Producto encontrado: {producto[1]}")
        print(f"Cantidad actual: {producto[2]}")

        while True:
            try:
                # Solicitar la nueva cantidad
                nueva_cantidad = float(input("Ingrese la nueva cantidad: ").strip().replace(',', '.'))
                if nueva_cantidad < 0:
                    print(Fore.RED + "La cantidad no puede ser negativa.")
                else:
                    break
            except ValueError:
                print(Fore.RED + "Por favor, ingrese una cantidad válida (número).")

        # Actualizar la cantidad en la base de datos
        cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (nueva_cantidad, producto_id))
        conexion.commit()
        print(Fore.GREEN + f"La cantidad del producto '{producto[1]}' se ha actualizado correctamente a {nueva_cantidad}.")
    else:
        # Si el producto no existe, mostramos un mensaje
        print(Fore.RED + f"No se encontró un producto con ID {producto_id}.")

    # Cerramos la conexión
    conexion.close()

def buscar_producto():
    
    print("Opciones de búsqueda:")
    print("1. Buscar por ID")
    print("2. Buscar por Nombre")
    print("3. Buscar por Categoría")
    
    while True:
        try:
            # Solicitar al usuario elegir el criterio de búsqueda
            opcion = int(input(Fore.YELLOW + "Elija el número de la opción que desea utilizar (1, 2, 3): ").strip())
            if opcion not in [1, 2, 3]:
                print(Fore.RED +"Opción no válida. Por favor elija 1, 2 o 3.")
            else:
                break
        except ValueError:
            print(Fore.RED +"Por favor, ingrese un número válido (1, 2 o 3).")

    # Conectar a la base de datos
    conexion = sqlite3.connect('E:\\proyecto_2024\\Prueba_Proyecto_Final_Python_Axel\\inventario.db')
    cursor = conexion.cursor()

    if opcion == 1:
        # Buscar por ID
        while True:
            try:
                producto_id = int(input(Fore.YELLOW + "Ingrese el ID del producto que desea buscar: ").strip())
                if producto_id < 1:
                    print(Fore.RED +"El ID debe ser un número positivo mayor a cero.")
                else:
                    break
            except ValueError:
                print(Fore.RED +"Por favor, ingrese un ID válido (número entero).")
        
        cursor.execute("SELECT id, nombre, descripcion, cantidad, precio, categoria FROM productos WHERE id = ?", (producto_id,))
        productos = cursor.fetchall()

    elif opcion == 2:
        # Buscar por Nombre
        nombre_buscar = input("Ingrese el nombre del producto que desea buscar: ").strip().lower()
        cursor.execute("SELECT id, nombre, descripcion, cantidad, precio, categoria FROM productos WHERE LOWER(nombre) LIKE ?", ('%' + nombre_buscar + '%',))
        productos = cursor.fetchall()

    elif opcion == 3:
        # Buscar por Categoría
        categoria_buscar = input("Ingrese la categoría del producto que desea buscar: ").strip().lower()
        cursor.execute("SELECT id, nombre, descripcion, cantidad, precio, categoria FROM productos WHERE LOWER(categoria) LIKE ?", ('%' + categoria_buscar + '%',))
        productos = cursor.fetchall()

    # Mostrar los resultados
    if productos:
        print(Fore.WHITE + "\nResultados de la búsqueda:")
        for producto in productos:
            print("-" * 60)
            print(f"ID: {producto[0]}")
            print(f"Nombre: {producto[1]}")
            print(f"Descripción: {producto[2]}")
            print(f"Cantidad: {producto[3]}")
            print(f"Precio: ${producto[4]:.2f}")
            print(f"Categoría: {producto[5]}")
            print("-" * 60)
            input(Fore.YELLOW +"<Presione cualquier tecla para continuar...>")  # Espera a que el usuario presione una tecla
    else:
        print(Fore.RED +"No se encontraron productos que coincidan con la búsqueda.")

    # Cerramos la conexión
    conexion.close()

def listado_productos():
    # Conectamos a la base de datos
    conexion = sqlite3.connect('E:\\proyecto_2024\\Prueba_Proyecto_Final_Python_Axel\\inventario.db')
    cursor = conexion.cursor()

    # Consultamos todos los productos de la tabla
    cursor.execute("SELECT id, nombre, descripcion, cantidad, precio, categoria FROM productos")
    productos = cursor.fetchall()

    # Si hay productos, los mostramos
    if productos:
        print("-" * 100)  # Línea superior
        print(Fore.CYAN + f"{'ID':<5} {'Nombre':<20} {'Descripción':<30} {'Cantidad':<10} {'Precio':<10} {'Categoría':<15}")
        print("-" * 100)  # Línea divisoria
        for producto in productos:
            # Mostrar cada producto con el formato adecuado
            print(Fore.WHITE + f"{producto[0]:<5} {producto[1]:<20} {producto[2]:<30} {producto[3]:<10} ${producto[4]:<10.2f} {producto[5]:<15}")
            print("-" * 100)  # Línea divisoria después de cada producto
            input(Fore.YELLOW +" <Presione una tecla para continuar>\n")  # Pausa después de cada producto
    else:
        print(Fore.RED +"No hay productos registrados en el inventario.")

    # Cerramos la conexión
    conexion.close()

def bajo_stock():
    # Solicitar al usuario el límite de cantidad
    while True:
        try:
            limite = float(input("Ingrese el límite de cantidad para el stock bajo: \n").strip().replace(',', '.'))
            if limite < 0:
                print(Fore.RED +"El límite debe ser un número positivo.")
            else:
                break
        except ValueError:
            print(Fore.RED +"Por favor, ingrese un valor numérico válido.")

    # Conectamos a la base de datos
    conexion = sqlite3.connect('E:\\proyecto_2024\\Prueba_Proyecto_Final_Python_Axel\\inventario.db')
    cursor = conexion.cursor()

    # Consultamos los productos con cantidad igual o inferior al límite especificado
    cursor.execute("SELECT id, nombre, descripcion, cantidad, precio, categoria FROM productos WHERE cantidad <= ?", (limite,))
    productos_bajo_stock = cursor.fetchall()

    # Si hay productos con bajo stock, los mostramos
    if productos_bajo_stock:
        print(Fore.RED +"\nProductos con bajo stock:")
        for producto in productos_bajo_stock:
            print("-" * 60)
            print(f"ID: {producto[0]}")  # ID del producto
            print(Fore.RED +f"Nombre: {producto[1]}")  # Nombre del producto
            print(f"Descripción: {producto[2]}")  # Descripción del producto
            print(Fore.RED + f"Cantidad: {producto[3]}")  # Cantidad disponible
            print(f"Precio: ${producto[4]:.2f}")  # Precio con formato
            print(f"Categoría: {producto[5]}")  # Categoría
            print("-" * 60)  # Línea para separar productos
            input(Fore.YELLOW +"<Presione cualquier tecla para continuar...>")
    else:
        print(Fore.GREEN +"No hay productos con stock bajo (igual o inferior al límite especificado).")

    # Cerramos la conexión
    conexion.close()

def mostrar_menu():
    print("\n*** PROGRAMA BASICO DE PARA INVENTARIO ***\n")
    print("1. Agregar Producto")
    print("2. Consultar Producto")
    print("3. Modificar Stock de Producto")
    print("4. Eliminar Producto")
    print("5. Listar Productos")
    print("6. Control de bajo Stock")
    print("7. Salir\n")    
    
