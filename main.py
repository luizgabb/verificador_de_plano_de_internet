def recomendar_plano(consumo):

  if consumo <= 10:

    return "Recomendamos que escolha nosso Plano Essencial Fibra - 50Mbps"

  elif consumo <= 20:

    return "Recomendamos que escolha nosso Plano Prata Fibra - 100Mbps"

  else:

    return "Recomendamos que escolha nosso Plano Premium Fibra - 300Mbps"




# Solicita ao usuário que insira o consumo médio mensal de dados:

consumo = float(input("Qual seu consumo de dados?(GB)"))




# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:

print(recomendar_plano(consumo))