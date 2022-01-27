import getpass

class Senha:
    def __init__(self,email,senha):
        self._email = email
        self._senha = senha

    def verifica_informacoes(self):
        if(self._email == 'weliton@weliton.com'
        and self._senha == '123456'):
            print('Bem vindo, pupunhalover')
        else:
            print('vaza caraio')


print('******** Bem vinho pupunhante +++++++++')
usuario = input('Email: ')
senha =getpass.getpass('senha: ')

teste = Senha(usuario,senha)
teste.verifica_informacoes()