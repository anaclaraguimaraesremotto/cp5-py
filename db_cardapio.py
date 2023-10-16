import cx_Oracle
import traceback

def recupera_cardapio():
    sql = "SELECT * FROM cardapio"
    try:
        with cx_Oracle.connect(
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
        with cx_Oracle.connect(
            user="rm97898", password="21092004", 
            dsn="oracle.fiap.com.br/orcl"
        ) as conexao:
            with conexao.cursor() as cur:
                cur.execute(ins, prato)
            conexao.commit()
    except Exception as erro:
        traceback.print_exc()
        raise erro

if __name__ == '__main__':
    prato = {
        "id": 100,
        "nome_prato": "Nome do Prato",
        "ingredientes": "Lista de Ingredientes",
        "preco": 20.50,
    }
    
    try:
        insere_cardapio(prato)
        print("Prato inserido com sucesso.")
    except Exception as erro:
        print("Erro ao inserir o prato:", erro)
    
    cardapios = recupera_cardapio()
    print("Pratos no banco de dados:")
    for prato in cardapios:
        print(prato)
