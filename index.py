titulo = "Bienvenido al test sobre el queso"
print(titulo + "\n" + "-"*len(titulo)+"\n")
puntuacion=0

opcion = input("Pregunta 1: Que haces cuando ves una tabla de quesos?\n"
                                "A- Salgo corriendo \n"
                                "B- Pruebo uno de los quesos o incluso varios\n"
                                "C- no puedo evitar comerlos\n")

if opcion == "a":
    puntuacion += 0
elif opcion =="b":
    puntuacion +=5
elif opcion =="c":
    puntuacion += 10
else:
    print("Las opciones disponibles son a,b y c")
    exit()

opcion = input("Pregunta 2: ¿Como te gusta la hamburguesa?\n"
                    "A- Sin queso\n"
                    "B- con queso\n"
                    "C- Pan y queso\n ")

if opcion == "a":
    puntuacion += 0
elif opcion =="b":
    puntuacion +=5
elif opcion =="c":
    puntuacion += 10
else:
    print("Las opciones disponibles son a,b y c")
    exit()

opcion = input("Pregunta 3: ¿Eres intolerante a la lactosa?\n"
                        "A- si\n"
                        "B- A veces\n"
                        "C- No\n")

if opcion == "a":
    puntuacion += 0
elif opcion =="b":
    puntuacion +=5
elif opcion =="c":
    puntuacion += 10
else:
    print("Las opciones disponibles son a,b y c")
    exit()

if puntuacion >=25:
    print("Eres fanatico del queso")
elif puntuacion >=15:
    print("Te gusta el queso")
else:
    print("No te gusta el queso")
