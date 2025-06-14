from random import randint



opcion = 0
flag = True


est_civil = {"C":"Casado",
             "S":"Soltero",
             "V":"Viudo"}

generos = {"M":"Masculino",
           "F":"Femenino",}


dicc = {"Rut": [],
        "Nombre": [],
        "Edad": [],
        "Estado Civil": [],
        "Genero": [],
        "fecha": []}


dicc = {"Rut": ["219766742"],
        "Nombre": ["Gabriel Caceres"],
        "Edad": ["19"],
        "Estado Civil": [est_civil["S"]],
        "Genero": [generos["M"]],
        "fecha": ["13-06-2025"]}

meses = ["Enero 2024", "Febrero 2024", "Marzo 2024", "Abril 2024", "Mayo 2024",
         "Junio 2024", "Julio 2024", "Agosto 2024", "Septiembre 2024", "Octubre 2024", "Noviembre 2024", "Diciembre 2024"]



while opcion != 4:
    try:
        opcion = int(input("Seleccione una opcion \n1.-Grabar. \n2.-Buscar. \n3.-Imprimir Certificados \n4.-Salir \nSeleccion: "))
    except Exception:
        print("ingreso invalido")
        continue
    
    if opcion == 1:
        print("Grabando...")
        while True:
            rut = str(input("Ingrese Rut (con puntos y guion):"))
            if rut == "":
                continue
            punto = rut.find(".")
            guion = rut.find("-")
            largo = len(rut)

            if largo == 12 and punto == 2 and guion == 10:
                break
            elif largo == 11 and punto == 1 and guion == 9:
                break
            else:
                print("el rut ingresado no es valido ")
                continue

    flag = True

    while flag:
        nombre = input("Ingrese Nombre:")

        if nombre == "":
            continue

        if any(caracter.isdigit() for caracter in nombre):
            print("Formato inválido, favor no ingresar números.")
            continue
        else:
            flag = False

                
        flag = True
        while flag:
            apellido = input("Ingrese apellido paterno:")
            if apellido == "":
                continue
            if any(caracter.isdigit() for caracter in apellido):
                print("Formato inválido, favor no ingresar números.")
                continue
            else:
                flag = False

        while True:
            try:
                edad = int(input("Ingrese su edad:"))
                if edad == "":
                    continue
                elif edad < 18:
                    print("el afiliado no cumple con la edad minima")
                    continue
                else:
                    break
            except Exception:
                print("ingreso invalido")
                
        
        while True:
            estado = input("Ingrese el estado civil (C,S,V):")
            if estado == "":
                continue
            if estado not in est_civil:
                print("Estado civil no valido recuerda usar C, S, V")
                continue
            else:
                break

        while True:
            genero = input("Ingrese su genero:")
            if genero == "":
                continue
            if genero not in generos:
                print("Su genero no existe recuerde usar M o F")    
                continue
            else:
                break    
        while True:    
            fecha = input("Ingrese su fecha de afiliacion:")
            largo_fecha = len(fecha)
            posiciones_guiones = [i for i, caracter in enumerate(fecha) if caracter == "-"]
            if posiciones_guiones == [2,5] and largo_fecha == 10:
                break
            elif not posiciones_guiones or largo_fecha != 10:
                print("recuerda ingresar la fecha en formato DD-MM-YYYY")
            else:
                print("recuerda ingresar la fecha en formato DD-MM-YYYY")
                continue  

        nombre_completo = nombre + "" + apellido
        dicc["rut"] = rut
        dicc["nombre"] = nombre_completo
        dicc["Edad"] = edad
        dicc["Estado Civil"] = est_civil[estado]
        dicc["Genero"] = generos[genero]
        dicc["fecha"] = fecha
        print("Afiliado Agregado correctamente")
        
        
        

        

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
                print(f"{mes.ljust(20)}: $ {randint(1000,1500)}")
            print("-"*50, "\n")

        except ValueError:
            print("\n *****RUT NO ENCONTRADO*****")
    
    if opcion == 4:
        print("\nSaliendo del sistema...")
        print("\tVersion SYS 2025-06 v.1")
        print("\tCopy Right")
        print("\tGabriel Barrea | Gabriel Caceres | Jean Indey")
        print("\n****CIERRE EXITOSO****")
        print("")

