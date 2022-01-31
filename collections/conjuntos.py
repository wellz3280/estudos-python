# contexto , enviar email para duas turmas diferentes

# curso_usuarios_data_scince = [15,45,23,56]
# curso_usuarios_machine_learning = [13,56,23,42]

# assistiram = []
# assistiram.extend(curso_usuarios_data_scince)

# fazendo uma copia da lista
# assistiram = curso_usuarios_data_scince.copy()

# extendendo lista a partir da cópia
# assistiram.extend(curso_usuarios_machine_learning)

# conjunts são reprensentado por varios elementos que não possui elementos repetidos

# set(cria um conjunto)
# print(set(assistiram), len(set(assistiram)))

# é possivel criar um conjunto diretamente usando chaves {}
conjunto_data_scince = {15,45,23,56}
# conjunto não possuem posição
# exemplo conjunto_data_scince[0] não há indexação

conjunto_machine_learning = {13,56,23,42}
# unindo os dois conjuntos usando o operador ou |
print(conjunto_data_scince | conjunto_machine_learning,"unindo conjuntos")

# pegando apenas os elementos iguais de um conjunto usuando o operador &
print(conjunto_data_scince & conjunto_machine_learning," Pegando apenas os iguais")
print(conjunto_data_scince - conjunto_machine_learning,"pegando apenas os não repetidos")
print(conjunto_data_scince ^ conjunto_machine_learning,"ou exclusivo")
# conjuntos são iteráraveis
# for usuario in set(assistiram):
#     print(f'usuario: {usuario}')
