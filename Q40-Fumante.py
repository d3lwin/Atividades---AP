#Entrada
anos = int(input("Quantos anos? "))
cigarros_dia = int(input("Quantos cigarros/dia? "))
valor_carteira = int(input("Digite o valor da carteira de cigarros: "))

#Calculando
dias = anos*365
total_cigarros = dias*cigarros_dia
total_carteiras = total_cigarros/20
valor_total = total_carteiras*valor_carteira

#Exibindo o resultado
print(f"O fumante gastou R${valor_total}.")
