from operator import attrgetter
from functools import  total_ordering

@total_ordering
class ContaSalario:
    def __init__(self,codigo):
        self._codigo =codigo
        self._saldo = 0

    def deposita(self,valor):
        self._saldo += valor

    def __eq__(self, other):
        if(type(other) != ContaSalario):
            return False
        return self._codigo  == other._codigo and self._saldo == other._saldo

    def __lt__(self, other):
        if(self._saldo != other._saldo):
            return self._saldo < other._saldo
        return self._codigo < other._codigo



    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo,self._saldo)


conta1 = ContaSalario(37)
conta2 = ContaSalario(32)
conta3 = ContaSalario(99)
conta1.deposita(2400)
conta2.deposita(1000)
conta3.deposita(1700)
contas = [conta1,conta2,conta3]

# print(conta1)
# print(conta2)

# print(conta1 == conta2)
# print(isinstance(conta1,ContaSalario))

# print(conta1 > conta2)

# ordenação natural usando o método __lt__
# for conta in sorted(contas):
#     print(conta)

# for conta in sorted(contas,key=attrgetter("_saldo","_codigo")):
#     print(conta)

# usando o __lt__
for conta in sorted(contas):
    print(conta)