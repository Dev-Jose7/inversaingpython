helados = []
idHelado = 0

while True:
    print("\n--- CRUD Helados ---")
    print("1. Crear Helado")
    print("2. Ver Lista de Helados")
    print("3. Modificar Helado")
    print("4. Eliminar Helado")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        idHelado = idHelado+1
        nombre = input("Ingrese el nombre del helado: ")
        descripcion = input("Ingrese la descripción del helado: ")
        precio = float(input("Ingrese el precio unitario del helado: "))

        helado = {
            'ID': idHelado,
            'Nombre': nombre,
            'Descripción': descripcion,
            'Precio': precio
        }

        helados.append(helado)

        print(f"Helado '{nombre}' creado exitosamente.")

    elif opcion == '2':
        if len(helados) > 0:
            print("\n--- Lista de Helados ---")
            for helado in helados:
                print(f"ID: {helado['ID']}, Nombre: {helado['Nombre']}, Descripción: {helado['Descripción']}, Precio: {helado['Precio']}")
        else:
            print("No hay helados registrados.")

    elif opcion == '3':
        if len(helados) == 0:
            print("No hay helados registrados. Para modificar debes añadir helados")
        else:
            idModificar = int(input("Ingrese el ID del helado que desea modificar: "))
            encontrar = False

            for helado in helados:
                if helado['ID'] == idModificar:
                    print(f"Helado a modificar:\nID: {helado['ID']}, Nombre: {helado['Nombre']}, Descripción: {helado['Descripción']}, Precio: {helado['Precio']}\n")
                    encontrar = True
                    nombre = input(f"Nuevo nombre (actual: {helado['Nombre']}): ")
                    descripcion = input(f"Nueva descripción (actual: {helado['Descripción']}): ")
                    precio = input(f"Nuevo precio (actual: {helado['Precio']}): ")

                    if nombre != "": helado['Nombre'] = nombre
                    if descripcion != "": helado['Descripción'] = descripcion
                    if precio != "": helado['Precio'] = float(precio)
                    print(f"Helado modificado exitosamente.")
                    break

            if encontrar is False:
                print(f"No se encontró un helado con el ID {idModificar}.")

    elif opcion == '4':
        if len(helados) == 0:
            print("No hay helados registrados. Para eliminar debes añadir helados")
        else:
            idEliminar = int(input("Ingrese el ID del helado que desea eliminar: "))
            encontrar = False

            for helado in helados:
                if helado['ID'] == idEliminar:
                    print(f"Helado a eliminar:\nID: {helado['ID']}, Nombre: {helado['Nombre']}, Descripción: {helado['Descripción']}, Precio: {helado['Precio']}")
                    encontrar = True
                    elegir = input(f"Desea eliminar a {helado['Nombre']} S/N: ")
                    if elegir == "s" or elegir == "S":
                        helados.remove(helado)
                        print(f"Helado eliminado exitosamente.")
                    break

            if encontrar is False:
                print(f"No se encontró un helado con el ID {idEliminar}.")

    elif opcion == '5':  # Salir
        print("Hasta luego...")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción entre 1 y 5.")


