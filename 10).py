print("Mercearia")
total = 0.0
contador = 1

while True:
    preco = float(input(f"Produto {contador}: R$ "))
    if preco == 0:
        break
    total += preco
    contador += 1

print(f"Total: R$ {total:.2f}")

dinheiro = float(input("Dinheiro: R$ "))
troco = dinheiro - total

print(f"Troco: R$ {troco:.2f}")
