palabra = input("Ingrese el texto: ")
Letra=len(palabra)
i=0
while i<Letra:
    if(palabra[i] != "a" and palabra[i] != "e" and palabra[i] != "i" and palabra[i] != "o" and palabra[i] != "u"):
        print(palabra[i])
    i = i+1