from flask import Flask, request, jsonify
from flask_cors import CORS
# import db_cardapio
import traceback

app = Flask(__name__)
CORS(app)  

@app.route("/cardapio", methods=["GET"])
def get_cardapio():
    
    cardapio_data = db_cardapio.get_cardapio()
    return jsonify(cardapio_data)

@app.route("/cardapio", methods=["POST"])
def insere_cardapio():
    try:
        dado = request.json
        db_cardapio.insert_cardapio(dado) 
        return jsonify({"msg": "Item de cardápio inserido com sucesso"}), 201
    except Exception as erro:
        traceback.print_exc()
        return jsonify({"msg": "Erro de sistema"}), 500

if __name__ == "__main__":
    app.run(debug=True)
