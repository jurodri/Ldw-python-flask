# Importando o Flask
from flask import Flask, render_template
# Importando o controller (routes.py)
from controllers import routes

# Criando uma instância do Flask
app = Flask(__name__, template_folder="views", static_folder="static") 
routes.init_app(app)
# Se for executado diretamente pelo interpretador
if __name__ == "__main__":
    # Iniciando o servidor com 0000
    app.run(host="0,0,0,0", port=5000, debug=True) 
    
