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
        "fecha": "13-06-2025"}

print(dicc)

while opcion != 4:
    try:
        opcion = int(input("Seleccione una opcion \n1.-Grabar. \n2.-Buscar. \n3.-Imprimir Certificados \n4.-Salir \nSeleccion: "))
    except Exception:
        print("ingreso invalido")

    if opcion == 1:
        print("Grabando...")
        try:
            rut = (input("Ingrese Rut (sin punto ni guion):"))
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
    if opcion == 2 :
        while True :
            busqueda = input("\ningrese el rut de la persona que desea buscar Ej(11.111.111-1) : \n")
            try:
                indice = dicc["Rut"].index(busqueda)
                for clave, valores in dicc.items():
                    print(f"{clave.ljust(20)}: {valores[indice]}")
            except ValueError:
                print("\n RUT no encontrado.")
            try:    
                Respuesta = str(input("\nDesea realizar otra busqueda (SI/NO): \n")).upper()
            except ValueError:
                print("debe ingresar solo caracteres")
            if Respuesta == "NO":
                break
            else:
                print("Ingreso no valido")        


    if opcion == 3: