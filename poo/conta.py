

class Conta:
    # construtor python
    def __init__(self,numero,titular,saldo,limite):
        print("objeto costruido {}".format(self))
        # atributos privado __atributo
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def deposita(self,valor):
        self.__saldo += valor

    # metodo privado usa __metodo
    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def saca(self,valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor de {} passou o limete".format(valor))

    def transfere(self,valor,destino):
        self.sacar(valor)
        destino.depositar(valor)

    def extrato(self):
       return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self,valor):
        self.__limite = valor

    # método estatico
    @staticmethod
    def codigo_banco():
        return {'BB':'001','CEF':'104','Bradesco':'237'}