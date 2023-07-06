total = 0
palavra = "phyton rocks!"
acabou = False

while (not acabou):
    acabou = (total == len(palavra))
    total = total + 1

print(" A palavra Phyton rocks tem ", total - 1, "letras!" )