from extensions import db
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)

    anuncios = db.relationship('Anuncio', backref='usuario', lazy=True)
    perguntas = db.relationship('Pergunta', backref='usuario', lazy=True)
    compras = db.relationship('Compra', backref='comprador', lazy=True)
    favoritos = db.relationship('Favorito', backref='usuario', lazy=True)


class Categoria(db.Model):
    __tablename__ = 'categoria'
    id_categoria = db.Column(db.Integer, primary_key=True)
    nome_categoria = db.Column(db.String(100), nullable=False)

    anuncios = db.relationship('Anuncio', backref='categoria', lazy=True)


class Anuncio(db.Model):
    __tablename__ = 'anuncio'
    id_anuncio = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    data_publicacao = db.Column(db.DateTime, default=datetime.utcnow)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    id_categoria = db.Column(db.Integer, db.ForeignKey('categoria.id_categoria'), nullable=False)

    perguntas = db.relationship('Pergunta', backref='anuncio', lazy=True)
    compras = db.relationship('Compra', backref='anuncio', lazy=True)
    favoritos = db.relationship('Favorito', backref='anuncio', lazy=True)


class Pergunta(db.Model):
    __tablename__ = 'pergunta'
    id_pergunta = db.Column(db.Integer, primary_key=True)
    texto_pergunta = db.Column(db.Text, nullable=False)
    data_pergunta = db.Column(db.DateTime, default=datetime.utcnow)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    id_anuncio = db.Column(db.Integer, db.ForeignKey('anuncio.id_anuncio'), nullable=False)

    resposta = db.relationship('Resposta', uselist=False, backref='pergunta')


class Resposta(db.Model):
    __tablename__ = 'resposta'
    id_resposta = db.Column(db.Integer, primary_key=True)
    texto_resposta = db.Column(db.Text, nullable=False)
    data_resposta = db.Column(db.DateTime, default=datetime.utcnow)
    id_pergunta = db.Column(db.Integer, db.ForeignKey('pergunta.id_pergunta'), nullable=False, unique=True)


class Compra(db.Model):
    __tablename__ = 'compra'
    id_compra = db.Column(db.Integer, primary_key=True)
    data_compra = db.Column(db.DateTime, default=datetime.utcnow)
    valor_total = db.Column(db.Float, nullable=False)
    id_comprador = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    id_anuncio = db.Column(db.Integer, db.ForeignKey('anuncio.id_anuncio'), nullable=False)


class Favorito(db.Model):
    __tablename__ = 'favorito'
    id_favorito = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    id_anuncio = db.Column(db.Integer, db.ForeignKey('anuncio.id_anuncio'), nullable=False)

