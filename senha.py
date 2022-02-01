import getpass

class Senha:
    def __init__(self,email,senha):
        self._email = email
        self._senha = senha

    def verifica_informacoes(self):
        if(self._email == 'weliton@weliton.com'
        and self._senha == '123456'):
            print('logado com sucesso')
        else:
            print('Usuario ou senha invalido')


print('******** Bem vinho Cliente +++++++++')
usuario = input('Email: ')
senha =getpass.getpass('senha: ')

teste = Senha(usuario,senha)
teste.verifica_informacoes()