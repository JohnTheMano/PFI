opcion=""
productos = []
cantidad=[]
opciones=[1,2,3,4,5,6,7,'salir']
volver=""
producto=[]

while opcion.lower() != ('salir') :
    while opcion not in opciones: 
        print("\n*** PROGRAMA BASICO DE STOCK ***\n")
        print("1. Agregar Producto")
        print("2. Consultar Producto")
        print("3. Modificar Stock Producto")
        print("4. Eliminar Producto")
        print("5. Listar Productos")
        print("6. Productos con bajo Stock")
        print("7. Salir\n")
   
        opcion=(input("Seleccione una opcion entre 1 y 7 o escriba 'salir' para cerrar el programa: " ))

        while opcion == "1":
            producto=(input("Ingrese nombre del producto:\t"))
            print(f'El nombre Ingresado es: {producto}\n')
            while True:
                cantidad=(input("ingrese cantidad:\t"))
                if cantidad.isdigit():
                   cantidad = int(cantidad)     
                   print(f'La cantidad ingresada es de: {cantidad} {producto}\n')
                   productos.append((producto, cantidad))
                   volver = input('Desea agregar otro producto? ')
                   if volver=="no":
                       opcion=""
                       input('Presione cualquier tecla para volver al menú principal')
                   break  
                else:
                    print('La cantidad debe ser un numero entero! intente nuevamente...')

        if opcion == "5":
            print("Lista de productos:")
            for prod, cant in productos:
                print(f"{prod}: {cant}")
            input('Presione cualquier tecla para volver al menú principal')
            opcion=""