from collections import defaultdict,Counter

meu_texto = "Meu nome é Weliton e gosto muito de nomes eu tenho uma gata e o nome dela é Suzi".lower()

# aparicoes = defaultdict(int)
# for palavra in meu_texto.split():
#     aparicoes[palavra] += 1

aparicoes = Counter(meu_texto.split())

print(aparicoes)