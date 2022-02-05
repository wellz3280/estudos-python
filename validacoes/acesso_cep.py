import requests

class BuscaEndereco:
    def __init__(self,cep):
        cep = str(cep)
        if(self.cep_eh_valido(cep)):
            self.cep = cep
        else:
            raise ValueError("Cep Inválido")
    def __str__(self):
        return self.format_cep()
    def cep_eh_valido(self,cep):
        if(len(cep)==8):
            return  True
        else:
            return False

    def format_cep(self):
        return "{}-{}".format(self.cep[:5],self.cep[5:])

    # acessando api do via cep
    def acessa_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json".format(self.cep)
        resposta = requests.get(url)
        dados = resposta.json()
        return {
            dados['logradouro'],
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        }


cep = "01105030"

busca = BuscaEndereco(cep)

logradouro,bairro,cidade,uf = busca.acessa_via_cep()
print(logradouro,bairro,cidade,uf)