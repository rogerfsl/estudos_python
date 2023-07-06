print("*********************************")
print("***BEM VINDO AO JOGO DE FORCA!***")
print("*********************************")

palavra_secreta = "carro".upper()
letras_acertadas = ["_","_","_","_","_"]

erros = 0

print (len(palavra_secreta))
print(letras_acertadas)

while (True):

    chute = input("Digite uma letra! ")
    chute = chute.strip().upper()

    if (chute in palavra_secreta):
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                letras_acertadas[index] = letra
            index += 1

    else:
        erros += 1
        print("VOCE ERORU, LHE RESTAM {} TENTATIVAS".format(6-erros))

    if (erros == 6):
        break
    elif ("_" not in letras_acertadas):
        print(letras_acertadas)

if ("_" not in letras_acertadas):
    print("VOCÊ GANHOU!!")
else:
    print("FIM DO JOGO!!")