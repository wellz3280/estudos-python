# dicionario é tipo array associativo do php

# outras formas de criar um dicionario
# dicionario = dict(joaquin = 1, cachorro = 2)

aparicoes = {'carlos':1,'weliton':1,'cachorro':2,'nome':2,'vindo':1}
print(aparicoes)
aparicoes['weliton']
# caso não exista no dicionario devolve o
print(aparicoes.get('xpto',0))
# mudando o valor
aparicoes['weliton'] = 2
print(aparicoes)
# deletando elemento
del aparicoes['carlos']
print(aparicoes)

# pengando as chaves
for elemento in aparicoes.keys():
    print(elemento)

# pegando os valores
for elemento in aparicoes.values():
    print(elemento)

# pegando chaves e valores
for elemento in aparicoes.items():
    print(elemento)

#desenpacotando
for chave,valor in aparicoes.items():
    print(chave,"= ",valor)

palavras = ["palavra {}".format(chave) for chave in aparicoes.keys()]
print(palavras)