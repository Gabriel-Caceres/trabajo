from random import randint


opcion = 0

est_civil = {"C":"Casado",
             "S":"Soltero",
             "V":"Viudo"}

generos = {"M":"Masculino",
           "F":"Femenino",}

dicc = {"Rut": ["219766742"],
        "Nombre": ["Gabriel Caceres"],
        "Edad": ["19"],
        "Estado Civil": [est_civil["S"]],
        "Genero": [generos["M"]],
        "fecha": ["13-06-2025"]}

meses = ["Enero 2024", "Febrero 2024", "Marzo 2024", "Abril 2024", "Mayo 2024",
         "Junio 2024", "Julio 2024", "Agosto 2024", "Septiembre 2024", "Octubre 2024", "Noviembre 2024", "Diciembre 2024"]

print(dicc)

while opcion != 4:
    try:
        opcion = int(input("Seleccione una opcion \n1.-Grabar. \n2.-Buscar. \n3.-Imprimir Certificados \n4.-Salir \nSeleccion: "))
    except Exception:
        print("ingreso invalido")

    if opcion == 1:
        print("Grabando...")
        try:
            rut = int(input("Ingrese Rut (sin punto ni guion):"))
        except Exception:
            print("Rut Invalido recuerde ingresar su rut sin puntos ni guion")
        nombre = input("Ingrese Nombre:")
        apellido = input("Ingrese el apellido paterno:")
        edad = input("Ingrese su edad:")
        estado = input("Ingrese su estado:")
        genero = input("Ingrese su genero:")
        fecha = input("Ingrese su fecha de afiliacion:")
        nombre_completo = nombre + "" + apellido
        dicc["rut"] = rut
        dicc["nombre"] = nombre_completo
        dicc["Edad"] = edad
        dicc["Estado Civil"] = est_civil[estado]
        dicc["Genero"] = generos[genero]
        dicc["fecha"] = fecha
        print(dicc)


    if opcion == 3:
        busqueda = input("Ingrese el rut del afiliado: ")
        try:
            indice = dicc["Rut"].index(busqueda)
            print("")
            print("-"*50)
            print("CERTIFICADO DE AFILIACION: ISAPRE VIDA Y SALUD")
            print("-"*50)
            for clave, valores in dicc.items():
                print(f"{clave.ljust(20)}: {valores[indice]}")
            print("-"*50)
            for mes in meses:
                print(f"{mes.ljust(20)}: $ {randint(1000,15000)}")
            print("-"*50, "\n")


        except ValueError:
            print("\n RUT no encontrado.")