from random import randint

vida_pikachu = 80
vida_squirtle = 90

print("Bienvenido a la batalla pokemon")
while vida_pikachu > 0 and vida_squirtle > 0 :

    print("Vida de Pikachu {}".format(vida_pikachu))
    print("ataque de pikachu...Preparate")
    ataque_pikachu = randint(1,2)
    if ataque_pikachu == 1:
        print("Pikachu ha usado Bola Voltio")
        vida_squirtle -= 10
    else :
        print("Pikachu ha usado onda trueno")
        vida_squirtle -= 11
    
    input("Enter para continuar....")
    print("Vida de Squirtle {}".format(vida_squirtle))
    print("Turno de squirtle... TU TURNO DE ATACAR")
    ataque_squirtle = input("Cual ataque deseas hacer [p] Placaje, [a] Pistola de agua y [b] Burbuja")
    if ataque_squirtle == "p" :
        print("Ataque placaje")
        vida_pikachu -= 10
    elif ataque_squirtle == "a" :
        print("Ataque pistola de agua")
        vida_pikachu -= 12
    elif ataque_squirtle == "b" :
        print("Ataque burbuja")
        vida_pikachu -= 9
    else:
        print("Fallaste")

if vida_pikachu > vida_squirtle :
    print("Pikachu Gana")
else:
    print("Squirtle Gana")


