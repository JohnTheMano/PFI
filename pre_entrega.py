opcion=""
productos = []  # Lista para almacenar productos y sus cantidades
opciones=[1,2,3,4,5,6,7,'salir']    # Opciones del menú
volver=""   # Variable para decidir si volver a agregar productos


while opcion.lower() != ('salir') : # Bucle principal que se ejecuta hasta que el usuario escribe 'salir'
    while opcion not in opciones:   # Bucle para mostrar el menú hasta que el usuario seleccione una de las opciones 
        print("\n*** PROGRAMA BASICO DE STOCK ***\n")
        print("1. Agregar Producto")
        print("2. Consultar Producto")
        print("3. Modificar Stock Producto")
        print("4. Eliminar Producto")
        print("5. Listar Productos")
        print("6. Productos con bajo Stock")
        print("7. Salir\n")
   
        opcion=(input("Seleccione una opcion entre 1 y 7 o escriba 'salir' para cerrar el programa: " )).lower()

        # Opción para agregar cada producto
        while opcion == "1":
            producto=(input("\nIngrese nombre del producto: ")).capitalize()
            print(f'El nombre Ingresado es: {producto}\n')
            while True: # Validación del input de "cantidad" como un número entero
                cantidad=(input("ingrese cantidad: "))
                if cantidad.isdigit():
                   cantidad = int(cantidad)     
                   print(f'La cantidad ingresada es de: {cantidad} {producto}\n')
                   productos.append((producto, cantidad))
                   volver = input('Desea agregar otro producto? si/no: ').lower()
                   if volver=="no": # Al no querer agregar más productos, seteamos la opcion en "" y volvemos al menu principal con el "break"
                       opcion=""
                       input('\n<Presione cualquier tecla para volver al menú principal>')
                   break  
                else:
                    print('La cantidad debe ser un numero entero! intente nuevamente...')

        # Opción para consultar un producto
        if opcion == "2":
            if productos == []:
                    print("\n<No se puede realizar una búsqueda - La lista de productos está VACÍA>")
                    input('\n<Presione cualquier tecla para volver al menú principal>')

            else:        
                producto_buscado = input("Ingrese el nombre del producto que desea buscar: ").capitalize()
                encontrado = False
                for producto in productos:
                    if producto_buscado == producto[0]:
                        print(f'\nEl stock del producto {producto[0]} es: {producto[1]}')
                        encontrado = True
                        input('\n<Presione cualquier tecla para volver al menú principal>')
                        break

                if not encontrado:  # Si no se encontró el producto
                    print("\n<Producto no encontrado>")
                    input('\n<Presione cualquier tecla para volver al menú principal>')
                    
                          
        # Opción para listar todos los productos
        if opcion == "5":
            print("\n*** Lista de productos ***")
            if productos == []: #Ejecuta el "for" sólo si la lista no está vacía
                    print("\n<La lista de productos está VACÍA>")
            else:
                for producto, cantidad in productos:               
                    print(f"{producto}: {cantidad}")
            input('\n<Presione cualquier tecla para volver al menú principal>')
            opcion=""
