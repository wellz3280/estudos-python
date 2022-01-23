print("*********************************")
print("bem vindo ao jogo de adivinhação")
print("*********************************")

numero_secreto = 42
# A funcão input sempre devolve uma string
chute = input("digite o seu numero: ")

# funcão int() converte string para inteiro
nunero_digitado = int(chute)

if(numero_secreto == nunero_digitado):
    print("voce acertou")
else:
    print("voce errou")

print("fim do jogo")