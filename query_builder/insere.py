import mysql.connector
from query_builder import QueryBuilder
from mysql.connector import Error
from connect_mysql import Conexao

continuar = False
while(not continuar):
    print(" Cadastrar usuario ")
    nome = input("digite o nome no usuario: ").capitalize()
    email = input("Digite o email: ").lower()
    data = {"nome": nome, "email": email}
    query = QueryBuilder('usuarios',data).get()
    continuar_inserindo = input('Encerrar  (s) sim (n) não').upper()

    if(continuar_inserindo == 'S'):
        continuar = True

