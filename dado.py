import random


jogar = False

while(not jogar):
    ask = input("Voçê gostaria de jogar os dados digite (y) para sim e (n) para não ?")
    
    if(ask == 'y'):
        dado = round(random.randrange(1,7))
        print(dado)

    elif(ask == 'n'):
        break

    