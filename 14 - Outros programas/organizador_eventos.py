
from collections import defaultdict
# Dicionário para agrupar participantes por tema
eventos = defaultdict(list)

# Entrada do número de participantes
n = int(input("digite o número de participantes").strip())

# TO_DO: Crie um loop para armazenar participantes e seus temas:

for i in range(n):
    while True: # Loop interno para garantir entrada válida para o participante atual
        entrada = input("Participante:").strip()

        partes = entrada.split(',')

        if len(partes) == 2:
            nome = partes[0].strip()
            tema = partes[1].strip()

            if nome and tema: # Garante que nome e tema não são vazios
                eventos[tema].append(nome)
                break # Sai do loop interno e vai para o próximo participante

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")