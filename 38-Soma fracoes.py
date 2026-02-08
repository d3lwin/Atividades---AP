#Entrada
numerador_1 = int(input("Digite o numerador: "))
denominador_1 = int(input("Digite o denominador: "))
numerador_2 = int(input("Digite o numerador: "))
denominador_2 = int(input("Digite o denominador: "))

#Calculando
mmc = denominador_1*denominador_2
numerador_3 = (mmc/denominador_1)*numerador_1
numerador_4 = (mmc/denominador_2)*numerador_2
numerador_final = int(numerador_3 + numerador_4)

#Exibindo o resultado
print(f"A soma das frações é: {numerador_final}/{mmc}")