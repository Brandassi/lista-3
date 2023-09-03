numero = int(input("Digite um número para ver sua tabuada: "))
contador = 1

while contador <= 10:
    produto = numero * contador
    print(f"{numero} x {contador} = {produto}")
    contador += 1
