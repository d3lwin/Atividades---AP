#Entrada
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
d = int(input("Digite o valor de d: "))
e = int(input("Digite o valor de e: "))
f = int(input("Digite o valor de f: "))

#Calculando
numerador_x = c*e - b*f
numerador_y = a*f - c*d
denominador = a*e - b*d
x = numerador_x/denominador
y = numerador_y/denominador

#Exibindo o resultado
print(f"Os valores de x e y resultantes são:  {x}, {y}")