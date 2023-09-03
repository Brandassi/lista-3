total_idades = 0
quantidade_pessoas = 0

idade = int(input("Digite a idade da pessoa (ou -1 para encerrar): "))
while idade != -1:
    total_idades += idade
    quantidade_pessoas += 1
    idade = int(input("Digite a idade da pessoa (ou -1 para encerrar): "))

if quantidade_pessoas == 0:
    print("Nenhuma idade foi informada.")
else:
    media_idades = total_idades / quantidade_pessoas

    if 0 <= media_idades <= 25:
        print("A turma é jovem.")
    elif 26 <= media_idades <= 60:
        print("A turma é adulta.")
    else:
        print("A turma é idosa.")
