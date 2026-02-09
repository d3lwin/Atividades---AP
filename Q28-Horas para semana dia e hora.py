#Entrada
hora = int(input('Digite o número de horas:  '))

#Calculando
dia = hora//24
resto_d = hora%24
semana = dia//7
dias_restantes = semana%7

#Exibindo resultado
print(f"O número de horas é igual a {semana} semanas(s), {dias_restantes} dias(s) e {resto_d} hora(s).")
