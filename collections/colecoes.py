
weliton = {"nome":"weliton","idade":35}
idades = [18,17,22,44,55,78,100]
idades.insert(0,20)
outras_idades = [56,99]
idades.extend(outras_idades)
print(idades)
idade =[(idade) for idade in idades if idade > 21]

print(idade)

def vizaaliza_lista(lista = None):
    if(lista == None):
        lista = list()

