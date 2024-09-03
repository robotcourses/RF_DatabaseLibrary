"""
Este módulo contém funções/keywords para geração de Strings SQL para manipulação de dados na tabela 'users'.
"""


def sql_select_users(id=None, nome=None, email=None, idade=None):
    """
    Gera um SQL SELECT para recuperar usuários da tabela 'users' com base nos critérios fornecidos.

    Argumentos:

        id (int, optional): O ID do usuário a ser pesquisado.
        nome (str, optional): O nome do usuário a ser pesquisado.
        email (str, optional): O e-mail do usuário a ser pesquisado.
        idade (int, optional): A idade do usuário a ser pesquisado.

    Retornos:

        str: A consulta SQL SELECT completa com as condições de filtragem apropriadas.
        
    Exemplos:

        ${sql}  |  Sql Select Users
        -> "SELECT * FROM users"
    
        OU
            
        ${sql}  |  Sql Select Users  |  id=1
        -> "SELECT * FROM users WHERE id=1"

        OU

        ${sql}  |  Sql Select Users  |  nome=Alice  |  idade=30
        -> "SELECT * FROM users WHERE nome = 'Alice' AND idade = 30;"
    """
    sql = "SELECT * FROM users"

    conditions = []

    if id is not None:
        conditions.append(f"id = {id}")
    if nome is not None:
        conditions.append(f"nome = '{nome}'")
    if email is not None:
        conditions.append(f"email = '{email}'")
    if idade is not None:
        conditions.append(f"idade = {idade}")

    if conditions:
        sql += " WHERE " + " AND ".join(conditions)

    return sql + ";"

def sql_insert_user(nome, email, idade):
    """
    Gera um SQL INSERT para adicionar um novo usuário à tabela 'users'.

    Argumentos:

        nome (str): O nome do novo usuário.
        email (str): O e-mail do novo usuário.
        idade (int): A idade do novo usuário.

    Retornos:

        str: A consulta SQL INSERT completa para adicionar o usuário.

    Exemplos:

        ${sql}  |  Sql Insert User  |  nome=Teste  |  email=teste@teste.com.br  |  idade=36
        -> "INSERT INTO users (nome, email, idade) VALUES ('Eve', 'teste@teste.com.br', 36);"
    """
    sql = f"INSERT INTO users (nome, email, idade) VALUES ('{nome}', '{email}', {idade});"

    return sql

def sql_update_user(id, nome=None, email=None, idade=None):
    """
    Gera um SQL UPDATE para modificar os dados de um usuário existente na tabela 'users'.

    Argumentos:
        id (int): O ID do usuário a ser atualizado.
        nome (str, optional): O novo nome do usuário.
        email (str, optional): O novo e-mail do usuário.
        idade (int, optional): A nova idade do usuário.

    Retornos:

        str: A consulta SQL UPDATE completa para atualizar o usuário.

    Raises:

        ValueError: Se nenhum dos campos opcionais 'nome', 'email' ou 'idade' for fornecido.

    Exemplos:

        ${sql}  |  Sql Update User  |  id=1 |  nome=Teste
        -> "UPDATE users SET nome = 'Teste' WHERE id = 1;"
    """
    updates = []

    if nome is not None:
        updates.append(f"nome = '{nome}'")
    if email is not None:
        updates.append(f"email = '{email}'")
    if idade is not None:
        updates.append(f"idade = {idade}")

    if not updates:
        raise ValueError("Pelo menos um dos campos 'nome', 'email' ou 'idade' deve ser fornecido para o comando UPDATE.")
    
    sql = f"UPDATE users SET {', '.join(updates)} WHERE id = {id};"
    
    return sql

def sql_delete_users(id=None, nome=None, email=None, idade=None):
    """
    Gera um SQL DELETE para remover usuários da tabela 'users' com base nos critérios fornecidos.

    Argumentos:

        id (int, optional): O ID do usuário a ser removido.
        nome (str, optional): O nome do usuário a ser removido.
        email (str, optional): O e-mail do usuário a ser removido.
        idade (int, optional): A idade do usuário a ser removido.

    Retornos:

        str: A consulta SQL DELETE completa com as condições de filtragem apropriadas.

    Exemplos:

        ${sql}  |  Sql Delete Users  |  id=1
        -> "DELETE FROM users WHERE id=1"

        OU

        ${sql}  |  Sql Delete Users  |  nome=Teste  |  idade=30
        -> "DELETE FROM users WHERE nome = 'Teste' AND idade = 30;"
    """
    sql = "DELETE FROM users"

    conditions = []

    if id is not None:
        conditions.append(f"id = {id}")
    if nome is not None:
        conditions.append(f"nome = '{nome}'")
    if email is not None:
        conditions.append(f"email = '{email}'")
    if idade is not None:
        conditions.append(f"idade = {idade}")

    if conditions:
        sql += " WHERE " + " AND ".join(conditions)

    return sql + ";"
