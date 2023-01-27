from banco import Acesso_banco

banco = Acesso_banco.Banco_de_dados()
banco.conectar()

def carrega_eventos():
    banco.db.commit()
    eventos = banco.recupera_evento()
    return eventos