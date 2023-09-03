multiplo = int(input("Digite o número múltiplo: "))
limite = int(input("Digite o limite: "))

contador = 0
while contador <= limite:
    if contador % multiplo == 0:
        print(contador)
    contador += 1
