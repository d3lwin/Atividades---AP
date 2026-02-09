#Entrada
numero = int(input("Digite um número: "))

#Decompondo o número
centena = numero//100
resto = numero%100
dezena = resto//10
unidade = resto%10
#Invertendo
num_invertido = unidade*100 + dezena*10 + centena
#Calculando o resultado
diferenca = numero - num_invertido

#Exibindo o resultado

print(f"O resultado é: {diferenca}")
