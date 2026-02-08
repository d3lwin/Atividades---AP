#Entrada
metro = int(input('Digite o valor em metro:  '))

#Calculando
km = metro//1000
resto_m = metro%1000

#Exibindo resultado
print(f"A o valor em m é igual a {km}km e {resto_m}metro(s).")