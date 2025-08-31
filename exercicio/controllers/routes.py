from flask import render_template, request, redirect, url_for

def init_app(app): 
    # Lista em Python (array) - modelos de celular
    modelos = ["iPhone 15", "Samsung Galaxy S23", "Xiaomi Redmi Note 12", "Motorola Edge 40"]
    acessorios = [{'Nome': 'Capa Protetora', 'Tipo': 'Proteção', 'Preço': 'R$ 49,90'}]
        
    # Definindo a rota principal da aplicação "/"
    @app.route("/")
    def home():  # Função que será executada ao acessar a rota
        return render_template("index.html")

    @app.route("/modelos", methods=['GET', 'POST'])
    def modelos_celular():
        modelo_destaque = "iPhone 15 Pro"
        lancamento = 2023
        fabricante = "Apple"
        
        # Dicionário em Python (objeto)
        fabricante_info = {"Nome": "Apple", "País": "EUA", "Fundação": 1976}
        
        # Tratando uma requisição post
        if request.method == 'POST':
            # Coletando o texto da Input
            if request.form.get('modelo'):
                modelos.append(request.form.get('modelo'))
                return redirect(url_for('modelos_celular'))
                
        return render_template("modelos.html", modelo_destaque=modelo_destaque, 
                              lancamento=lancamento, fabricante=fabricante, 
                              modelos=modelos, fabricante_info=fabricante_info)
   
    @app.route('/acessorios', methods=['GET', 'POST'])
    def acessorios_celular():
        # Tratando a requisição POST
        if request.method == 'POST':
            if request.form.get('nome') and request.form.get('tipo') and request.form.get('preco'):
                acessorios.append({
                    'Nome': request.form.get('nome'), 
                    'Tipo': request.form.get('tipo'),
                    'Preço': request.form.get('preco')
                })
                return redirect(url_for('acessorios_celular'))
                
        return render_template('acessorios.html', acessorios=acessorios)