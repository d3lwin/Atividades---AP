#Entrada
valor = int(input('Digite um valor: '))

#Calculando
prestacao = valor//3
resto = valor%3
entrada = prestacao + resto

#Exibindo o resultado
print(f"O valor da entrada é R${entrada} e cada prestação será de R${prestacao}.")
