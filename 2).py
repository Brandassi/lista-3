contador_pares = 0
contador_impares = 0

contador = 0
while contador < 10:
    numero = int(input(f"Digite o {contador + 1}º número inteiro: "))
    
    if numero % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1
    
    contador += 1

print(f"Quantidade de números pares: {contador_pares}")
print(f"Quantidade de números ímpares: {contador_impares}")
