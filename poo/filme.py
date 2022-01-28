from programa import Programa

class Filme(Programa):
    def __init__(self,nome,ano,duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    #um print maneiro
    def __str__(self):
        return f'{self.nome} -{self.ano} - {self.duracao} - likes {self.likes}'