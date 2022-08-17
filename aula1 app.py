from flask import Flask, render_template,request
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

#Rota para o formulário
@app.route ("/form")
def form():
    return render_template("form.html"),200

#Rota tratamento do form
@app.route("/form_recebe", methods= ["GET","POST"])
def form_recebe():
    nome=""
    if request.method == "POST":
        nome= request.form["nome"]
        return "Nome: {}".format(nome),200
    else:
        return "Não chamar direto no GET", 200
    
app.run()