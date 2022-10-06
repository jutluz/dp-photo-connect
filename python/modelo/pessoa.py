from geral.config import *

class Pessoa(db.Model):
    #colunas
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    senha = db.Column(db.String(254))

    #função de retornar em texto
    def __str__(self):
        return self.nome + "[id="+str(self.id)+ "], " +\
            self.email + ", " + self.senha

    #função de transformar os atributos em json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha
        }
