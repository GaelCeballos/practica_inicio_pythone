dolar=20.3
euro=20.5
opcion = input("¿Qué deseas hacer ?:\n"
                    "A- pesos a dolares\n"
                    "B- pesos a euros\n"
                    "C- dolares a pesos\n"
                    "D- euros a pesos\n")

if opcion == "a":
    moneda = float(input("Pesos a dolares, Ingresa pesos"))
    print("La conversion es: {}".format(moneda/dolar))
elif opcion =="b":
    moneda = float(input("pesos a euros, Ingresa pesos"))
    print("La conversion es: {}".format(moneda/euro))
elif opcion == "c":
    moneda = float(input("dolares a pesos, Ingresa dolares"))
    print("La conversion es: {}".format(moneda*dolar))
elif opcion == "d":
    moneda = float(input("euros a pesos, Ingresa euros"))
    print("La conversion es: {}".format(moneda*euro))
else:
    print("Solo se puede ingresar la opcion a,b,c,d")
    exit()