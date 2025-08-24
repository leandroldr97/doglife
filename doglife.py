from flask import Flask 
from markupsafe import escape
from flask import render_template
from flask import request
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
import os
from extensions import db 
from dotenv import load_dotenv

load_dotenv ()

app = Flask (__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@localhost/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
import models 

from models import Usuario, Anuncio, Categoria, Favorito , Compra , Pergunta, Resposta

with app.app_context():
    db.create_all()


@app.route('/usuarios')
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/usuarios/novo', methods=['GET', 'POST'])
def criar_usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        novo = Usuario(nome=nome, email=email, senha=senha)
        db.session.add(novo)
        db.session.commit()
        return redirect('/usuarios')
    return render_template('form_usuario.html')

@app.route('/usuarios/editar/<int:id>', methods=['GET', 'POST'])
def editar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    if request.method == 'POST':
        usuario.nome = request.form['nome']
        usuario.email = request.form['email']
        usuario.senha = request.form['senha']
        db.session.commit()
        return redirect('/usuarios')
    return render_template('form_usuario.html', usuario=usuario)

@app.route('/usuarios/deletar/<int:id>', methods=['POST'])
def deletar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect('/usuarios')



@app.route('/categorias')
def listar_categorias():
    categorias = Categoria.query.all()
    return render_template('categorias.html', categorias=categorias)

@app.route('/categorias/novo', methods=['GET', 'POST'])
def criar_categoria():
    if request.method == 'POST':
        nome_categoria = request.form['nome_categoria']
        nova = Categoria(nome_categoria=nome_categoria)
        db.session.add(nova)
        db.session.commit()
        return redirect('/categorias')
    return render_template('form_categoria.html')

@app.route('/categorias/editar/<int:id>', methods=['GET', 'POST'])
def editar_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    if request.method == 'POST':
        categoria.nome_categoria = request.form['nome_categoria']
        db.session.commit()
        return redirect('/categorias')
    return render_template('form_categoria.html', categoria=categoria)

@app.route('/categorias/deletar/<int:id>', methods=['POST'])
def deletar_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    db.session.delete(categoria)
    db.session.commit()
    return redirect('/categorias')



@app.route('/anuncios')
def listar_anuncios():
    anuncios = Anuncio.query.all()
    return render_template('anuncios.html', anuncios=anuncios)

@app.route('/anuncios/novo', methods=['GET', 'POST'])
def criar_anuncio():
    usuarios = Usuario.query.all()
    categorias = Categoria.query.all()
    if request.method == 'POST':
        novo = Anuncio(
            titulo=request.form['titulo'],
            descricao=request.form['descricao'],
            preco=float(request.form['preco']),
            id_usuario=int(request.form['id_usuario']),
            id_categoria=int(request.form['id_categoria'])
        )
        db.session.add(novo)
        db.session.commit()
        return redirect('/anuncios')
    return render_template('form_anuncio.html', usuarios=usuarios, categorias=categorias)

@app.route('/anuncios/editar/<int:id>', methods=['GET', 'POST'])
def editar_anuncio(id):
    anuncio = Anuncio.query.get_or_404(id)
    usuarios = Usuario.query.all()
    categorias = Categoria.query.all()
    if request.method == 'POST':
        anuncio.titulo = request.form['titulo']
        anuncio.descricao = request.form['descricao']
        anuncio.preco = float(request.form['preco'])
        anuncio.id_usuario = int(request.form['id_usuario'])
        anuncio.id_categoria = int(request.form['id_categoria'])
        db.session.commit()
        return redirect('/anuncios')
    return render_template('form_anuncio.html', anuncio=anuncio, usuarios=usuarios, categorias=categorias)

@app.route('/anuncios/deletar/<int:id>', methods=['POST'])
def deletar_anuncio(id):
    anuncio = Anuncio.query.get_or_404(id)
    db.session.delete(anuncio)
    db.session.commit()
    return redirect('/anuncios')



@app.route('/perguntas')
def listar_perguntas():
    perguntas = Pergunta.query.all()
    return render_template('perguntas.html', perguntas=perguntas)

@app.route('/perguntas/novo', methods=['GET', 'POST'])
def criar_pergunta():
    usuarios = Usuario.query.all()
    anuncios = Anuncio.query.all()
    if request.method == 'POST':
        nova = Pergunta(
            texto_pergunta=request.form['texto_pergunta'],
            id_usuario=int(request.form['id_usuario']),
            id_anuncio=int(request.form['id_anuncio'])
        )
        db.session.add(nova)
        db.session.commit()
        return redirect('/perguntas')
    return render_template('form_pergunta.html', usuarios=usuarios, anuncios=anuncios)

@app.route('/perguntas/editar/<int:id>', methods=['GET', 'POST'])
def editar_pergunta(id):
    pergunta = Pergunta.query.get_or_404(id)
    usuarios = Usuario.query.all()
    anuncios = Anuncio.query.all()
    if request.method == 'POST':
        pergunta.texto_pergunta = request.form['texto_pergunta']
        pergunta.id_usuario = int(request.form['id_usuario'])
        pergunta.id_anuncio = int(request.form['id_anuncio'])
        db.session.commit()
        return redirect('/perguntas')
    return render_template('form_pergunta.html', pergunta=pergunta, usuarios=usuarios, anuncios=anuncios)

@app.route('/perguntas/deletar/<int:id>', methods=['POST'])
def deletar_pergunta(id):
    pergunta = Pergunta.query.get_or_404(id)
    db.session.delete(pergunta)
    db.session.commit()
    return redirect('/perguntas')



@app.route('/respostas')
def listar_respostas():
    respostas = Resposta.query.all()
    return render_template('respostas.html', respostas=respostas)

@app.route('/respostas/novo', methods=['GET', 'POST'])
def criar_resposta():
    perguntas = Pergunta.query.all()
    if request.method == 'POST':
        nova = Resposta(
            texto_resposta=request.form['texto_resposta'],
            id_pergunta=int(request.form['id_pergunta'])
        )
        db.session.add(nova)
        db.session.commit()
        return redirect('/respostas')
    return render_template('form_resposta.html', perguntas=perguntas)

@app.route('/respostas/editar/<int:id>', methods=['GET', 'POST'])
def editar_resposta(id):
    resposta = Resposta.query.get_or_404(id)
    perguntas = Pergunta.query.all()
    if request.method == 'POST':
        resposta.texto_resposta = request.form['texto_resposta']
        resposta.id_pergunta = int(request.form['id_pergunta'])
        db.session.commit()
        return redirect('/respostas')
    return render_template('form_resposta.html', resposta=resposta, perguntas=perguntas)

@app.route('/respostas/deletar/<int:id>', methods=['POST'])
def deletar_resposta(id):
    resposta = Resposta.query.get_or_404(id)
    db.session.delete(resposta)
    db.session.commit()
    return redirect('/respostas')



@app.route('/compras')
def listar_compras():
    compras = Compra.query.all()
    return render_template('compras.html', compras=compras)

@app.route('/compras/novo', methods=['GET', 'POST'])
def criar_compra():
    usuarios = Usuario.query.all()
    anuncios = Anuncio.query.all()
    if request.method == 'POST':
        nova = Compra(
            valor_total=float(request.form['valor_total']),
            id_comprador=int(request.form['id_comprador']),
            id_anuncio=int(request.form['id_anuncio'])
        )
        db.session.add(nova)
        db.session.commit()
        return redirect('/compras')
    return render_template('form_compra.html', usuarios=usuarios, anuncios=anuncios)

@app.route('/compras/editar/<int:id>', methods=['GET', 'POST'])
def editar_compra(id):
    compra = Compra.query.get_or_404(id)
    usuarios = Usuario.query.all()
    anuncios = Anuncio.query.all()
    if request.method == 'POST':
        compra.valor_total = float(request.form['valor_total'])
        compra.id_comprador = int(request.form['id_comprador'])
        compra.id_anuncio = int(request.form['id_anuncio'])
        db.session.commit()
        return redirect('/compras')
    return render_template('form_compra.html', compra=compra, usuarios=usuarios, anuncios=anuncios)

@app.route('/compras/deletar/<int:id>', methods=['POST'])
def deletar_compra(id):
    compra = Compra.query.get_or_404(id)
    db.session.delete(compra)
    db.session.commit()
    return redirect('/compras')



@app.route('/favoritos')
def listar_favoritos():
    favoritos = Favorito.query.all()
    return render_template('favoritos.html', favoritos=favoritos)

@app.route('/favoritos/novo', methods=['GET', 'POST'])
def criar_favorito():
    usuarios = Usuario.query.all()
    anuncios = Anuncio.query.all()
    if request.method == 'POST':
        novo = Favorito(
            id_usuario=int(request.form['id_usuario']),
            id_anuncio=int(request.form['id_anuncio'])
        )
        db.session.add(novo)
        db.session.commit()
        return redirect('/favoritos')
    return render_template('form_favorito.html', usuarios=usuarios, anuncios=anuncios)

@app.route('/favoritos/editar/<int:id>', methods=['GET', 'POST'])
def editar_favorito(id):
    favorito = Favorito.query.get_or_404(id)
    usuarios = Usuario.query.all()
    anuncios = Anuncio.query.all()
    if request.method == 'POST':
        favorito.id_usuario = int(request.form['id_usuario'])
        favorito.id_anuncio = int(request.form['id_anuncio'])
        db.session.commit()
        return redirect('/favoritos')
    return render_template('form_favorito.html', favorito=favorito, usuarios=usuarios, anuncios=anuncios)

@app.route('/favoritos/deletar/<int:id>', methods=['POST'])
def deletar_favorito(id):
    favorito = Favorito.query.get_or_404(id)
    db.session.delete(favorito)
    db.session.commit()
    return redirect('/favoritos')



@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
