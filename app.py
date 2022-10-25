from flask import Flask
from flask_cors import CORS
from api.cliente_service import cliente
from api.fornecedor_service import fornecedor

app = Flask(__name__)
CORS(app,resources={r"/*":{"origins":"*"}})

#
# REGISTRAR AS ROTAS
#
app.register_blueprint(cliente,url_prefix='/api/cliente')
app.register_blueprint(fornecedor,url_prefix='/api/fornecedor')
#
# OPERAÇÕES
#
@app.route("/")
def info():
    return "API v.1.0"

if __name__ == "__main__":
    app.run(debug=True,host="127.0.0.1", port=5000)