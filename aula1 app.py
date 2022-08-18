from flask import Flask, render_template,request,session,redirect,url_for
app = Flask("projeto")
app.secret_key= "WEQUODSAJOISF1239D0A909s0akif" #criar uma chave de criptografia


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



@app.route("/login") #Rota do form de login
def login():
    return render_template("login.html"),200

@app.route("/login_validar",methods=["POST"]) #rota para validar login/senha
def login_validar():
    if request.form["usuario"] == "vinicius" and request.form["senha"] == "123":
        session["usuario"]= request.form["usuario"]
        session["codigo"] = 1
        return redirect(url_for("acesso_restrito"))

    else:
        return "Login/senha inválidos, digite novamente", 200

@app.route("/restrito") #rota para area restrita
def acesso_restrito():
    if session["codigo"] == 1:
        return "Bem vindo à area restrita <br> Usuário :{} <br> Código: {}".format(session["usuario"], session["codigo"]), 200
    else: 
        return "Acesso Inválido" , 200
app.run()