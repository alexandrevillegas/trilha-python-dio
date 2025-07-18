class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item: str, preco: float):
        self.itens.append({"item": item, "preco": preco})

    def calcular_total(self) -> float:
        total = sum(item["preco"] for item in self.itens)
        return total

if __name__ == "__main__":
    quantidade_itens = int(input())

    meu_pedido = Pedido()

    for _ in range(quantidade_itens):
        entrada_item = input()
        
        # Encontra o índice do último espaço na string
        ultimo_espaco_idx = entrada_item.rfind(' ') 
        
        # Separa o nome do item e o preço com base no último espaço
        nome_item = entrada_item[:ultimo_espaco_idx]
        preco_item = float(entrada_item[ultimo_espaco_idx + 1:])

        meu_pedido.adicionar_item(nome_item, preco_item)

    valor_total = meu_pedido.calcular_total()
    print(f"{valor_total:.2f}")