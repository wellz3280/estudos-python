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

def imprimeMensagemVencer(acertou):
    if (acertou):
        print(" Voçê ganhou parabens")
    else:
        print("Game Over")

def nivelDoJogo(nivel,tamanho_palavra):
    # nivel do jogo se baseia em quantidade
    # de letras mais nivel selecionado

    if(int(nivel) == 1):
        chance = tamanho_palavra + 10
        return chance
    elif(int(nivel) == 2):
        chance = tamanho_palavra + 5
        return chance
    elif(int(nivel) == 3):
        chance = tamanho_palavra + 2
        return chance
    elif(int(nivel) == 4):
        chance = tamanho_palavra
        return chance