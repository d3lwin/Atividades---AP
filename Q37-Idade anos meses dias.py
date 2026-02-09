#Entrada
dias = int(input('Quantos dias?  '))

#Calculando
anos = dias//365
resto = dias%365
meses = resto//30
dias = resto%30

#Exibindo o resultado
print(f"Fulano tem {anos} ano(s), {meses} mes(es) e {dias} dias(s) de idade")
