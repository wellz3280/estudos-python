from programa import Programa

class Serie(Programa):
    def __init__(self,nome,ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome} -{self.ano}- {self.temporadas} - likes {self.likes}'