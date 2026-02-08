#Entrada
numero = int(input('Digite um número (4 dígitos): '))

#Decompondo o número
milhar = numero//1000
resto_m = numero%1000
centena = resto_m//100
resto_c= resto_m%100
dezena = resto_c//10
unidade = resto_c%10

#somando
total = milhar + centena + dezena + unidade

#Exibindo o resultado
print(f"O resultado é: {total}")