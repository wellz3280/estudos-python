import re
class ExtratorUrl:
    def __init__(self,url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self,url):
        if(type(url) == str):
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if(not self.url):
            raise ValueError('Url esta vazia')

        # expressões regulares
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        math = padrao_url.match(url)

        if(not math):
            raise ValueError('url não é valida')

    def _url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_param(self,param):
        parametro_busca = param
        url_param = self._url_parametros()
        indice_parametro = url_param.find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = url_param.find('&', indice_valor)

        if indice_e_comercial == -1:
            valor = url_param[indice_valor:]
        else:
            valor = url_param[indice_valor:indice_e_comercial]

        return valor

    def __len__(self):
        return len(self.url)

    def __eq__(self, other):
        return self.url == other.url

class Converte:
    def __init__(self,moeda_origem,moeda_destino,valor):
        self.moeda_origem = moeda_origem
        self.moeda_destino = moeda_destino
        self.valor = valor

    def _cotacao_dolar(self):
        return 5.50

    def _cotacao_euro(self):
        return 6.03

    def coverte(self):
        if(self.moeda_destino == 'dolar'):
            dolar = float(self._cotacao_dolar())
            conversao = float(self.valor) / dolar
            print("O valor Dolar: {:.2f}".format(conversao))

        elif(self.moeda_destino == 'euro'):
            euro = float(self._cotacao_euro())
            conversao = float(self.valor) / euro
            print("O valor Euro: {:.2f}".format(conversao))

        else:
            print('Não hà conversão para esta moéda')



url = "bytebank.com/cambio?quantidade=1000&moedaOrigem=real&moedaDestino=chingling"
# url = None
parametro = ExtratorUrl(url)
quantidade = parametro.get_param('quantidade')
moeda_origem = parametro.get_param('moedaOriegm')
moeda_destino = parametro.get_param('moedaDestino')

converte = Converte(moeda_origem,moeda_destino,quantidade).coverte()

