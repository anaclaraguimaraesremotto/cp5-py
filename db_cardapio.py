import oracledb
import traceback

def insert_cardapio(prato):
    insert = '''insert into cardapio( id, nome_prato, ingredientes, valor)
                values(:id, :nome_prato, :ingredientes, :valor)'''
    
    try:
        with oracledb.connect(
            user="rm97898", password="210904",
            dsn="oracle.fiap.com.br/orcl"
        ) as conexao:

            with conexao.cursor() as cur:
                cur.execute(insert, prato)
            conexao.commit()

    except Exception as erro:
        traceback.print_exc()
        raise erro
    
if __name__ == '__main__':
    p = {"id": 150, "nome_prato": "misto quente", 
         "ingredientes": "pão, presunto e queijo", "valor": 13.00}
    insert_cardapio(p)
