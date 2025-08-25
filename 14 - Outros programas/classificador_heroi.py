# -*- coding: utf-8 -*-

# Laço de repetição 
while True:
    

    nome_heroi = input("Digite o nome do Herói: ")
    
  
    try:
        xp_heroi = int(input(f"Digite a quantidade de experiência (XP) de {nome_heroi}: "))
    except ValueError:
        print("\nErro: A experiência (XP) deve ser um número inteiro. Tente novamente.\n")
        continue # Volta para o início do laço de repetição

    # --- ESTRUTURA DE DECISÕES ---
    # Variável de nível.
    nivel = ""

  
    if xp_heroi < 1001:
        nivel = "Ferro"
    elif xp_heroi >= 1001 and xp_heroi <= 2000:
        nivel = "Bronze"
    elif xp_heroi >= 2001 and xp_heroi <= 5000:
        nivel = "Prata"
    elif xp_heroi >= 5001 and xp_heroi <= 7000:
        nivel = "Ouro"
    elif xp_heroi >= 7001 and xp_heroi <= 8000:
        nivel = "Platina"
    elif xp_heroi >= 8001 and xp_heroi <= 9000:
        nivel = "Ascendente"
    elif xp_heroi >= 9001 and xp_heroi <= 10000:
        nivel = "Imortal"
    else: # Se o XP for maior ou igual a 10.001
        nivel = "Radiante"

    # --- SAÍDA ---
   

    print(f"O Herói de nome **{nome_heroi}** está no nível de **{nivel}**")

    
    # Pergunta ao usuário se ele deseja classificar outro herói.
    continuar = input("\nDeseja classificar outro herói? (s/n): ")
    

    if continuar.lower() != 's':
        print("Programa finalizado.")
        break
    print("\n") 