base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = 1

contador = 0
while contador < expoente:
    resultado *= base
    contador += 1

print(f"{base} elevado a {expoente} é igual a {resultado}")
