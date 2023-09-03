n = int(input("Digite o valor de n: "))
soma = 0
contador = 0

while contador < n:
    valor = float(input("Digite um valor: "))
    soma += valor
    contador += 1

media = soma / n
print(f"A média aritmética dos {n} valores é: {media}")
