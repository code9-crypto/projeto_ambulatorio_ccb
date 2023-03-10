# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ficha_atendimento.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from banco import Acesso_banco
from datetime import datetime
import datetime
from cadastra_evento import Ui_Dialog10
import Atualiza_eventos



class Ui_Dialog3(object):
    def setupUi(self, Dialog):
        self.data = datetime.datetime.today()
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(724, 685)
        iconTela = QtGui.QIcon()
        iconTela.addFile("img/enfermagem.png")
        Dialog.setWindowIcon(iconTela)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 3, 341, 31))
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 201, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 38, 181, 29))
        self.label_2.setObjectName("label_2")
        self.cmbEvento = QtWidgets.QComboBox(Dialog)
        self.cmbEvento.setGeometry(QtCore.QRect(57, 43, 280, 20))
        self.cmbEvento.setObjectName("cmbEvento")

        #BOTÃO QUE CADASTRA NOVO EVENTO
        self.btnAddEvento = QtWidgets.QPushButton(Dialog)
        iconAdd = QtGui.QIcon()
        iconAdd.addPixmap(QtGui.QPixmap("img/add_evento.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAddEvento.setIcon(iconAdd)
        self.btnAddEvento.setIconSize(QtCore.QSize(22, 22))
        self.btnAddEvento.setGeometry(QtCore.QRect(339, 42, 22, 22))
        self.btnAddEvento.setObjectName("btnAddEvento")

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(9, 70, 701, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.edtData = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.edtData.setPlaceholderText("")
        self.edtData.setObjectName("edtData")
        self.horizontalLayout_2.addWidget(self.edtData)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.edtHora = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.edtHora.setObjectName("edtHora")
        self.horizontalLayout_2.addWidget(self.edtHora)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.edtAlojamento = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.edtAlojamento.setObjectName("edtAlojamento")
        self.horizontalLayout_2.addWidget(self.edtAlojamento)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.edtClinica = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.edtClinica.setObjectName("edtClinica")
        self.horizontalLayout_2.addWidget(self.edtClinica)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 110, 701, 181))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 681, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.chkHAS = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.chkHAS.setText("")
        self.chkHAS.setObjectName("chkHAS")
        self.horizontalLayout_3.addWidget(self.chkHAS)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.chkDM = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.chkDM.setText("")
        self.chkDM.setObjectName("chkDM")
        self.horizontalLayout_3.addWidget(self.chkDM)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.chkDAC = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.chkDAC.setText("")
        self.chkDAC.setObjectName("chkDAC")
        self.horizontalLayout_3.addWidget(self.chkDAC)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.chkCirurgia = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.chkCirurgia.setText("")
        self.chkCirurgia.setObjectName("chkCirurgia")
        self.horizontalLayout_3.addWidget(self.chkCirurgia)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.edtAlergia = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.edtAlergia.setObjectName("edtAlergia")
        self.horizontalLayout_3.addWidget(self.edtAlergia)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 681, 72))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.txtMedicamentos = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.txtMedicamentos.setObjectName("txtMedicamentos")
        self.verticalLayout.addWidget(self.txtMedicamentos)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 130, 681, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.label_13)
        self.edtPA = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.edtPA.setInputMask("")
        self.edtPA.setObjectName("edtPA")
        self.horizontalLayout_4.addWidget(self.edtPA)
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        self.edtPulso = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.edtPulso.setObjectName("edtPulso")
        self.horizontalLayout_4.addWidget(self.edtPulso)
        self.label_15 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.edtTemp = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.edtTemp.setObjectName("edtTemp")
        self.horizontalLayout_4.addWidget(self.edtTemp)
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_4.addWidget(self.label_16)
        self.edtGlicemia = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.edtGlicemia.setObjectName("edtGlicemia")
        self.horizontalLayout_4.addWidget(self.edtGlicemia)
        self.label_17 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_4.addWidget(self.label_17)
        self.edtPeso = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.edtPeso.setObjectName("edtPeso")
        self.horizontalLayout_4.addWidget(self.edtPeso)
        self.label_18 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_4.addWidget(self.label_18)
        self.edtSaturacao = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.edtSaturacao.setObjectName("edtSaturacao")
        self.horizontalLayout_4.addWidget(self.edtSaturacao)
        self.lblSaturacao = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.lblSaturacao.setObjectName("lblSaturacao")
        self.horizontalLayout_4.addWidget(self.lblSaturacao)
        self.edtAltura = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.edtAltura.setObjectName("edtAltura")
        self.horizontalLayout_4.addWidget(self.edtAltura)
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(50, 290, 591, 31))
        self.label_19.setObjectName("label_19")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 320, 691, 71))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_2.addWidget(self.label_20)
        self.txtHistorico = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.txtHistorico.setObjectName("txtHistorico")
        self.verticalLayout_2.addWidget(self.txtHistorico)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 390, 691, 71))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_3.addWidget(self.label_21)
        self.txtMedicacao = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.txtMedicacao.setObjectName("txtMedicacao")
        self.verticalLayout_3.addWidget(self.txtMedicacao)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 460, 691, 71))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_4.addWidget(self.label_22)
        self.txtPrescricao = QtWidgets.QTextEdit(self.verticalLayoutWidget_4)
        self.txtPrescricao.setObjectName("txtPrescricao")
        self.verticalLayout_4.addWidget(self.txtPrescricao)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 530, 691, 71))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_5.addWidget(self.label_23)
        self.txtRetorno = QtWidgets.QTextEdit(self.verticalLayoutWidget_5)
        self.txtRetorno.setObjectName("txtRetorno")
        self.verticalLayout_5.addWidget(self.txtRetorno)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(9, 600, 691, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_24 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_5.addWidget(self.label_24)
        self.edtHD = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.edtHD.setObjectName("edtHD")
        self.horizontalLayout_5.addWidget(self.edtHD)
        self.label_25 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_5.addWidget(self.label_25)
        self.edtCID = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.edtCID.setObjectName("edtCID")
        self.horizontalLayout_5.addWidget(self.edtCID)
        self.label_26 = QtWidgets.QLabel(Dialog)
        self.label_26.setObjectName("label_26")
        self.label_26.setGeometry(QtCore.QRect(10, 630, 501, 20))
        self.label_26.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.cmbIdentificacao = QtWidgets.QComboBox(Dialog)
        self.cmbIdentificacao.setGeometry(QtCore.QRect(200, 630, 501, 20))
        self.cmbIdentificacao.setObjectName("cmbIdentificacao")
        self.btnSalvar = QtWidgets.QPushButton(Dialog)
        self.btnSalvar.setGeometry(QtCore.QRect(100, 652, 191, 31))
        self.btnSalvar.setObjectName("btnSalvar")
        self.btnConcluir = QtWidgets.QPushButton(Dialog)
        self.btnConcluir.setGeometry(QtCore.QRect(410, 652, 191, 31))
        self.btnConcluir.setObjectName("btnConcluir")
        self.edtPesquisaNome = QtWidgets.QLineEdit(Dialog)
        self.edtPesquisaNome.setGeometry(QtCore.QRect(507, 19, 180, 20))
        self.edtPesquisaNome.setObjectName("edtPesquisaNome")
        self.edtPesquisaNome.hide()

        #LABEL DE AVISO DE ERRO
        self.lblAviso = QtWidgets.QLabel(Dialog)
        self.lblAviso.setGeometry(QtCore.QRect(550, 2, 180, 20))
        self.lblAviso.setObjectName("lblAviso")
        self.lblAviso.hide()

        #BOTÃO QUE PESQUISA O NOME DIGITADO
        self.btnPesquisaNome = QtWidgets.QPushButton(Dialog)
        iconPesquisaNome = QtGui.QIcon()
        iconPesquisaNome.addPixmap(QtGui.QPixmap("img/pesquisa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisaNome.setIcon(iconPesquisaNome)
        self.btnPesquisaNome.setIconSize(QtCore.QSize(19, 19))
        self.btnPesquisaNome.setGeometry(QtCore.QRect(688, 18, 20, 20))
        self.btnPesquisaNome.setObjectName("btnPesquisaNome")
        self.btnPesquisaNome.hide()
        self.cmbNomeAtendido = QtWidgets.QComboBox(Dialog)
        self.cmbNomeAtendido.setGeometry(QtCore.QRect(480, 40, 207, 20))
        self.cmbNomeAtendido.setObjectName("cmbNomeAtendido")

        #BOTÃO QUE MOSTRA O CAMPO PARA PESQUISAR ALGUM NOME
        self.btnFechado = QtWidgets.QPushButton(Dialog)
        iconFechado = QtGui.QIcon()
        iconFechado.addPixmap(QtGui.QPixmap("img/cadeadoVermelho.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnFechado.setIcon(iconFechado)
        self.btnFechado.setIconSize(QtCore.QSize(22, 22))
        self.btnFechado.setGeometry(QtCore.QRect(688, 39, 22, 22))
        self.btnFechado.setObjectName("btnFechado")
        self.btnFechado.show()

        #BOTÃO QUE FECHA O CAMPO QUE FOI ABERTO
        self.btnAberto = QtWidgets.QPushButton(Dialog)
        iconAberto = QtGui.QIcon()
        iconAberto.addPixmap(QtGui.QPixmap("img/cadeadoVerde.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAberto.setIcon(iconAberto)
        self.btnAberto.setIconSize(QtCore.QSize(22, 22))
        self.btnAberto.setGeometry(QtCore.QRect(688, 39, 22, 22))
        self.btnAberto.setObjectName("btnFechado")
        self.btnAberto.hide()

        self.label_28 = QtWidgets.QLabel(Dialog)
        self.label_28.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.label_28.setObjectName("label_28")

        #ÍCONE DE VISTO PARA O BOTÃO SALVAR
        self.btnIconeVisto = QtWidgets.QPushButton(Dialog)
        self.btnIconeVisto.setGeometry(QtCore.QRect(295, 652, 33, 33))
        self.btnIconeVisto.setAutoDefault(False)
        self.btnIconeVisto.setObjectName("btnIconeVisto")
        self.iconVisto = QtGui.QIcon()
        self.iconVisto.addPixmap(QtGui.QPixmap("img/visto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIconeVisto.setIcon(self.iconVisto)
        self.btnIconeVisto.setIconSize(QtCore.QSize(40, 40))
        self.btnIconeVisto.hide()

        #ÍCONE DE ERRO PARA O BOTÃO SALVAR
        self.btnIconeErrado = QtWidgets.QPushButton(Dialog)
        self.btnIconeErrado.setGeometry(QtCore.QRect(295, 652, 30, 30))
        self.btnIconeErrado.setAutoDefault(False)
        self.btnIconeErrado.setObjectName("btnIconeErrado")
        self.iconErrado = QtGui.QIcon()
        self.iconErrado.addPixmap(QtGui.QPixmap("img/errado4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIconeErrado.setIcon(self.iconErrado)
        self.btnIconeErrado.setIconSize(QtCore.QSize(55, 55))
        self.btnIconeErrado.hide()

        #ÍCONE DE VISTO PARA O BOTÃO CONCLUIR
        self.btnIconeVistoConcluir = QtWidgets.QPushButton(Dialog)
        self.btnIconeVistoConcluir.setGeometry(QtCore.QRect(605, 652, 33, 33))
        self.btnIconeVistoConcluir.setAutoDefault(False)
        self.btnIconeVistoConcluir.setObjectName("btnIconeVistoConcluir")
        self.iconVistoConcluir = QtGui.QIcon()
        self.iconVistoConcluir.addPixmap(QtGui.QPixmap("img/visto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIconeVistoConcluir.setIcon(self.iconVistoConcluir)
        self.btnIconeVistoConcluir.setIconSize(QtCore.QSize(40, 40))
        self.btnIconeVistoConcluir.hide()

        #ÍCONE DE ERRO PARA O BOTÃO CONCLUIR
        self.btnIconeErradoConcluir = QtWidgets.QPushButton(Dialog)
        self.btnIconeErradoConcluir.setGeometry(QtCore.QRect(605, 652, 30, 30))
        self.btnIconeErradoConcluir.setAutoDefault(False)
        self.btnIconeErradoConcluir.setObjectName("btnIconeErradoConcluir")
        self.iconErradoConcluir = QtGui.QIcon()
        self.iconErradoConcluir.addPixmap(QtGui.QPixmap("img/errado4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIconeErradoConcluir.setIcon(self.iconErradoConcluir)
        self.btnIconeErradoConcluir.setIconSize(QtCore.QSize(55, 55))
        self.btnIconeErradoConcluir.hide()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #Acessando o banco de dados
        self.banco = Acesso_banco.Banco_de_dados()
        self.banco.conectar()

        #Chamando o método que limita e formata os campos
        self.formatando_e_limitando_campos()

        #Chamando o método que recupera o nome do profissional
        self.recuperando_nome_profissional()

        # Chamando o método que recupera nome dos pacientes
        self.recuperar_paciente()

        #Chamando o método de cadastrar a ficha pelo botão SALVAR
        self.btnSalvar.clicked.connect(self.cadastrando_ficha_reavaliacao)

        #Chamando o método que dá alta na ficha
        self.btnConcluir.clicked.connect(self.cadastrando_ficha_concluir_alta)

        #Chamando o método que recupera data e horario
        self.recuperando_data_e_hora()

        #Chamando o método que recupera o código do paciente através do evento de mudança de nome da combobox e atribui na variavel da chave estrangeira
        self.cmbNomeAtendido.currentTextChanged.connect(self.recupera_codigo_paciente)

        #Chamando o método para iniciar junto com o programa e atribui o valor na variavel da chave estrangeira
        self.recupera_codigo_paciente()

        #Chamando método que recupera os eventos
        self.recupera_evento()

        #Chamando método para abrir tela de cadastrar evento
        self.btnAddEvento.clicked.connect(self.abrir_cadastro_evento)

        #Chamando método que abre o campo de pesquisa através do botão do cadeado vermelho
        self.btnFechado.clicked.connect(self.abre_campo_de_pesquisa)

        #Chamando método que fecha o campo de pesquisa através do botão do cadeado verde
        self.btnAberto.clicked.connect(self.fecha_campo_de_pesquisa)

        #Chamando o método que pesquisa nome pelo próprio botão
        self.btnPesquisaNome.clicked.connect(self.busca_paciente)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SISTEMA AMBULATÓRIO - ATENDIMENTO"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">FICHA DE ATENDIMENTO</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "EVENTO:"))
        self.label_3.setText(_translate("Dialog", "DATA:"))
        self.label_4.setText(_translate("Dialog", "HORA:"))
        self.label_5.setText(_translate("Dialog", "ALOJAMENTO:"))
        self.label_6.setText(_translate("Dialog", "CLÍNICA:"))
        self.groupBox.setTitle(_translate("Dialog", "ANTECEDENTES PESSOAIS"))
        self.label_7.setText(_translate("Dialog", "HAS"))
        self.label_8.setText(_translate("Dialog", "DM"))
        self.label_9.setText(_translate("Dialog", "DAC"))
        self.label_10.setText(_translate("Dialog", "CIRURGIA RECENTE"))
        self.label_11.setText(_translate("Dialog", "ALERGIA A:"))
        self.label_12.setText(_translate("Dialog", "MEDICAMENTOS EM USO:"))
        self.label_13.setText(_translate("Dialog", "PA:"))
        self.label_14.setText(_translate("Dialog", "PULSO:"))
        self.label_15.setText(_translate("Dialog", "TEMP.:"))
        self.label_16.setText(_translate("Dialog", "GLICEMIA:"))
        self.label_17.setText(_translate("Dialog", "PESO:"))
        self.label_18.setText(_translate("Dialog", "ALTURA:"))
        self.lblSaturacao.setText(_translate("Dialog", "SATUR.:"))
        self.label_19.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">ATENDIMENTO / CONSULTA / PROCEDIMENTO / ENCAMINHAMENTO APÓS O ATENDIMENTO</span></p></body></html>"))
        self.label_20.setText(_translate("Dialog", "<b>HISTÓRICO:</b>"))
        self.label_21.setText(_translate("Dialog", "<b>PRESCRIÇÃO MEDICA:</b>"))
        self.label_22.setText(_translate("Dialog", "<b>ANOTAÇÃO DE ENFERMAGEM:</b>"))
        self.txtPrescricao.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_23.setText(_translate("Dialog", "<b>RETORNO / ORIENTAÇÕES GERAIS:</b>"))
        self.label_24.setText(_translate("Dialog", "HD:"))
        self.label_25.setText(_translate("Dialog", "CID:"))
        self.label_26.setText(_translate("Dialog", "IDENTIFICAÇÃO DO PROFISSIONAL:"))
        self.btnSalvar.setText(_translate("Dialog", "SALVAR"))
        self.btnConcluir.setText(_translate("Dialog", "ALTA / CONCLUIR"))
        self.btnAddEvento.setToolTip("Cadastrar evento")
        self.label_28.setText(_translate("Dialog", "ATENDENDO O(A):"))
        self.lblAviso.setText(_translate("Dialog", "aviso de teste"))


    #EVENTO QUE FORMATA A DATA E HORARIO E ATRIBUI AOS SEUS CAMPOS
    def recuperando_data_e_hora(self):
        data = self.data.strftime("%d/%m/%Y")
        horario = self.data.strftime("%H:%M")
        self.edtData.setText(data)
        self.edtHora.setText(horario)


    #EVENTO QUE RECUPERA O NOME DO PACIENTE E ATRIBUI NA COMBOBOX
    def recuperar_paciente(self):
        try:
            dados = self.banco.recuperar_paciente()
            for dado in dados:
                self.cmbNomeAtendido.addItem(dado[0])
        except:
            self.cmbNomeAtendido.setDisabled(True)

    #EVENTO QUE RECUPERA O CÓDIGO DO PACIENTE
    def recupera_codigo_paciente(self):
        try:
            nome_paciente = self.cmbNomeAtendido.currentText()
            resp = self.banco.recupera_codigo_paciente(nome_paciente)
            self.codigo_paciente = resp[0][0]
        except:
            self.cmbNomeAtendido.setDisabled(True)



    #EVENTO QUE LIMITA E FORMATA OS CAMPOS
    def formatando_e_limitando_campos(self):
        self.edtData.setMaxLength(10)
        self.edtData.setInputMask("00/00/0000")
        self.edtHora.setMaxLength(5)
        self.edtHora.setInputMask("00:00")
        self.edtAlojamento.setMaxLength(20)
        self.edtClinica.setMaxLength(20)
        self.edtAlergia.setMaxLength(15)
        self.edtPA.setMaxLength(7)
        self.edtPulso.setMaxLength(7)
        self.edtTemp.setMaxLength(5)
        self.edtGlicemia.setMaxLength(5)
        self.edtPeso.setMaxLength(5)
        self.edtAltura.setMaxLength(6)
        self.edtHD.setMaxLength(45)
        self.edtCID.setMaxLength(45)

    #EVENTO QUE RECUPERA NOME DO PROFISSIONAL E CRM
    def recuperando_nome_profissional(self):
        try:
            nome_profissional = self.banco.recupera_profissional()
            for identificacao in nome_profissional:
                self.cmbIdentificacao.addItem(identificacao[0])
        except:
            self.cmbIdentificacao.setDisabled(True)

    #EVENTO QUE RECUPERA EVENTO
    def recupera_evento(self):
        try:
            self.cmbEvento.clear()
            self.cmbEvento.update()
            for evento in self.banco.recupera_evento():
                self.cmbEvento.addItem(evento[0])
        except:
            self.cmbEvento.setDisabled(True)


    #EVENTO QUE CADASTRA A FICHA DE ATENDIMENTO PARA POSSÍVEL REAVALIAÇÃO
    def cadastrando_ficha_reavaliacao(self):
        ficha = {}
        ficha['evento'] = self.cmbEvento.currentText()
        ficha['nome'] = self.cmbNomeAtendido.currentText()
        ficha['data'] = self.edtData.text()
        ficha['hora'] = self.edtHora.text()
        ficha['alojamento'] = self.edtAlojamento.text()
        ficha['clinica'] = self.edtClinica.text()

        if self.chkHAS.isChecked():
            ficha['has'] = int(1)
        else:
            ficha['has'] = int(0)

        if self.chkDM.isChecked():
            ficha['dm'] = int(1)
        else:
            ficha['dm'] = int(0)

        if self.chkDAC.isChecked():
            ficha['dac'] = int(1)
        else:
            ficha['dac'] = int(0)

        if self.chkCirurgia.isChecked():
            ficha['cirurgia'] = int(1)
        else:
            ficha['cirurgia'] = int(0)

        ficha['alergia'] = self.edtAlergia.text()
        ficha['medicamentos'] = self.txtMedicamentos.document().toPlainText()
        ficha['pa'] = self.edtPA.text()
        ficha['pulso'] = self.edtPulso.text()
        ficha['temp'] = self.edtTemp.text()
        ficha['glicemia'] = self.edtGlicemia.text()
        ficha['peso'] = self.edtPeso.text()
        ficha['altura'] = self.edtAltura.text()
        ficha['historico'] = self.txtHistorico.document().toPlainText()
        ficha['medicacao'] = self.txtMedicacao.document().toPlainText()
        ficha['prescricao'] = self.txtPrescricao.document().toPlainText()
        ficha['retorno'] = self.txtRetorno.document().toPlainText()
        ficha['hd'] = self.edtHD.text()
        ficha['cid'] = self.edtCID.text()
        ficha['fkpaciente'] = self.codigo_paciente
        ficha['identificacao'] = self.cmbIdentificacao.currentText()
        ficha['saturacao'] = self.edtSaturacao.text()
        ficha['reavaliacao'] = 'SIM'
        try:
            if ficha['evento'] != "":
                if self.btnIconeErrado.isActiveWindow():
                    self.btnIconeErrado.hide()
                    self.banco.cadastrar_atendimento(ficha)
                    self.limpa_campos()
                    self.btnIconeVisto.show()
                else:
                    self.btnIconeVisto.show()
            else:
                self.btnIconeErrado.show()
        except:
            self.btnIconeErrado.show()

    #EVENTO QUE DA ALTA NA FICHA DE ATENDIMENTO
    def cadastrando_ficha_concluir_alta(self):
        ficha = {}
        ficha['evento'] = self.cmbEvento.currentText()
        ficha['nome'] = self.cmbNomeAtendido.currentText()
        ficha['data'] = self.edtData.text()
        ficha['hora'] = self.edtHora.text()
        ficha['alojamento'] = self.edtAlojamento.text()
        ficha['clinica'] = self.edtClinica.text()

        if self.chkHAS.isChecked():
            ficha['has'] = int(1)
        else:
            ficha['has'] = int(0)

        if self.chkDM.isChecked():
            ficha['dm'] = int(1)
        else:
            ficha['dm'] = int(0)

        if self.chkDAC.isChecked():
            ficha['dac'] = int(1)
        else:
            ficha['dac'] = int(0)

        if self.chkCirurgia.isChecked():
            ficha['cirurgia'] = int(1)
        else:
            ficha['cirurgia'] = int(0)

        ficha['alergia'] = self.edtAlergia.text()
        ficha['medicamentos'] = self.txtMedicamentos.document().toPlainText()
        ficha['pa'] = self.edtPA.text()
        ficha['pulso'] = self.edtPulso.text()
        ficha['temp'] = self.edtTemp.text()
        ficha['glicemia'] = self.edtGlicemia.text()
        ficha['peso'] = self.edtPeso.text()
        ficha['altura'] = self.edtAltura.text()
        ficha['historico'] = self.txtHistorico.document().toPlainText()
        ficha['medicacao'] = self.txtMedicacao.document().toPlainText()
        ficha['prescricao'] = self.txtPrescricao.document().toPlainText()
        ficha['retorno'] = self.txtRetorno.document().toPlainText()
        ficha['hd'] = self.edtHD.text()
        ficha['cid'] = self.edtCID.text()
        ficha['fkpaciente'] = self.codigo_paciente
        ficha['identificacao'] = self.cmbIdentificacao.currentText()
        ficha['saturacao'] = self.edtSaturacao.text()
        ficha['reavaliacao'] = 'NAO'
        try:
            if ficha['evento'] != "":
                if self.btnIconeErradoConcluir.isActiveWindow():
                    self.btnIconeErradoConcluir.hide()
                    self.banco.cadastrar_atendimento(ficha)
                    self.limpa_campos()
                    self.btnIconeVistoConcluir.show()
                else:
                    self.btnIconeVistoConcluir.show()
            else:
                self.btnIconeErradoConcluir.show()
        except:
            self.btnIconeErradoConcluir.show()

    #LIMPANDO CAMPOS
    def limpa_campos(self):
        self.edtAlojamento.clear()
        self.edtClinica.clear()
        self.chkHAS.setChecked(False)
        self.chkDM.setChecked(False)
        self.chkDAC.setChecked(False)
        self.chkCirurgia.setChecked(False)
        self.edtAlergia.clear()
        self.txtMedicamentos.clear()
        self.edtPA.clear()
        self.edtPulso.clear()
        self.edtTemp.clear()
        self.edtGlicemia.clear()
        self.edtPeso.clear()
        self.edtAltura.clear()
        self.edtSaturacao.clear()
        self.txtHistorico.clear()
        self.txtMedicacao.clear()
        self.txtPrescricao.clear()
        self.txtRetorno.clear()
        self.edtHD.clear()
        self.edtCID.clear()

    #EVENTO QUE ATUALIZA OS EVENTOS
    def load(self):
        self.cmbEvento.clear()
        try:
            addEvento = Atualiza_eventos.carrega_eventos()
            for evento in addEvento:
                self.cmbEvento.addItem(evento[0])
        except:
            self.cmbEvento.setDisabled(True)


    #ABRIR A TELA DE CADASTRAR EVENTO
    def abrir_cadastro_evento(self):
        telaEvento = QtWidgets.QDialog()
        ui = Ui_Dialog10()
        ui.setupUi(telaEvento)
        self.btnAddEvento.setDisabled(True)
        telaEvento.show()
        retornoEvento = telaEvento.exec_()
        if retornoEvento == 0:
            self.btnAddEvento.setDisabled(False)
            self.load()

    #EVENTO QUE ABRE O CAMPO
    def abre_campo_de_pesquisa(self):
        self.btnFechado.hide()
        self.btnAberto.show()
        self.edtPesquisaNome.show()
        self.btnPesquisaNome.show()

    #EVENTO QUE FECHA O CAMPO
    def fecha_campo_de_pesquisa(self):
        self.btnAberto.hide()
        self.btnFechado.show()
        self.edtPesquisaNome.hide()
        self.edtPesquisaNome.clear()
        self.btnPesquisaNome.hide()
        self.lblAviso.hide()

    #EVENTO QUE BUSCA O NOME DO PACIENTE DE ACORDO COM O QUE FOI DIGITADO NO CAMPO
    def busca_paciente(self):
        nome = self.edtPesquisaNome.text()
        try:
            pega_nome = self.banco.busca_paciente(nome)
            self.lblAviso.hide()
            self.cmbNomeAtendido.setCurrentText(pega_nome[0][0])
        except:
            self.lblAviso.setText("<span style=\"color:red\">Este nome não existe</span>")
            self.lblAviso.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog3()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
