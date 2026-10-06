from negocio.negocio_categoria import crear_categoria

def solicitar_datos_categoria():
    nombre = descripcion = ""

    while nombre == "":
        nombre = input("Ingrese el nombre de la categoria: ")
    while descripcion == "":    
        descripcion = input("Ingrese la descripion de la categoria: ")

    crear_categoria(nombre, descripcion)