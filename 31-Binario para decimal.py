#Entrada
binario = int(input('Digite um número (binário, 4 dígitos): '))

#Decompondo o número
bit_4 = binario//1000
resto_1 = binario%1000
bit_3 = resto_1//100
resto_2= resto_1%100
bit_2 = resto_2//10
bit_1 = resto_2%10

#Convertendo para decimal
decimal = bit_1 + bit_2*2 + bit_3*4 + bit_4*8

#Exibindo o resultado
print(f"O número binário {binario} equivale a {decimal}.")