#Entrada
nota_1 = float(input("Digite a primeira nota: "))
peso_1 = int(input("Digite o peso: "))
nota_2 = float(input("Digite a segunda nota: "))
peso_2 = int(input("Digite o peso: "))
nota_3 = float(input("Digite a terceira nota: "))
peso_3 = int(input("Digite o peso: "))

#Calculando a media
pesos = peso_1 + peso_2 + peso_3
media = (nota_1*peso_1 + nota_2*peso_2 + nota_3*peso_3)/pesos

#Exibindo resultado
print(f"A média ponderada das notas é {media}.")
