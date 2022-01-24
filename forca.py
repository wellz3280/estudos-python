def jogar_forca():
    print("**********************************")
    print("*** bem vindo ao jogo de Forca ***")
    print("**********************************")

    palavra_secreta = "banana".upper()
    dica = "fruta"
    escolher_dica = False
    tamanho_palavra = len(palavra_secreta)
    letras_acertadas = []
    pontos = 100
    pontos_por_letra = 10


    for i in range (0,tamanho_palavra):
        letras_acertadas.append("_")

    enforcou = False
    acertou = False

    print("Você começa com 100 pontos a cada erro perde 10 pontos")
    print("Você pode escolher uma dica, mais perdera 10 pontos")

    while(not enforcou and not acertou):
        print("Pontucação atual: {:d}".format(pontos))
        chute = input("Digite uma letra ").upper().strip()

        # regras do jogo
        # SE ERRAR PERDE 10 PONTOS

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index +=1
        else:
            pontos -= pontos_por_letra

        if(pontos == 50):
            escolher_dica = True
            escolha_usuario = input("Voçe tem {} pontos, Quer uma dica ? (S) sim e (N) não ".format(pontos))\
                .upper().strip()

        if(escolher_dica and escolha_usuario == "S"):
            print(dica)
            pontos -= 10
        elif(escolher_dica and escolha_usuario == "N"):
            continue

        enforcou = pontos == 0

        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

        if(acertou):
            print(" Voçê ganhou parabens, e fez {:d} pontos".format(pontos))

        if(enforcou):
            print("game over")

if(__name__ == "__main__"):
    jogar_forca()