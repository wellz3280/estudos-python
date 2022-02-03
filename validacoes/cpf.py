from validate_docbr import CPF

class Cpf:
    def __init__(self,documento):
        if(self.valida(documento)):
            self.cpf = documento
        else:
            raise ValueError('CPF Inválido')

    def __str__(self):
        return self.format()

    def valida(self,documento):
        validador = CPF()
        return validador.validate(documento)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)



