

while True:
    try:
        cantidad_cientificos = int(input())
        if cantidad_cientificos > 0:
            break
    except ValueError:
        pass
    print("¡Dato de investigacion invadido! ingresa un numero entero positivo para continuar el registro")

principales = 0
asistentes = 0

for _ in range(cantidad_cientificos):
    while True:
        id_cientificos = input()
        if len(id_cientificos) >= 6 and " " not in id_cientificos:
            break

    while True:
        try:
            publicaciones = int(input())
            if publicaciones >= 0:
                break
        except ValueError:
            pass
        print("¡error de registro! Ingresa un número entero positivo para el número de publicaciones.")

    if publicaciones > 10:
        principales += 1
    else:
        asistentes += 1
print(f"¡el instituto cuenta con {principales} investigadores principales y {asistentes} investigadores asistentes! ¡ciencia en marcha!")