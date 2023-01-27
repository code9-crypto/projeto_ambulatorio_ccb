import mysql.connector
import os

class Banco_de_dados():
    #MÉTODO PARA SE CONECTAR AO BANCO
    def conectar(self):
        self.db = mysql.connector.connect(user="root", password="qdU438MKcBAt9gVe4&Of", host="sistema", database="ambulatorio")
        self.cursor = self.db.cursor()

    #MÉTODO PARA SE DESCONECTAR DO BANCO
    def desconectar(self):
        self.cursor.close()

    #MÉTODO QUE FARÁ LOGIN NO SISTEMA
    def login_profissional(self, conta):
        select = f"select * from tb_contas_profissional where usuario = '{conta['usuario']}' and senha = '{conta['senha']}'"
        self.cursor.execute(select)
        result = self.cursor.fetchall()
        return result

    #MÉTODO QUE FARÁ A BUSCA DO NOME DO PROFISSIONAL E SEU CRM, MÉTODO USADO NAS CLASSES: FICHA_ATENDIMENTO.PY E FICHA_ATENDIMENTO_DA_CONSULTA.PY
    def recupera_profissional(self):
        select_profissional = "select concat(upper(nome_completo), rp) as identificacao from tb_profissionais"
        self.cursor.execute(select_profissional)
        result_pro = self.cursor.fetchall()
        return result_pro

    #MÉTODO QUE IRÁ CADASTRAR OS PACIENTES NO BANCO
    def cadastrar_paciente(self, dados):
        insert_paciente = f"insert into tb_pacientes (nome, idade, sexo, telefone, comum_congregacao, ministerio, cidade, estado, pais, identidade_atendido) values ('{dados['nome']}',{int(dados['idade'])},'{dados['sexo']}','{dados['tel']}','{dados['comum']}','{dados['ministerio']}','{dados['cidade']}','{dados['estado']}','{dados['pais']}', '{dados['identidade']}')"
        self.cursor.execute(insert_paciente)
        self.db.commit()
        #JÁ NO CADASTRO FAZENDO ALTERAÇÃO NO CAMPO FKPACIENTES_ATENDIMENTO
        recupera_cod_pac = f"select idpacientes from tb_pacientes where nome = '{os.environ['nome_paciente']}'"
        self.cursor.execute(recupera_cod_pac)
        result_cod = self.cursor.fetchall()
        atualiza_pac = f"update tb_pacientes set fkpacientes_atendimento = {int(result_cod[0][0])} where idpacientes = {int(result_cod[0][0])}"
        self.cursor.execute(atualiza_pac)
        self.db.commit()

    #MÉTODO QUE RECUPERA OS DADOS DO PACIENTE QUE PODEM SER REAVALIADOS E SERÁ USADO NA CLASSE REAVALIACAO.PY
    def recuperar_paciente_ja_atendido_sim(self):
        select = "select distinct nome_atendido from tb_fichas_de_atendimentos where reavaliacao = 'SIM'"
        self.cursor.execute(select)
        result_pc = self.cursor.fetchall()
        return result_pc

    # MÉTODO QUE RECUPERA OS DADOS DO PACIENTE QUE JÁ ESTÃO COM ALTA E SERÁ USADO NA CLASSE CONSULTAS.PY
    def recuperar_paciente_ja_atendido_nao(self):
        select = "select distinct nome_atendido from tb_fichas_de_atendimentos where reavaliacao = 'NAO'"
        self.cursor.execute(select)
        result_pc = self.cursor.fetchall()
        return result_pc

    #MÉTODO QUE RECUPERA O NOME DO PACIENTE E SERÁ USADA NA CLASSE FICHA_ATENDIMENTO.PY
    def recuperar_paciente(self):
        select = "select nome from tb_pacientes order by nome"
        self.cursor.execute(select)
        result_pc = self.cursor.fetchall()
        return result_pc


    #MÉTODO QUE CADASTRA OS ATENDIMENTOS
    def cadastrar_atendimento(self, ficha):
        insert_atendimento = f"insert into tb_fichas_de_atendimentos (evento, nome_atendido, data, hora, alojamento, clinica, has, dm, dac, cirurgia_recente, alergia, medicamentos_em_uso, pa, pulso, temperatura, glicemia, peso, altura, historico, medicacao, prescricao, retorno, hd, cid, tb_pacientes_fkpacientes_atendimento, identificacao_profissional, saturacao, reavaliacao) values " \
                             f"('{ficha['evento']}', '{ficha['nome']}', '{ficha['data']}', '{ficha['hora']}', '{ficha['alojamento']}', " \
                             f"'{ficha['clinica']}', {ficha['has']}, {ficha['dm']}, {ficha['dac']}, {ficha['cirurgia']}, '{ficha['alergia']}', '{ficha['medicamentos']}', '{ficha['pa']}', '{ficha['pulso']}', '{ficha['temp']}', '{ficha['glicemia']}', '{ficha['peso']}', '{ficha['altura']}', '{ficha['historico']}', '{ficha['medicacao']}', '{ficha['prescricao']}', '{ficha['retorno']}', '{ficha['hd']}', '{ficha['cid']}', " \
                             f"{ficha['fkpaciente']}, '{ficha['identificacao']}', '{ficha['saturacao']}', '{ficha['reavaliacao']}')"
        self.cursor.execute(insert_atendimento)
        self.db.commit()

    #MÉTODO QUE RECUPERA O CÓDIGO DO PACIENTE
    def recupera_codigo_paciente(self, nome):
        select_paciente = f"select idpacientes from tb_pacientes where nome = '{nome}'"
        self.cursor.execute(select_paciente)
        resultado = self.cursor.fetchall()
        return resultado

    #MÉTODO QUE RECUPERA OS ATENDIDOS E A SUA QUANTIDADE DE ATENDIMENTO E ESTÁ SENDO USADO NA CLASSE CONSULTAS.PY
    def recupera_atendidos_e_quantidade_nao(self):
        select_nomes = f"select distinct nome_atendido from tb_fichas_de_atendimentos where reavaliacao = 'NAO'"
        self.cursor.execute(select_nomes)
        result_nomes = self.cursor.fetchall()
        nomes = []
        for nome in result_nomes:
            nomes.append(nome[0])

        atendidos = []
        for atendido in nomes:
            select_atendidos = f"select nome, ministerio, cidade, estado, pais, count(nome_atendido) as quantidade from tb_pacientes inner join " \
                                       f"tb_fichas_de_atendimentos on tb_fichas_de_atendimentos.tb_pacientes_fkpacientes_atendimento = tb_pacientes.fkpacientes_atendimento " \
                                       f"where tb_fichas_de_atendimentos.nome_atendido = '{atendido}' and tb_fichas_de_atendimentos.reavaliacao = 'NAO'"
            self.cursor.execute(select_atendidos)
            result_atendidos = self.cursor.fetchall()
            atendidos.append(result_atendidos)

        return atendidos

    # MÉTODO QUE RECUPERA OS ATENDIDOS E A SUA QUANTIDADE DE ATENDIMENTO E ESTÁ SENDO USADO NA CLASSE REAVALIACAO.PY
    def recupera_atendidos_e_quantidade_sim(self):
        select_nomes = f"select idatendimentos, nome_atendido from tb_fichas_de_atendimentos where reavaliacao = 'SIM'"
        self.cursor.execute(select_nomes)
        result_nomes = self.cursor.fetchall()
        nomes = []
        for nome in result_nomes:
            nomes.append(nome)

        atendidos = []
        for atendido in nomes:
            select_atendidos = f"select idatendimentos, nome, ministerio, cidade, estado, pais, data, hora from tb_pacientes inner join " \
                               f"tb_fichas_de_atendimentos on tb_fichas_de_atendimentos.tb_pacientes_fkpacientes_atendimento = tb_pacientes.fkpacientes_atendimento " \
                               f"where tb_fichas_de_atendimentos.nome_atendido = '{atendido[1]}' and tb_fichas_de_atendimentos.idatendimentos = {atendido[0]} and tb_fichas_de_atendimentos.reavaliacao = 'SIM'"
            self.cursor.execute(select_atendidos)
            result_atendidos = self.cursor.fetchall()
            atendidos.append(result_atendidos)
        self.db.commit()

        return atendidos

    #MÉTODO QUE RECUPERA APENAS UM PACIENTE MEDIANTE VALOR RECEBIDO E QUE ESTÁ COM ALTA, PARA SER USADA NA CLASSE CONSULTA.PY
    def recupera_paciente_mediante_valor_recebido_nao(self, paciente):
        select_paciente_val = f"select nome, ministerio, cidade, estado, pais, count(nome_atendido) as quantidade from tb_pacientes inner join " \
                                       f"tb_fichas_de_atendimentos on tb_fichas_de_atendimentos.tb_pacientes_fkpacientes_atendimento = tb_pacientes.fkpacientes_atendimento " \
                                       f"where tb_fichas_de_atendimentos.nome_atendido = '{paciente}' and tb_fichas_de_atendimentos.reavaliacao = 'NAO'"
        self.cursor.execute(select_paciente_val)
        resultado_paciente = self.cursor.fetchall()
        return resultado_paciente

    # MÉTODO QUE RECUPERA APENAS UM PACIENTE MEDIANTE VALOR RECEBIDO PARA POSSÍVEL REAVALIAÇÃO, PARA SER USADA NA CLASSE REAVALIACAO.PY
    def recupera_paciente_mediante_valor_recebido_sim(self, paciente):
        select_paciente_val = f"select idatendimentos, nome, ministerio, cidade, estado, pais, data, hora from tb_pacientes inner join " \
                              f"tb_fichas_de_atendimentos on tb_fichas_de_atendimentos.tb_pacientes_fkpacientes_atendimento = tb_pacientes.fkpacientes_atendimento " \
                              f"where tb_fichas_de_atendimentos.nome_atendido = '{paciente}' and tb_fichas_de_atendimentos.reavaliacao = 'SIM'"
        self.cursor.execute(select_paciente_val)
        resultado_paciente = self.cursor.fetchall()
        return resultado_paciente

    #MÉTODO QUE RECUPERA TODOS OS ATENDIMENTOS DO PACIENTE, MÉTODO USADO NA CLASSE FICHA_INDIVIDUAL3.PY
    def recupera_todos_atendimentos_paciente(self, nome):
        select_atendimentos = f"select nome, ministerio, telefone, comum_congregacao, cidade, estado, pais, evento, data, hora, alojamento, clinica, has, dm, dac, cirurgia_recente, alergia, medicamentos_em_uso, pa, pulso, temperatura," \
                              f"glicemia, peso, altura, historico, medicacao, prescricao, retorno, hd, cid, identificacao_profissional, saturacao, identidade_atendido " \
                              f"from tb_fichas_de_atendimentos inner join tb_pacientes " \
                              f"on tb_fichas_de_atendimentos.tb_pacientes_fkpacientes_atendimento = tb_pacientes.fkpacientes_atendimento where tb_pacientes.nome = '{nome}' and tb_fichas_de_atendimentos.reavaliacao = 'NAO'"
        self.cursor.execute(select_atendimentos)
        retornos = self.cursor.fetchall()
        return retornos

    #MÉTODO QUE FARÁ CADASTRO DO PROFISSIONAL E SERÁ USADO NA CLASSE CADASTRO_PROFISSIONAL.PY
    def cadastrar_profissional(self, cadastro):
        insert_profissional = f"insert into tb_profissionais (nome_completo, profissao, rp) values ('{cadastro['nome']}','{cadastro['profissao']}','{cadastro['rp']}')"
        self.cursor.execute(insert_profissional)
        self.db.commit()

    #MÉTODO QUE PEGA OS DADOS DA FICHA DO PACIENTE DE ACORDO COM CÓDIGO DA FICHA, MÉTODO USADO NA CLASSE FICHA_ATENDIMENTO_DA_REAVALIACAO.PY
    def recupera_dados_ficha_atendimento_paciente(self, cod_paciente):
        select_ficha = f"select * from tb_fichas_de_atendimentos where idatendimentos = {cod_paciente}"
        self.cursor.execute(select_ficha)
        volta_dados = self.cursor.fetchall()
        return volta_dados


    #MÉTODO QUE RECUPERA O EVENTO, USADO NAS CLASSES: FICHA_ATENDIMENTO.PY, FICHA_ATENDIMENTO_DA_CONSULTA.PY
    def recupera_evento(self):
        select_evento = "select nome_evento from tb_eventos order by nome_evento"
        self.cursor.execute(select_evento)
        retorna_evento = self.cursor.fetchall()
        return retorna_evento

    #MÉTODO QUE IRÁ CADASTRAR EVENTO, ESTE SERÁ USADO NA CLASSE CADASTRAR_EVENTO.PY
    def cadastrar_evento(self, evento):
        insert_evento = f"insert into tb_eventos (nome_evento) values ('{evento}')"
        self.cursor.execute(insert_evento)
        self.db.commit()

    #MÉTODO QUE IRÁ ATUALIZAR OS EVENTOS E ESTÁ SENDO USADO NA CLASSE ATUALIZA_EVENTOS.PY
    def atualiza_eventos(self):
        select = "select * from tb_eventos order by nome_evento"
        self.cursor.execute(select)
        recebe = self.cursor.fetchall()
        return recebe

    #MÉTODO QUE ATUALIZA OS DADOS REAVALIADOS DO PACIENTE, ESTE MÉTODO ESTÁ SENDO USADO NA CLASSE FICHA_ATENDIMENTO_DA_REAVALIACAO NO BOTÃO SALVAR
    def atualiza_ficha_paciente(self, info):
        update_ficha = f"update tb_fichas_de_atendimentos set alojamento = '{info['alojamento']}', clinica = '{info['clinica']}', " \
                       f"has = {info['has']}, dm = {info['dm']}, dac = {info['dac']}, cirurgia_recente = {info['cirurgia']}, alergia = '{info['alergia']}', " \
                       f"medicamentos_em_uso = '{info['medicamentos']}', pa = '{info['pa']}', pulso = '{info['pulso']}', temperatura = '{info['temp']}', " \
                       f"glicemia = '{info['glicemia']}', peso = '{info['peso']}', altura = '{info['altura']}', historico = '{info['historico']}', " \
                       f"medicacao = '{info['prescricao']}', prescricao = '{info['anotacao']}', retorno = '{info['retorno']}', hd = '{info['hd']}', " \
                       f"cid = '{info['cid']}', identificacao_profissional = '{info['profissional']}', saturacao = '{info['saturacao']}', reavaliacao = '{info['reavaliacao']}' " \
                       f"where idatendimentos = {info['codAtendimento']}"
        self.cursor.execute(update_ficha)
        self.db.commit()

    #MÉTODO QUE BUSCA O NOME DO PACIENTE DE ACORDO O QUE FOI RECEBIDO, USADO NA CLASSE FICHA_ATENDIMENTO.PY
    def busca_paciente(self, nome):
        pega_paciente = f"select nome from tb_pacientes where nome like '{nome}%'"
        self.cursor.execute(pega_paciente)
        volta_nome = self.cursor.fetchall()
        return volta_nome

    #MÉTODO QUE PEGA AS IDENTIDADES, ESTE MÉTODO ESTÁ SENDO USADO NA CLASSE CADASTRO.PY
    def busca_identidade(self, id):
        pega_identidade = f"select identidade_atendido from tb_pacientes where identidade_atendido like '{id}%' order by identidade_atendido desc limit 1"
        self.cursor.execute(pega_identidade)
        volta_identidade = self.cursor.fetchall()
        return volta_identidade

    # MÉTODO QUE PEGA AS IDENTIDADES, ESTE MÉTODO ESTÁ SENDO USADO NA CLASSE CADASTRO.PY
    def busca_identidade_sem_parametro(self):
        pega_identidade = f"select identidade_atendido from tb_pacientes where identidade_atendido like 'M%' order by identidade_atendido desc limit 1"
        self.cursor.execute(pega_identidade)
        volta_identidade = self.cursor.fetchall()
        return volta_identidade