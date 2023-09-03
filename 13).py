numero = int(input("Montar a tabuada de: "))
inicio = int(input("Começar por: "))
fim = int(input("Terminar em: "))

print(f"Vou montar a tabuada de {numero} começando em {inicio} e terminando em {fim}:")

contador = inicio

while contador <= fim:
    resultado = numero * contador
    print(f"{numero} X {contador} = {resultado}")
    contador += 1
