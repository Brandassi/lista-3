tamanho = int(input("Digite o tamanho da linha (número de pontos): "))
linha = ""
contador = 0

while contador < tamanho:
    linha += "*"
    contador += 1

print(linha)
