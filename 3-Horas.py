#Entrada
minuto = int(input("Digite a quantidade de minutos: "))

#Conversão
hora = minuto//60
resto_minuto = minuto%60

#Exibindo o resultado
print(f"{minuto} minutos equivalem a {hora} horas e {resto_minuto} minutos.")