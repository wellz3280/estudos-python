import random
def jogar_adivinhacao():
    print("**********************************")
    print("*bem vindo ao jogo de adivinhação*")
    print("**********************************")

    # A funcão input sempre devolve uma string
    # funcão int() converte string para inteiro
    # gerando numero aleatorio com a biblioteca random

    # variaveis do jogo
    numero_secreto = round(random.randrange(1,101))
    total_de_tentativas = 0
    pontos = 1000


    print("Qual nivél de dificuldade ?")
    print("(1) Fácil (2) Médio (3) Difícil ")

    nivel = int(input("Ecolha um nível"))

    if(nivel ==1):
        total_de_tentativas = 20
    elif(nivel ==2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1,total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada,total_de_tentativas))

        chute = int(input("digite o seu numero: "))

        if(chute< 1 or chute > 100):
            print("digite um numero entre 1 e 100")
            continue

        print("********************************")

        acertou= chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("voce acertou e fez {:d} pontos".format(pontos))
            break
        else:
            if(maior):
                print("voce errou seu chute foi maior que o numero secreto")
            elif(menor):
                print("voce errou seu chute foi menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        print("********************************")

    if(rodada == total_de_tentativas):
        print("GAME OVER")

if(__name__ == "__main__"):
    jogar_adivinhacao()
