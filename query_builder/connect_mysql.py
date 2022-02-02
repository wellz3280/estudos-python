import mysql.connector

class Conexao:
    def _dados_conn(self):
       dados = {'host':'localhost','database':'testePython','user':'root','password':''}
       return dados

    def connection(self):
        dado = self._dados_conn()
        conn = mysql.connector.connect(
            host= dado['host'],
            database = dado['database'],
            user = dado['user'],
            password = dado['password']
        )
        return conn

