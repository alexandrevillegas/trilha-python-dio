def sistema_login():
  """
  Verifica as credenciais de login de um usuário usando um dicionário de clientes.
  """
  # Dicionário de usuários e senhas.
  usuarios = {
      "joao": "1234",
      "ana": "abcd",
      "maria": "senha123",
      "marcelo": "iou789",
  }

  # Solicita a entrada do usuário.
  usuario = input("Digite seu nome:")
  senha = input("Digite sua senha: ")

  # Verifica se o usuário existe no dicionário e se a senha está correta.
  if usuario in usuarios and usuarios[usuario] == senha:
    print("Acesso permitido")
  else:
    print("Usuário ou senha incorretos")

# Executa o programa.
sistema_login()