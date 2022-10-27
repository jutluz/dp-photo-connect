from geral.config import *
from modelo.pessoa import Pessoa
from modelo.arquivos import Arquivos
from flask import Flask, render_template, request, send_file

#rota padrão
@app.route("/")
def inicio():
    return "Cadastro e login de pessoas."


@app.route("/insere_imagem", methods = ["GET", "POST"])
def index():
    if request.method == 'POST':
        file = request.files['arquivo']

        arq = Arquivos(nomearq=file.filename, dados=file.read())
        db.session.add(arq)
        db.session.commit()

        return f'Uploaded: {file.filename}'
    return render_template('index.html')

@app.route("/listar", methods = ["GET"])
def listar():
    pessoas = db.session.query(Pessoa).all()
    pessoas_em_json = [x.json() for x in pessoas]
    resposta = jsonify(pessoas_em_json)
    resposta.headers.add("Access-Allow-Controll-Origin", "*")
    return resposta

@app.route("/incluir_pessoa", methods=['POST'])
def incluir_pessoa():
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()
    print((dados))

    try:
        #verificação de campo vazio
        if dados['email'].strip() == '' or dados['senha'].strip() == '' or dados['nome'].strip() == '':
            raise Exception("Não deixe nenhum campo vazio!") #mensagem de erro
        #pega os dados da nova pessoa
        nova = Pessoa(**dados)
        #adiciona pessoa no banco
        db.session.add(nova)
        db.session.commit()
    
    except Exception as e: 
        resposta = jsonify({"resultado":"Erro", "detalhes":str(e)}) #mensagem de erro
    
    resposta.headers.add("Access-Control-Allow-Origin", "*") #permissão de origem
    return resposta

@app.route("/login", methods=['POST'])
def logar():
    #resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json(force=True)
    
    #filtrando os atributos de pessoa para verificar se os dados recebidos no login conferem com o do banco de dados
    encontrado = db.session.query(Pessoa).filter_by(email=dados['email'], senha=dados['senha']).first()
    if encontrado is not None:
        resposta = jsonify({"resultado": "ok", "detalhes": "ok"}) #tudo certo com o login :)
    else:
        print("Erro de login")
        resposta = jsonify({"resultado": "Erro", "detalhes": "login e/ou senha inválido(s)"}) #mensagem de erro
    
    resposta.headers.add("Access-Control-Allow-Origin", "*") #permissão de origem
    resposta.headers.add('Access-Control-Allow-Credentials', 'true') #cookies
    return resposta
