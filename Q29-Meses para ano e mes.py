#Entrada
mes = int(input('Digite o número de meses:  '))

#Calculando
ano = mes//12
resto_a = mes%12

#Exibindo resultado
print(f"O número de meses é igual a {ano} ano(s) e {resto_a} mes(es).")
