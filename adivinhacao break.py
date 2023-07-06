import random

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 100)
tentativa_correta = numero_secreto
rodada = 1

while (tentativa_correta == numero_secreto):
    print("tentativa {} ".format(rodada))

    rodada = rodada + 1
    chute_1 = int(input("Digite um número de 1 a 100: "))
    chute = int(chute_1)

    if (chute < 1 or chute > 100):
        print("VOCÊ DEVE DIGITAR UM NÚMERO ENTRE 1 E 100")
        continue

    certo = chute == numero_secreto
    maior = chute > numero_secreto

    print("Você digitou o número: ", chute_1)

    if(certo):
        print("ACERTOU MIZERAVI!")
        break
    elif (maior):
        print("VOCÊ ERROU! O SEU CHUTE FOI MAIOR QUE O NÚMERO SECRETO.")
    else:
        print("VOCÊ ERROU! O SEU CHUTE FOI MENOR QUE O NÚMERO SECRETO.")

print("O NÚMERO SECRETO É: ", numero_secreto)
print("FIM DE JOGO")