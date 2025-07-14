def conta_vogais(texto)
    #Convertendo a string de elntrada para letras minúsculas usando .lower()
    texto = texto.lower()
    vogais = "aeiouáéíóúàèìòùâêîôûãõ"
    contador = 0
    #iniciando um loop for para percorrer cada caractere da linha de entrada
    for caractere in texto:
        if caractere in vogais:
            contador += 1

    print (f"O número de vogais na string '{numero}' é: {contador})
