from geral.config import *

class Arquivos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nomearq = db.Column(db.String(50))
    dados = db.Column(db.LargeBinary)
