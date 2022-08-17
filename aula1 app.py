from flask import Flask, render_template
app = Flask("projeto")

#Rota primaria
@app.route("/")
def ola_mundo():   
    nome = "Vinicius Saviello"
    produtos = [{"nome": "Ração", "preco": 199.90},
    {"nome": "Console Atual", "preco": 4499.00}]

    return render_template("alo.html", n=nome, aProdutos=produtos), 200
#Rota nova
@app.route("/teste")
@app.route("/teste/<variavel>")
def funcao_teste(variavel=""):
    return "Nova rota teste<br>Variavel: {}".format(variavel), 200 



app.run()