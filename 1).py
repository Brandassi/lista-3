numero_inicial = int(input("Digite o número inicial: "))
numero_final = int(input("Digite o número final: "))

if numero_inicial <= numero_final:
    
    contador = numero_inicial

    
    while contador <= numero_final:
        print(contador)
        contador += 1
else:
    print("O número inicial deve ser menor ou igual ao número final.")
