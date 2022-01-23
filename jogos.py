import forca
import adivinhacao

def escolher_jogo():
    print("*********************************")
    print("*********Escolha Um jogo*********")
    print("*********************************")

    print("(1) Forca (2) Adivinhaçao")

    jogo = int(input("Qual Jogo"))

    if(jogo == 1):
        print("Jognado Forca")
        forca.jogar_forca()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar_adivinhacao()

if(__name__ == "__main__"):
    escolher_jogo()