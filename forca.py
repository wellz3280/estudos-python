import random

def jogar_forca():
   
    imprime_mensagem_abertura()

    palavra_secreta = seleciona_palavra_secreta()

    tamanho_palavra = len(palavra_secreta)
    letras_acertadas = inicializa_letras_acertadas(tamanho_palavra)

    # o numero de tentativas é a quantidade de letras + 2

    nivel = input("Selecione uma dificuldade (1) Fácil (2)Médio (3) Difícil (4) Muito DIfícil ")
    chances =  nivelDoJogo(nivel,tamanho_palavra)


    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        print("Numero de chutes: {:d}".format(chances))
        print(letras_acertadas," {:d} letras".format(tamanho_palavra))

        chute = pedeChute()

        if(chute in palavra_secreta):
            marcaChuteCorreto(chute,palavra_secreta,letras_acertadas)
        else:
            chances -= 1
            desenha_forca(chances)

        enforcou = chances == 0
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        if (acertou):
            imprime_mensagem_vencedor()

        if(enforcou):
            imprime_mensagem_perdedor(palavra_secreta)

def imprime_mensagem_abertura():
    print("**********************************")
    print("*** bem vindo ao jogo de Forca ***")
    print("**********************************")

def seleciona_palavra_secreta():
    arquivo = open("palavras.txt","r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()
    numero_aleatorio = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero_aleatorio].upper()
    return palavra_secreta

def inicializa_letras_acertadas(tamanho):
    range_palavra = []
    for i in range(0, tamanho):
        range_palavra.append("_")
    return range_palavra

def pedeChute():
    return input("Digite uma letra ").upper().strip()

def marcaChuteCorreto(chute,palavra_secreta,letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def nivelDoJogo(nivel,tamanho_palavra):
    # nivel do jogo se baseia em quantidade
    # de letras mais nivel selecionado

    if(int(nivel) == 1):
        chance = tamanho_palavra + 10
        return chance
    elif(int(nivel) == 2):
        chance = tamanho_palavra + 6
        return chance
    elif(int(nivel) == 3):
        chance = tamanho_palavra + 4
        return chance
    elif(int(nivel) == 4):
        chance = tamanho_palavra + 3
        return chance

def desenha_forca(chance):
    print("  _______     ")
    print(" |/      |    ")

    if(chance == 7):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(chance == 6):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(chance == 5):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(chance == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(chance == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(chance == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (chance == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogar_forca()
