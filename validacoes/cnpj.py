from validate_docbr import CNPJ

class Cnpj:
    def __init__(self, documento):
        if (self.valida(documento)):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ Inválido')

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)