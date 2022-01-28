import array as arr
import numpy as np
from operator import attrgetter

# para definir esta classe como abstrata
from abc import ABCMeta,abstractmethod
# herançãs
class Conta(metaclass=ABCMeta):
    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self,valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return f'>> Codigo {self._codigo} Saldo {self._saldo} <<'


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    def passa_o_mes(self):
        pass

conta28 = ContaInvestimento(28)

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)

# polimorfirmo
contas =[conta16,conta17]

for conta in contas:
    conta.passa_o_mes() # duck typing
    print(conta)

# array, evitaremos usar array puro
# se precisarmos usar com numeros usamos o numpy

arr.array('d',[1.0,3.5])

numeros = np.array([1,3.5])
numeros += 3
print(numeros)