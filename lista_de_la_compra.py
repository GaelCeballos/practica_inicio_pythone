
lista_de_la_compra = []
desicion = None

print("Programa Lista de la compra \n")
while True :
    desicion = input("Qué deseas comprar ([q] Para salir)")
    if desicion =="q" :
        break
    elif desicion in lista_de_la_compra :
        print ("{} el item ya esta en la lista".format(desicion))
    else :
        if input("Seguro que quieres añadir {} este item a la compra [s/n]".format(desicion)) == "s" :
            lista_de_la_compra.append(desicion)

print("La lista de la compra es:")
print(lista_de_la_compra)
