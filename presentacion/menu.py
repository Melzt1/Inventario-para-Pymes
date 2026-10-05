from auxiliares import nombre_aplicacion, version_aplicacion, menu_superior

def menu_principal():
    while True:
        print(f"{nombre_aplicacion} - {version_aplicacion}")
        for clave, valor in menu_superior.items():
            print(clave, valor)

        opcion = input("Ingresa una opcion: ")

        if opcion == "1":
            pass
        elif opcion == "2":     
            pass
        elif opcion == "3":
            print("Programa Finalizado.")
            break
        else:
            print("Opcion invalida.")        

    