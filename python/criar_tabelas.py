from geral.config import *
from modelo.pessoa import *

if __name__ == "__main__":
    #db.drop_all()
    #print("Tabelas excluídas")
    
    db.create_all()
    print("Tabelas criadas")