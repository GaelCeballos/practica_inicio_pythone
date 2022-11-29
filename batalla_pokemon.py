from random import randint

vida_pikachu = 80
vida_squirtle = 90

vida_pi = vida_pikachu
vida_sq = vida_squirtle

print("Bienvenido a la batalla pokemon")
while vida_pi > 0 and vida_sq > 0 :

    barra_de_vida_pikachu = int(vida_pi *10 / vida_pikachu)
    print("Pikachu    [{}{}] ({}/{})".format("*"*barra_de_vida_pikachu, " "*(10 - barra_de_vida_pikachu),
                                                                vida_pi,vida_pikachu))

    barra_de_vida_squirtle = int(vida_sq*10 / vida_squirtle)
    print("Squirtle    [{}{}]".format("*"*barra_de_vida_squirtle, ""*(10 - barra_de_vida_squirtle)))


    print("ataque de pikachu...Preparate")
    ataque_pikachu = randint(1,2)
    if ataque_pikachu == 1:
        print("Pikachu ha usado Bola Voltio")
        vida_sq -= 10
    else :
        print("Pikachu ha usado onda trueno")
        vida_sq -= 11
    
    input("Enter para continuar....")
    print("Turno de squirtle... TU TURNO DE ATACAR")
    ataque_squirtle = input("Cual ataque deseas hacer [p] Placaje, [a] Pistola de agua y [b] Burbuja")
    if ataque_squirtle == "p" :
        print("Ataque placaje")
        vida_pi -= 10
    elif ataque_squirtle == "a" :
        print("Ataque pistola de agua")
        vida_pi -= 12
    elif ataque_squirtle == "b" :
        print("Ataque burbuja")
        vida_pi -= 9
    else:
        print("Fallaste")

if vida_pi > vida_sq :
    print("Pikachu Gana")
else:
    print("Squirtle Gana")


