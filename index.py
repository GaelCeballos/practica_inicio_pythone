import random
ra=random.randint(1,10)
print(ra)
numero= int(input("Ingresa un numero del 1 al 10 a ver si adivinas "))
if ra==numero:
    print("Felicidades adivinaste")
else:
    print("Fail")
print("*************************************")
print("El numero ganador era: {}".format(ra))