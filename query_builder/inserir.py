from query_builder import QueryBuilder
from connect_mysql import Conexao
from mysql.connector import Error

class Inserir(QueryBuilder):
    def __init__(self,table,data):
        super().__init__(table,data)
        self.conn = Conexao()

    def _sql(self):
        key = self._dados_chave()
        valor = self._dados_valores()
        campos = ",".join(key)
        valores = "','".join(valor)
        sql = "INSERT INTO " + self._tabela + " (" + campos + ") VALUES ('" + valores + "');"

        return sql

    def get(self):
        try:
            sql = self._sql()
            conn = self.conn.connection()
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            print(f'{cursor.rowcount} linha(s) afetada(s)')
            cursor.close()
        except Error as erro:
            print(f'Falha ao inserir dados ao banco {erro}')
        finally:
            if (conn.is_connected()):
                conn.close()
                print("conexao finalizada")