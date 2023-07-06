# import
from random import choice,randint
from tkinter import *
from time import sleep


# funções
def btnGirar():
    global faceMaior
    if dadoEscolhido.get() == 1:
        faceMaior = 6
        girardado()
    elif dadoEscolhido.get() == 2:
        faceMaior = 12
        girardado()
    elif dadoEscolhido.get() == 3:
        faceMaior = 20
        girardado()


def girardado():
    numero = randint(faceMenor, faceMaior)
    sleep(0.5)
    dado1.set(numero)


# variaveis
faceMenor = 1
faceMaior = 6

# janela
dado = Tk()
dado.title("Dados")
dado.config(bg='White')
dado.geometry("300x200")
dado.resizable(False, False)

dadoEscolhido = IntVar()
dado1 = StringVar()

face6 = Radiobutton(dado, text="6 Lados", value=1, font="Times 14", bg="White", variable=dadoEscolhido)
face12 = Radiobutton(dado, text="12 Lados", value=2, font="Times 14", bg="White", variable=dadoEscolhido)
face20 = Radiobutton(dado, text="20 Lados", value=3, font="Times 14", bg="White", variable=dadoEscolhido)
face6.select()

face6.grid(row=0, column=0)
face12.grid(row=0, column=1)
face20.grid(row=0, column=2)

Button(dado, text="Girar", font="Times, 16", command=btnGirar).grid(columnspan=3)
lblDado1 = Label(dado, text='', font='Times 30', textvariable=dado1, bg='#ffffff').grid(columnspan=3)

dado.mainloop()