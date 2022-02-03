from cpf import Cpf
from cnpj import Cnpj

class Documento: #factory para validação de documentos

    @staticmethod
    def cria_documento(documento):
        if(len(documento) == 11):
            return Cpf(documento)
        elif(len(documento) == 14):
            return Cnpj(documento)
        else:
            raise ValueError('Quantidade de digitos esta errada!!')