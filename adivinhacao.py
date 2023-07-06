print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 15
total_tentativas = 5
rodada = 1

while (rodada <= total_tentativas):
    print("Tentativa {} de {} ". format(rodada, total_tentativas))
    chute_1 = input("Digite um número: ")
    chute = int(chute_1)

    certo = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    print("Você digitou o número: ", chute_1)

    if(certo):
        print("ACERTOU MIZERAVI!")
    else:
        if (maior):
            print("VOCÊ ERROU! O SEU CHUTE FOI MAIOR QUE O NÚMERO SECRETO.")
        elif (menor):
            print("VOCÊ ERROU! O SEU CHUTE FOI MENOR QUE O NÚMERO SECRETO.")

    rodada = rodada + 1
print("FIM DE JOGO")


