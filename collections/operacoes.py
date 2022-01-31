usuarios = {1,5,76,34,52,13,17}

# adiconando elemento em um conjunto
usuarios.add(99)
usuarios.add(990)
# pode-se congelar o conjunto, proibindo a adição de novos elementos
congelar = frozenset(usuarios)

print(len(usuarios))

meu_texto = "meu nome é weliton e gosto muito de nomes eu tenho uma gata e o nome dela é suzi"
print(meu_texto.split())
print("weliton" in meu_texto.split())
# posso transformar strings em conjunto
# print(set(meu_texto.split()))