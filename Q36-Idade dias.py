#Entrada
anos = int(input('Quantos anos?  '))
meses = int(input('Quantos meses?  '))
dias = int(input('Quantos dias?  '))

#Calculando
dias_totais = anos*365 + meses*30 + dias

#Exibindo o resultado
print(f"Fulano tem {dias_totais} dia(s) de idade")
