#Entrada
valor_fabrica = int(input("Digite o valor de fábrica do carro: "))

#Calculando
imposto = valor_fabrica*0.45
distribuidor = valor_fabrica*0.28
valor_final = valor_fabrica + imposto + distribuidor

#Exibindo o resultado
print(f"O valor final do carro é R${valor_final}.")