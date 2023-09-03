numero = int(input("Digite um número inteiro para calcular o fatorial: "))
resultado = 1
contador = 1

while contador <= numero:
    resultado *= contador
    contador += 1

print(f"O fatorial de {numero} é {resultado}")
