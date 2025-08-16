from flask import Flask 
from markupsafe import escape
from flask import render_template
from flask import request
app = Flask (__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/anuncios')
def anuncios():
    return "Lista de anúncios"

@app.route('/compras')
def compras():
    return "Relatório de compras"

@app.route('/vendas')
def vendas():
    return "Relatório de vendas"

if __name__ == '__main__':
    app.run(debug=True)

