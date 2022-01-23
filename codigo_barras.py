print("**********Scaneie o produto*********")


produto = "ameixa seca"
cod_ameixa = 123456789
valor = 12.95

escaneado_str = input("Escaneie o Produto: ")
escaneado_int = int(escaneado_str)

if(escaneado_int == cod_ameixa):
    print("Produto {} R$ {:.2f}".format(produto,valor))
else:
    print("Tente Novamente Por favor")

