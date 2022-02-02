from abc import ABCMeta,abstractmethod

class QueryBuilder(metaclass=ABCMeta):
    def __init__(self,tabela,data):
        self._tabela = tabela
        self._data = data

    def _dados_chave(self):
        data = self._data
        key = []
        for chave in data.keys():
            key.append(chave)
        return key

    def _dados_valores(self):
        data = self._data
        valor = []
        for valores in data.values():
            valor.append(valores)
        return valor

