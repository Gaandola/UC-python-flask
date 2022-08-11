from flask import Flask, render_template
app = Flask("projeto")
@app.route("/")
def ola_mundo():   
    nome = "Vinicius Saviello"
    produtos = [{"nome": "Ração", "preco": 199.90},
    {"nome": "Console Atual", "preco": 4499.00}]

    return render_template("alo.html", n=nome, aProdutos=produtos), 200

app.run()