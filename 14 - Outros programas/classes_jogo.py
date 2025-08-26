class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome.strip()
        self.idade = idade
        self.tipo = tipo.lower().strip()

    def atacar(self):
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            ataque = "forma desconhecida"
        print(f"O {self.tipo} {self.nome} atacou usando {ataque}")

def jogo_interativo():
    herois = []

    # Quantos heróis criar?
    while True:
        try:
            quantidade = int(input("Quantos heróis deseja criar? "))
            if quantidade > 0:
                break
            else:
                print("Número precisa ser maior que zero.")
        except ValueError:
            print("Número inválido. Tente novamente.")

    for i in range(1, quantidade + 1):
        nome = input(f"Digite o nome do herói #{i}: ").strip()

        while True:
            try:
                idade = int(input(f"Digite a idade do herói {nome}: "))
                break
            except ValueError:
                print("Idade inválida. Digite um número inteiro.")

        tipo = input(
            f"Digite o tipo do herói {nome} (mago, guerreiro, monge, ninja): "
        ).lower().strip()

        if tipo not in ("mago", "guerreiro", "monge", "ninja"):
            print("Tipo não reconhecido. Será considerado 'desconhecido'.")

        herois.append(Heroi(nome, idade, tipo))

    print("\n=== Resultados dos ataques ===")
    for heroi in herois:
        heroi.atacar()

if __name__ == "__main__":
    jogo_interativo()
