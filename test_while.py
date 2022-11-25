respuesta = None



while respuesta !="a" and respuesta !="b" and respuesta != "c":
    respuesta= input("Que opcion prefieres A, B o C")

if respuesta =="a":
    print("has elegiod bien")
elif respuesta =="b":
    print("mal")
elif respuesta == "c":
    print("muy mal")
else: 
    print("no se a dado una respuesta con sentido: ")
