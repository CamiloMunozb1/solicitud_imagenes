from funciones.busqueda_imagenes import BuscadorImagenes

while True:
    print("""
        Bienvenido a la solicitud de imagenes:
            1. Buscar imagenes.
            2. Gestion de imagenes.
            3. Salir
        """)
    try:
        usuario = str(input("Ingresa la opcion que desees: ")).strip()
        if not usuario:
            print("El campo debe estar completo.")
            break
        elif usuario == "1":
            imagen = BuscadorImagenes()
            imagen.busqueda_imagen()
        elif usuario == "2":
            print("Opcion a desarrollar.")
        elif usuario == "3":
            print("Gracias por usar y solicitar tus imagenes favoritas.")
            break
        input("\nPresiona enter para continuar...")
    except TypeError:
        print("Error de digitacion, volver a intentar.")
    except Exception as error:
        print(f"Error en el programa : {error}.")