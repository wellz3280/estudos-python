class Programa:
    def __init__(self, nome, ano):
        self._nome = nome
        self.ano = ano
        self._likes = likes = 0

    @property
    def nome(self):
        return self._nome.title()

    @property
    def likes(self):
        return self._likes

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f'{self.nome} -{self.ano} - likes {self.likes}'