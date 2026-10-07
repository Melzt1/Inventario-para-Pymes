from negocio.negocio_categoria import crear_categoria, actualizar_categoria, obtener_categoria

def solicitar_datos_categoria():
    nombre = descripcion = ""

    while nombre == "":
        nombre = input("Ingrese el nombre de la categoria: ")
    while descripcion == "":    
        descripcion = input("Ingrese la descripion de la categoria: ")

    crear_categoria(nombre, descripcion)

def solicitar_actualizar_categoria():
    try:
        id_categoria = int(input("Ingrese el ID de la categoria: "))
    except ValueError:
        print("El ID debe ser un numero entero.")
        return

    # Buscamos la categoria por su ID
    # Si existe, obtenemos el objeto Categoria y si no existe obtenemos None
    categoria = obtener_categoria(id_categoria)

    # Si no encontro la categoria se detiene la funcion actual
    if categoria is None:
        print("No existe una categoría con ese ID.")
        return 

    nombre = input("Ingrese el nombre de la categoria: ")   
    descripcion = input("Ingrese la descripion de la categoria: ")

    return actualizar_categoria(id_categoria, nombre, descripcion)                   