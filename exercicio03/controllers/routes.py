from flask import render_template, request, redirect, url_for
import json
import urllib.request
from models.database import db, Modelo, Acessorio

def init_app(app):
    
    @app.route("/")
    def home():
        return render_template("index.html")

    
    @app.route('/modelos', methods=['GET', 'POST'])
    def modelos_celular():
        
        page = request.args.get('page', 1, type=int)
        per_page = 5  
        
        if request.method == 'POST':
            nome = request.form['nome']
            lancamento = request.form.get('lancamento')
            fabricante = request.form.get('fabricante')
            
            novo_modelo = Modelo(nome=nome, lancamento=lancamento, fabricante=fabricante)
            db.session.add(novo_modelo)
            db.session.commit()
            return redirect(url_for('modelos_celular'))
        
        # CONSULTA PAGINADA
        modelos_paginados = Modelo.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return render_template('modelos.html', modelos=modelos_paginados)

    @app.route('/modelos/delete/<int:id>', methods=['POST'])
    def delete_modelo(id):
        modelo = Modelo.query.get(id)
        if modelo:
            db.session.delete(modelo)
            db.session.commit()
        return redirect(url_for('modelos_celular'))

    @app.route('/modelos/edit/<int:id>', methods=['GET', 'POST'])
    def edit_modelo(id):
        modelo = Modelo.query.get_or_404(id)
        
        if request.method == 'POST':
            modelo.nome = request.form['nome']
            modelo.lancamento = request.form.get('lancamento')
            modelo.fabricante = request.form.get('fabricante')
            
            db.session.commit()
            return redirect(url_for('modelos_celular'))
        
        return render_template('edit_modelo.html', modelo=modelo)

    
    @app.route('/acessorios', methods=['GET', 'POST'])
    def acessorios_celular():
        
        page = request.args.get('page', 1, type=int)
        per_page = 5
        
        if request.method == 'POST':
            nome = request.form['nome']
            tipo = request.form['tipo']
            preco = request.form['preco']
            modelo_id = request.form.get('modelo_id')  # NOVO CAMPO
            
            novo_acessorio = Acessorio(
                nome=nome, 
                tipo=tipo, 
                preco=preco, 
                modelo_id=modelo_id if modelo_id else None
            )
            db.session.add(novo_acessorio)
            db.session.commit()
            return redirect(url_for('acessorios_celular'))
        
        acessorios_paginados = Acessorio.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        modelos = Modelo.query.all()
        return render_template('acessorios.html', 
                             acessorios=acessorios_paginados, 
                             modelos=modelos)

    @app.route('/acessorios/edit/<int:id>', methods=['GET', 'POST'])
    def edit_acessorio(id):
        acessorio = Acessorio.query.get_or_404(id)
        modelos = Modelo.query.all()  
        
        if request.method == 'POST':
            acessorio.nome = request.form['nome']
            acessorio.tipo = request.form['tipo']
            acessorio.preco = request.form['preco']
            acessorio.modelo_id = request.form.get('modelo_id')  
            db.session.commit()
            return redirect(url_for('acessorios_celular'))
        
       
        return render_template('edit_acessorio.html', acessorio=acessorio, modelos=modelos)
    
    @app.route('/acessorios/delete/<int:id>', methods=['POST'])
    def delete_acessorio(id):
        acessorio = Acessorio.query.get_or_404(id)
        db.session.delete(acessorio)
        db.session.commit()
        return redirect(url_for('acessorios_celular'))
            
    @app.route('/clientes')
    def clientes():
        url = 'https://jsonplaceholder.typicode.com/users'
        response = urllib.request.urlopen(url)
        data = response.read()
        clientes = json.loads(data)
        return render_template('clientes.html', clientes=clientes)