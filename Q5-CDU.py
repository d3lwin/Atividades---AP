#Entrada
numero = int(input('Digite um número: '))

#Decompondo o número
centena = numero//100
resto = numero%100
dezena = resto//10
unidade = resto%10

#Exibindo o resultado
print(centena + dezena + unidade)
