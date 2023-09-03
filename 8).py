soma = 0
contador = 0

while True:
    numero = int(input("Digite um número inteiro (ou 0 para sair): "))
    
    if numero == 0:
        break
    
    soma += numero
    contador += 1

print(f"A soma dos {contador} números lidos é: {soma}")
