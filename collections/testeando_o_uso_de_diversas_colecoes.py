from collections import Counter

texto1 = """""
    EUA e Rússia trocam farpas na ONU pela crise da Ucrânia
A reunião do Conselho de Segurança ocorre diante do crescente medo de uma invasão iminente da Rússia na Ucrânia.
Rússia e Estados Unidos se enfrentaram nesta segunda-feira (31) no Conselho de Segurança das Nações Unidas devido à concentração de tropas russas na fronteira com a Ucrânia, enquanto o Ocidente intensifica as ameaças de sanções para evitar um conflito na Europa.

Diante da escalada das tensões, os Estados Unidos estão dispostos a desmentir qualquer "desinformação" de Moscou em uma das sessões das Nações Unidas que gerou mais expectativas em anos.


"""""

texto2 = """""
    Polícia Federal diz que Bolsonaro não cometeu prevaricação no caso Covaxin
PF entendeu que não cabe ao presidente comunicar eventuais crimes a órgãos de 
controle. Investigação começou depois que irmãos Miranda contaram que relataram a Bolsonaro suspeitas na compra da vacina indiana.
A Polícia Federal concluiu que o presidente Jair Bolsonaro não praticou o crime de prevaricação no caso da negociação para compra da vacina indiana Covaxin.

As investigações têm como base os depoimentos dados à CPI da Covid pelo funcionário do Ministério da Saúde Luís Ricardo Miranda e pelo irmão dele, o deputado federal Luis Miranda (DEM-DF).

"""""
def analisa_frequencia_de_letras(texto,frequencia):
    aparicoes = Counter(texto.lower())
    total_de_caracters = sum(aparicoes.values())

    proporcoes = [(letra,frequencia/total_de_caracters) for letra,frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(frequencia)
    for caractere,proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere,proporcao *100))


analisa_frequencia_de_letras(texto1,10)
analisa_frequencia_de_letras(texto2,10)
