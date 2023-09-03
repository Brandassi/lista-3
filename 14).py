salario_inicial = float(input("Digite o salário inicial do funcionário: "))
ano = 1996
salario = salario_inicial
aumento_percentual = 1.5

while ano <= 2023:
    salario += salario * (aumento_percentual / 100)
    aumento_percentual += 1.5
    ano += 1

print(f"O salário atual do funcionário em 2023 é R${salario:.2f}")