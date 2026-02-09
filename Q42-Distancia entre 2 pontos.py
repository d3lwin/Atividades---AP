#Entrada
x_1 = int(input("Digite o x do primeiro ponto: "))
y_1 = int(input("Digite o y do primeiro ponto: "))
x_2 = int(input("Digite o x do segundo ponto: "))
y_2 = int(input("Digite o y do segundo ponto: "))

#Calculando
diferenca_x = x_2 - x_1
diferenca_y = y_2 - y_1
soma_quadrados = diferenca_x**2 + diferenca_y**2
distancia = soma_quadrados**(1/2)

#Exibindo o resultado
print(f"A distância entre os pontos é: {distancia}")
