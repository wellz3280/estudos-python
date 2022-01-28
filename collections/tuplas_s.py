
class ContaCorrente:
    def __init__(self,codigo):
        self.codigo =codigo
        self.saldo = 0

    def deposita(self,valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self.codigo,self.saldo)

# tupla é imutavel
# tupla não é possivel usar append
# tuplas são usudas, quando as posições que tem siginificado
# exemplo = quando (x,Y) o valor de x deve ser o primeira posição
weliton = ("weliton",35,1986)
karla = ("karla",38,1983)


conta_weliton = ContaCorrente(10)
conta_weliton.deposita(500)
#
conta_nicole = ContaCorrente(54211)
conta_nicole.deposita(1000)
# lista
contas = [conta_weliton,conta_nicole]
#
for conta in contas:
    print(conta)