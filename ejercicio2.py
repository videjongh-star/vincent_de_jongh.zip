
equipos_disponibles = 20
historial_usos = 0

print("¡bienvenido al sistema de gestion de equipos del laboratorio central de investigacion!")
while True:
    print("/n=== menu principal ====")
    print("1.-equipos disponibles")
    print("2.-asignar equipo")
    print("3.-liberar equipo")
    print("4.-historial de usos.")
    print("5.-salir.")
    opcion = input("seleccione una opcion: ")  
    if opcion =="1":
        print(f"equipos disponibes en el laboratorio: {equipos_disponibles}")
    elif opcion == "2":
        try:
            cantidad = int(input("ingrese la cantidad de equipos a asignar: "))
            if cantidad <= 0:
                print("error: la cantidad no puede ser menor o igual a 0")
            elif cantidad > equipos_disponibles:
                print("error: no hay suficientes equipos disponibles.")
            else:
                equipos_disponibles -= cantidad
                historial_usos += cantidad
                print(f"se han asignado {cantidad} equipos correctamente")
        except ValueError:
            print("error: ingrese un numero entero valido")
    elif opcion == "3":
         try:
            cantidad = int(input("ingrese la cantidad de equipos a liberar:")
            if cantidad <= 0:
              print("error la cantidad supera la capacidad maxima del laboratorio (20 equipos"))
            elif equipos_disponibles + cantidad > 20:
             print


            

      
