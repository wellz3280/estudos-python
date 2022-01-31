from collections import defaultdict

meu_texto = "Meu nome é Weliton e gosto muito de nomes eu tenho uma gata e o nome dela é Suzi".lower()

aparicoes = defaultdict(int)
for palavra in meu_texto.split():
    ate_agora = aparicoes[palavra]
    aparicoes[palavra] = ate_agora +1

print(aparicoes)