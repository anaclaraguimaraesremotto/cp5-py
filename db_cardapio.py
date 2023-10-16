import oracledb
import traceback

def recupera_cardapio():
    sql = "SELECT * FROM cardapio"
    try:
        with oracledb.connect(
            user="rm97898", password="21092004", 
            dsn="oracle.fiap.com.br/orcl"
        ) as conexao:
            with conexao.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
    except Exception as erro:
        traceback.print_exc()
        raise erro

def insere_cardapio(prato):
    ins = '''INSERT INTO cardapio(id, nome_prato, ingredientes, preco)
             VALUES(:id, :nome_prato, :ingredientes, :preco)'''
    try:
        with oracledb.connect(
            user="rm97898", password="21092004", 
            dsn="oracle.fiap.com.br/orcl"
        ) as conexao:
            with conexao.cursor() as cur:
                cur.execute(ins, prato)
            conexao.commit()
    except Exception as erro:
        traceback.print_exc()
        raise erro

def delete_cardapio(id):
    delete_sql = "DELETE FROM cardapio WHERE id = :id"
    try:
        with oracledb.connect(
            user="rm97898", password="21092004",
            dsn="oracle.fiap.com.br/orcl"
        ) as conexao:
            with conexao.cursor() as cur:
                cur.execute(delete_sql, {"id": id})
            conexao.commit()
    except Exception as erro:
        traceback.print_exc()
        raise erro

def update_cardapio(id, prato):
    update_sql = '''
        UPDATE cardapio
        SET nome_prato = :nome_prato,
            ingredientes = :ingredientes,
            preco = :preco
        WHERE id = :id
    '''
    try:
        with oracledb.connect(
            user="rm97898", password="21092004",
            dsn="oracle.fiap.com.br/orcl"
        ) as conexao:
            with conexao.cursor() as cur:
                prato["id"] = id
                cur.execute(update_sql, prato)
            conexao.commit()
    except Exception as erro:
        traceback.print_exc()
        raise erro