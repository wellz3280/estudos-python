import re

# verificar se esta no padrao

url = "www.bytebank.com.br/cambio"
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
math = padrao_url.match(url)

if(not math):
    raise ValueError('url não é valida')
else:
    print("url valida")