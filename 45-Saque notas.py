#Entrada
valor = int(input('Digite um valor: '))

#Calculando as notas
nota_cinquenta = valor//50
resto_1 = valor%50
nota_dez = resto_1//10
resto_2= resto_1%10
nota_cinco = resto_2//5
nota_um = resto_2%5

#Exibindo o resultado
print(f"Você irá receber {nota_cinquenta} nota(s) de 50 reais, {nota_dez} nota(s) de 10 reais, {nota_cinco} nota(s) de 5 reais de {nota_um} nota(s) de 1 real.")