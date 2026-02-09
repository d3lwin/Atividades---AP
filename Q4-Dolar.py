#Entrada
valor_dolar = float(input("Digite a cotação do dólar: "))
dolar = float(input("Digite o valor em dólar: "))

#Conversão
real = dolar * valor_dolar

#Exibindo o resultado
print(f"Na cotação atual, ${dolar} equivalem a R${real}")
