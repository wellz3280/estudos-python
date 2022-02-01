import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    database='testePython',
    user='root',
    password=''
)

if(conn.is_connected()):
    db_info = conn.get_server_info()
    print(f'Conectado ao Mysql versão {db_info}')
    cursor = conn.cursor()
    cursor.execute('SELECT database();')
    linha = cursor.fetchone()
    print(f'Conectado ao banco de dados {linha}')

if(conn.is_connected()):
    cursor.close()
    conn.close()
    print(f'Conexão ao Mysql foi encerrada')
