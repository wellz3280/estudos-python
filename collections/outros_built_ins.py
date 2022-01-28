# idade = [23,29,18,78,55,14,22,99]
#
# # pegando o indice de uma lista na unha
# for i in range(len(idade)):
#     print(i, idade[i])
#
# # enumerate
# print(enumerate(idade)) # lazy
# print(list(enumerate(idade))) # forçando
#
# for indice,idade in enumerate(idade): #lazy
#     print(indice,idade)

#  posso desempacotar a tupla
usuarios = [
    ("weliton",35,1986),
    ("dinda",34,1987),
    ("karla",38,1983)
]

for nome,idade,ano in usuarios:
    print(nome)

for _,idade,_ in usuarios: # ignorando o resto
    print(idade)