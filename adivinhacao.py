# python parte modulo 7
import random

print("*********************************")
print("bem vindo ao jogo de adivinhação")
print("*********************************")

# A funcão input sempre devolve uma string
# funcão int() converte string para inteiro
# gerando numero aleatorio com a biblioteca random

numero_secreto = round(random.randrange(1,101))
total_de_tentativas = 0


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
    chute = input("digite o seu numero: ")

    if(int(chute) < 1 or int(chute) > 100):
        print("digite um numero entre 1 e 100")
        continue

    nunero_digitado = int(chute)
    print("********************************")

    acertou=nunero_digitado == numero_secreto
    maior = nunero_digitado > numero_secreto
    menor = nunero_digitado < numero_secreto

    if(acertou):
        print("voce acertou")
        break
    else:
        if(maior):
            print("voce errou seu chute foi maior que o numero secreto")
        elif(menor):
            print("voce errou seu chute foi menor que o numero secreto")
    print("********************************")

