#Entrada
segundo = int(input('Digite o número de segundos:  '))

#Calculando
hora = segundo//3600
resto_h = segundo%3600
minuto = resto_h//60
resto_m = resto_h%60

#Exibindo resultado
print(f"O número de segundos é igual a {hora} hora(s), {minuto} minuto(s) e {resto_m} segundo(s).")