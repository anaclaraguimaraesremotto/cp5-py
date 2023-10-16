from flask import Flask, request, jsonify
from flask_cors import CORS
import db_cardapio
import traceback

app = Flask(__name__)
CORS(app)

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
        db_cardapio.insere_cardapio(dado)
        return jsonify({"msg": "Prato inserido com sucesso"}), 201
    except Exception as erro:
        traceback.print_exc()
        return jsonify({"msg": "Erro de sistema"}), 406

@app.route("/cardapio/<int:id>", methods=["DELETE"])
def delete_prato(id):
    try:
        db_cardapio.delete_cardapio(id) 
        return jsonify({"msg": "Prato deletado com sucesso"}), 200
    except Exception as erro:
        traceback.print_exc()
        return jsonify({"msg": "Erro na deleção"}), 404

@app.route("/cardapio/<int:id>", methods=["PUT"])
def update_prato(id):
    try:
        dado = request.json
        db_cardapio.update_cardapio(id, dado)
        return jsonify({"msg": "Prato atualizado com sucesso"}), 200
    except Exception as erro:
        traceback.print_exc()
        return jsonify({"msg": "Erro na atualização"}), 406

if __name__ == "__main__":
    app.run(debug=True)