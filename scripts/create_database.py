import pymysql

# Configurações de conexão para o MySQL
config = {
    'user': 'rc_user',
    'password': 'rc_123',
    'host': 'localhost',
    'port': 3306,
    'database': 'rc_databaselibrary'
}

# Conectar ao banco de dados
try:
    conn = pymysql.connect(
        host=config['host'],
        user=config['user'],
        password=config['password'],
        database=config['database'],
        port=config['port']
    )
    cursor = conn.cursor()

    # Criar tabela 'users'
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        idade INT
    )
    ''')

    # Inserir alguns registros na tabela 'users'
    usuarios = [
        ('Alice', 'alice@example.com', 30),
        ('Bob', 'bob@example.com', 25),
        ('Charlie', 'charlie@example.com', 35),
        ('Diana', 'diana@example.com', 28)
    ]

    cursor.executemany('INSERT INTO users (nome, email, idade) VALUES (%s, %s, %s)', usuarios)

    # Commit das mudanças e fechamento da conexão
    conn.commit()
    print("Banco de dados e tabela criados com sucesso!")

except pymysql.MySQLError as err:
    print(f"Erro ao conectar ao MySQL: {err}")

finally:
    if conn:
        cursor.close()
        conn.close()
        print("Conexão com o MySQL foi encerrada.")
