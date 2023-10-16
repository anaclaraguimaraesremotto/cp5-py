from flask import Flask, request, jsonify
from flask_cors import CORS
import db_cardapio
import traceback

app = Flask(__name__)
# CORS(app)

@app.route("/cardapio", methods=["GET"])
def get_all():
    try:
        dados = db_cardapio.recupera_cardapio() 
        resposta = []
        for registro in dados:
            prato = {
                "id": registro[0],
                "nome_prato": registro[1],
                "ingredientes": registro[2],
                "preco": float(registro[3])  
            }
            resposta.append(prato)
            
        return jsonify(resposta), 200
    except Exception as erro:
        traceback.print_exc()
        return jsonify({"msg": "Erro na recuperação"}), 404

@app.route("/cardapio", methods=["POST"])
def insere_prato():
    try:
        dado = request.json
        db_cardapio.insert_prato(dado)
        return jsonify({"msg": "Prato inserido com sucesso"}), 201
    except Exception as erro:
        traceback.print_exc()
        return jsonify({"msg": "Erro de sistema"}), 406

if __name__ == "__main__":
    app.run(debug=True)
