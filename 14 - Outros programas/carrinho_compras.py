# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input("digite o número de itens").strip())

# Loop para adicionar itens ao carrinho
for _ in range(n):
    linha = input("digite o produto e o valor").strip()
    
    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ")
    2
    # Separa o nome do produto e o preço
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])
    
    # Adiciona ao carrinho
    carrinho.append((item, preco))
    total += preco

# TODO: Exiba os itens e o total da compra

# print(carrinho)
# print(type(carrinho))
# print(len(carrinho))


num_itens = (len(carrinho))
coord_item_corrente = 0
total = 0.00

while num_itens>0:

    item_corrente = carrinho[coord_item_corrente][0]
    valor_item_corrente = carrinho[coord_item_corrente][1]
    print(f"{item_corrente}: R${valor_item_corrente:.2f}")
    coord_item_corrente =(coord_item_corrente + 1)
    num_itens =(num_itens - 1)
    total = (total + valor_item_corrente)

print(f"Total: R${total:.2f}")