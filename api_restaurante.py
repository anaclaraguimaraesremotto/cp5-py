from flask import Flask, request
from flask_cors import CORS
import db_cardapio
import traceback

app = Flask(__name__)

CORS(app)

@app.route("/cardapio", methods=["POST"])
def insere_cardapio():
    try:
        dado = request.json
        db_cardapio.insert_cardapio(dado)
        return dado, 200
    except Exception as erro:
        traceback.print_exc()
        info = {"msg" : "Erro de sistema"}
        return info, 406
    
app.run(debug=True)