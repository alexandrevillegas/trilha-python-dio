# Função
def calcular_nivel(vitorias, derrotas):
  
    saldo = vitorias - derrotas
    
    nivel = ""

    if vitorias <= 10:
        nivel = "Ferro"
    elif vitorias <= 20:
        nivel = "Bronze"
    elif vitorias <= 50:
        nivel = "Prata"
    elif vitorias <= 80:
        nivel = "Ouro"
    elif vitorias <= 90:
        nivel = "Diamante"
    elif vitorias <= 100:
        nivel = "Lendário"
    else: # Se vitórias for maior ou igual a 101
        nivel = "Imortal"
        
    return saldo, nivel

# Laço
while True:
    99
    try:
        qtd_vitorias = int(input("Digite a quantidade de vitórias: "))
        qtd_derrotas = int(input("Digite a quantidade de derrotas: "))
    except ValueError:
        print("\nErro: Por favor, digite apenas números inteiros.\n")
        continue # Volta para o início do laço

    # Chamada
    saldoVitorias, nivelHeroi = calcular_nivel(qtd_vitorias, qtd_derrotas)

    # Saída
    print(f"\nO Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivelHeroi}**")
    
   
    continuar = input("\nDeseja calcular para outro herói? (s/n): ")
    if continuar.lower() != 's':
        print("Programa finalizado.")
        break 