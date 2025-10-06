from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Modelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    lancamento = db.Column(db.Integer)
    fabricante = db.Column(db.String(100))
    
  
    acessorios = db.relationship('Acessorio', backref='modelo', lazy=True)

class Acessorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Float, nullable=False)
   
    modelo_id = db.Column(db.Integer, db.ForeignKey('modelo.id'), nullable=True)