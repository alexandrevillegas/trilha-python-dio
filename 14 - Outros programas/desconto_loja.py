# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# TODO: Aplique o desconto se o cupom for válido:
if cupom == "DESCONTO10":
  preco = (preco*0.90)
  preco_final = "{:.2f}".format(preco)
  print(preco_final)
elif cupom == "DESCONTO20":
  preco = (preco*0.80)
  preco_final = "{:.2f}".format(preco)
  print(preco_final)
else:
  preco_final = "{:.2f}".format(preco)
  print(preco_final)