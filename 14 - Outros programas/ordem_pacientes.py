def ordenar_pacientes(pacientes):
    """
    Organiza uma lista de pacientes com base na idade e na urgência do caso.

    Args:
        pacientes (list): Uma lista de dicionários, onde cada dicionário
                          representa um paciente com as chaves 'nome', 'idade' e 'status'.

    Returns:
        list: Uma nova lista de pacientes ordenada por prioridade.
    """

    def _obter_prioridade(paciente):
        # Prioridade máxima para "urgente"
        if "urgente" in paciente['status'].lower():
            return 0
        # Prioridade para pacientes acima de 60 anos
        elif paciente['idade'] > 60:
            return 1
        # Demais pacientes
        else:
            return 2

    # A função sorted() é usada para criar uma nova lista ordenada.
    # A 'key' é uma tupla para ordenar por múltiplos critérios:
    # 1. A prioridade calculada (0, 1 ou 2)
    # 2. A idade (para desempate em grupos de mesma prioridade, útil para o critério > 60 anos)
    #    Para que pacientes mais velhos tenham precedência dentro do mesmo grupo de prioridade,
    #    usamos o negativo da idade (-paciente['idade']), garantindo uma ordem decrescente de idade.
    # 3. O índice original (para garantir a "ordem de chegada" para pacientes com a mesma prioridade
    #    e idade, já que a função sorted() é estável por padrão, mas incluir o índice garante isso
    #    explicitamente).
    pacientes_ordenados = sorted(
        pacientes,
        key=lambda p: (_obter_prioridade(p), -p['idade'], pacientes.index(p))
    )
    
    return pacientes_ordenados

# --- Entrada de Dados ---
n = int(input("Insira o número de pacientes: "))
lista_pacientes = []

for _ in range(n):
    nome, idade_str, status = input("Insira nome, idade e status do paciente: ").split(', ')
    idade = int(idade_str)
    lista_pacientes.append({'nome': nome, 'idade': idade, 'status': status})

# --- Processamento ---
pacientes_em_ordem = ordenar_pacientes(lista_pacientes)

# --- Saída de Dados ---
nomes_ordenados = [p['nome'] for p in pacientes_em_ordem]
print("Ordem de Atendimento:", ", ".join(nomes_ordenados))