
idades = [45,87,99,1,21,444,556]

# ordenando
# sorted e reverse não alteram o idades no endereco de meméria
ordenando = sorted(idades)
print(ordenando)


revertendo = sorted(idades,reverse=True)
print(revertendo)

# ordena direto no endereço de idades
idades.sort()
print(idades)