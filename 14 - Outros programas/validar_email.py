import re



def validar_email(email):

  padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

  return re.match(padrao, email) is not None



email = input().strip()



if validar_email(email):

  print("E-mail válido")

else:

  print("E-mail inválido")