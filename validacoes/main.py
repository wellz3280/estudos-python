import re
# fatiando string
# fatia_um = self.cpf[:3]
# fatia_dois = self.cpf[3:6]
#fatia_tres = self.cpf[6:9]
#fatia_quatro = self.cpf[9:]

# from factory_documento import Documento
# # valida= Documento.cria_documento("40550000000180")
# valida= Documento.cria_documento("36529972803")
#
# print(valida)

# padrao_email = '\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}'
# texto = "aaaaaaaaa weliton@gmail.com"
# resposta = re.search(padrao_email,texto)
# print(resposta.group())

from telefones_br import TelefoneBr

telefone = "552126481234"

teste = TelefoneBr(telefone)

print(teste)