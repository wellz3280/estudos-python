
class Cliente:
    # getters e setters
    # os metodos tem que ter o mesmo nome do atributo
    def __init__(self, nome):
        self.__nome = nome

    @property # getter
    def nome(self):
        return self.__nome.title()

    @nome.setter # setter
    def nome(self,nome):
        self.__nome = nome