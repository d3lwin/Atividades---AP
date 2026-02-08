#Entrada
minuto = int(input('Digite o número de minutos:  '))

#Calculando
hora = minuto//60
resto_h = minuto%60
dia = hora//24
horas_restantes = hora%24

#Exibindo resultado
print(f"O número de minutos é igual a {dia} dia(s), {horas_restantes} hora(s) e {resto_h} minuto(s).")