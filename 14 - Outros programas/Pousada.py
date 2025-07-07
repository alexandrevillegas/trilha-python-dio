def gerenciar_reservas(quartos_disponiveis_str, quartos_solicitados_str):
    """
    Verifica quais reservas podem ser aceitas e quais devem ser recusadas.

    Args:
        quartos_disponiveis_str (str): String com os números dos quartos disponíveis, separados por espaços.
        quartos_solicitados_str (str): String com os números dos quartos solicitados, separados por espaços.

    Returns:
        tuple: Uma tupla contendo duas listas: (quartos_confirmados, quartos_recusados).
    """
    # Converte as strings de entrada para conjuntos de números de quartos (para busca eficiente)
    # Usamos set() para garantir que não haja quartos duplicados e para operações de busca mais rápidas.
    quartos_disponiveis = set(quartos_disponiveis_str.split())
    quartos_solicitados = quartos_solicitados_str.split() # Mantemos como lista para preservar a ordem de solicitação

    reservas_confirmadas = []
    reservas_recusadas = []

    for quarto_solicitado in quartos_solicitados:
        if quarto_solicitado in quartos_disponiveis:
            reservas_confirmadas.append(quarto_solicitado)
            quartos_disponiveis.remove(quarto_solicitado)  # Remove o quarto disponível para evitar reservar novamente
        else:
            reservas_recusadas.append(quarto_solicitado)
            
    return reservas_confirmadas, reservas_recusadas

# --- Entrada de Dados ---
quartos_disponiveis_input = input("Insira os quartos disponíveis: ")
quartos_solicitados_input = input("Insira os quartos solicitados: ")

# --- Processamento ---
confirmadas, recusadas = gerenciar_reservas(quartos_disponiveis_input, quartos_solicitados_input)

# --- Saída de Dados ---
print(f"Reservas confirmadas: {' '.join(confirmadas)}")
print(f"Reservas recusadas: {' '.join(recusadas)}")