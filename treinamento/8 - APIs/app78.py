from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Executar o comando para criar o banco de dados
def banco_de_dados(app):
    db = SQLAlchemy(app)
    db:SQLAlchemy
    return db
    
# Criar uma API flask
app = Flask(__name__)
# Criar uma instância de SQLAlchemy
app.config['SECRET_KEY'] = 'FSD24323f$@!s@'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

with app.app_context():
    db = banco_de_dados(app)
    db.drop_all()
    db.create_all()

# Definir a estrutura da tabela Postagem
# id_postagem, titulo, autor

class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))

# Definir a estrutura da tabela Autor
# id_autor, nome, email, senha, admin, postagens
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')
    
with app.app_context():
    # Criar usuários administradores
    autor = Autor(nome='João',email='João@gmail.com',senha='123',admin=True) 
    db.session.add(autor)
    db.session.commit()