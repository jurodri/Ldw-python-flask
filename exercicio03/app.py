from flask import Flask, render_template
from controllers import routes
from models.database import db
import os

app = Flask(__name__, template_folder='views')
routes.init_app(app)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_NAME = 'projects.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(BASE_DIR, DB_NAME)}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
        print(f'Banco de dados SQLite criado com sucesso: {DB_NAME}')
    
    app.run(host='0.0.0.0', port=4000, debug=True)