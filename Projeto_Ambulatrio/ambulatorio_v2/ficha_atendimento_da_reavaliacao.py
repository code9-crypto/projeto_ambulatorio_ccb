# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ficha_atendimento_da_reavaliacao.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
from banco import Acesso_banco


class Ui_Dialog9(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(716, 678)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/enfermagem.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, -2, 341, 31))
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 28, 361, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.edtEvento = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.edtEvento.setObjectName("edtEvento")
        self.horizontalLayout.addWidget(self.edtEvento)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(9, 58, 701, 31))
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
        self.groupBox.setGeometry(QtCore.QRect(10, 98, 701, 181))
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
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 681, 92))
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
        self.edtAltura = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.edtAltura.setObjectName("edtAltura")
        self.horizontalLayout_4.addWidget(self.edtAltura)
        self.label_29 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_4.addWidget(self.label_29)
        self.edtAltura_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.edtAltura_2.setObjectName("edtAltura_2")
        self.horizontalLayout_4.addWidget(self.edtAltura_2)
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(50, 278, 591, 31))
        self.label_19.setObjectName("label_19")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 308, 691, 71))
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
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 378, 691, 71))
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
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 448, 691, 71))
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
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 518, 691, 71))
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
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 588, 691, 31))
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
        self.btnSalvar = QtWidgets.QPushButton(Dialog)
        self.btnSalvar.setGeometry(QtCore.QRect(100, 645, 191, 31))
        self.btnSalvar.setObjectName("btnSalvar")
        self.cmbNomeAtendido = QtWidgets.QComboBox(Dialog)
        self.cmbNomeAtendido.setGeometry(QtCore.QRect(480, 28, 231, 20))
        self.cmbNomeAtendido.setObjectName("cmbNomeAtendido")
        self.label_28 = QtWidgets.QLabel(Dialog)
        self.label_28.setGeometry(QtCore.QRect(390, 28, 91, 21))
        self.label_28.setObjectName("label_28")
        self.label_26 = QtWidgets.QLabel(Dialog)
        self.label_26.setGeometry(QtCore.QRect(10, 616, 181, 29))
        self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_26.setWordWrap(False)
        self.label_26.setObjectName("label_26")
        self.cmbIdentificacao = QtWidgets.QComboBox(Dialog)
        self.cmbIdentificacao.setGeometry(QtCore.QRect(200, 621, 501, 20))
        self.cmbIdentificacao.setObjectName("cmbIdentificacao")
        self.btnAlta = QtWidgets.QPushButton(Dialog)
        self.btnAlta.setGeometry(QtCore.QRect(440, 645, 191, 31))
        self.btnAlta.setObjectName("btnAlta")

        # ÍCONE DE VISTO PARA O BOTÃO SALVAR
        self.btnIconeVisto = QtWidgets.QPushButton(Dialog)
        self.btnIconeVisto.setGeometry(QtCore.QRect(295, 642, 33, 33))
        self.btnIconeVisto.setAutoDefault(False)
        self.btnIconeVisto.setObjectName("btnIconeVisto")
        self.iconVisto = QtGui.QIcon()
        self.iconVisto.addPixmap(QtGui.QPixmap("img/visto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIconeVisto.setIcon(self.iconVisto)
        self.btnIconeVisto.setIconSize(QtCore.QSize(40, 40))
        self.btnIconeVisto.hide()

        # ÍCONE DE ERRO PARA O BOTÃO SALVAR
        self.btnIconeErrado = QtWidgets.QPushButton(Dialog)
        self.btnIconeErrado.setGeometry(QtCore.QRect(295, 642, 30, 30))
        self.btnIconeErrado.setAutoDefault(False)
        self.btnIconeErrado.setObjectName("btnIconeErrado")
        self.iconErrado = QtGui.QIcon()
        self.iconErrado.addPixmap(QtGui.QPixmap("img/errado4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIconeErrado.setIcon(self.iconErrado)
        self.btnIconeErrado.setIconSize(QtCore.QSize(55, 55))
        self.btnIconeErrado.hide()

        # ÍCONE DE VISTO PARA O BOTÃO CONCLUIR
        self.btnIconeVistoConcluir = QtWidgets.QPushButton(Dialog)
        self.btnIconeVistoConcluir.setGeometry(QtCore.QRect(635, 642, 33, 33))
        self.btnIconeVistoConcluir.setAutoDefault(False)
        self.btnIconeVistoConcluir.setObjectName("btnIconeVisto")
        self.iconVistoConcluir = QtGui.QIcon()
        self.iconVistoConcluir.addPixmap(QtGui.QPixmap("img/visto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIconeVistoConcluir.setIcon(self.iconVistoConcluir)
        self.btnIconeVistoConcluir.setIconSize(QtCore.QSize(40, 40))
        self.btnIconeVistoConcluir.hide()

        # ÍCONE DE ERRO PARA O BOTÃO CONCLUIR
        self.btnIconeErradoConcluir = QtWidgets.QPushButton(Dialog)
        self.btnIconeErradoConcluir.setGeometry(QtCore.QRect(605, 642, 30, 30))
        self.btnIconeErradoConcluir.setAutoDefault(False)
        self.btnIconeErradoConcluir.setObjectName("btnIconeErrado")
        self.iconErradoConcluir = QtGui.QIcon()
        self.iconErradoConcluir.addPixmap(QtGui.QPixmap("img/errado4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIconeErradoConcluir.setIcon(self.iconErradoConcluir)
        self.btnIconeErradoConcluir.setIconSize(QtCore.QSize(55, 55))
        self.btnIconeErradoConcluir.hide()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #CONETANDO AO BANCO
        self.banco = Acesso_banco.Banco_de_dados()
        self.banco.conectar()

        #Chamando método que formata e limita os campos
        self.formatando_e_limitando_campos()

        #Chamando método assim que abre tela
        self.pega_ficha()

        #Chamando método assim que abre tela
        self.recuperando_nome_profissional()

        #Chamando o método salvar através do botão salvar
        self.btnSalvar.clicked.connect(self.salvar)

        #Chamando o método concluir através do botão alta( o qual irá encerrar o atendimento )
        self.btnAlta.clicked.connect(self.concluir)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SISTEMA AMBULATORIO - FICHA PARA REAVALIAÇÃO"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">FICHA DE ATENDIMENTO</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "EVENTO:"))
        self.label_3.setText(_translate("Dialog", "DATA:"))
        self.edtData.setInputMask(_translate("Dialog", "00/00/0000"))
        self.label_4.setText(_translate("Dialog", "HORA:"))
        self.edtHora.setInputMask(_translate("Dialog", "00:00"))
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
        self.label_29.setText(_translate("Dialog", "SATUR.:"))
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
        self.btnSalvar.setText(_translate("Dialog", "SALVAR"))
        self.label_28.setText(_translate("Dialog", "ATENDENDO O(A):"))
        self.label_26.setText(_translate("Dialog", "IDENTIFICAÇÃO DO PROFISSIONAL:"))
        self.btnAlta.setText(_translate("Dialog", "ALTA / CONCLUIR"))

    #MÉTODO QUE IRÁ PEGAR OS DADOS DO PACIENTE ESPECÍFICO E PREENCHERÁ OS CAMPOS DE ACORDO
    def pega_ficha(self):
        try:
            dados = self.banco.recupera_dados_ficha_atendimento_paciente(os.environ['codigo_atendimento'])
            self.edtEvento.setReadOnly(True)
            self.edtEvento.setText(dados[0][1])
            self.cmbNomeAtendido.setDisabled(True)
            self.cmbNomeAtendido.addItem(dados[0][2])
            self.edtData.setReadOnly(True)
            self.edtData.setText(dados[0][3])
            self.edtHora.setReadOnly(True)
            self.edtHora.setText(dados[0][4])
            self.edtAlojamento.setText(dados[0][5])
            self.edtClinica.setText(dados[0][6])

            if dados[0][7] == 0:
                self.chkHAS.setCheckable(True)
            else:
                self.chkHAS.setChecked(True)

            if dados[0][8] == 0:
                self.chkDM.setCheckable(True)
            else:
                self.chkDM.setChecked(True)

            if dados[0][9] == 0:
                self.chkDAC.setCheckable(True)
            else:
                self.chkDAC.setChecked(True)

            if dados[0][10] == 0:
                self.chkCirurgia.setCheckable(True)
            else:
                self.chkCirurgia.setChecked(True)

            self.edtAlergia.setText(dados[0][11])
            self.txtMedicamentos.setText(dados[0][12])
            self.edtPA.setText(dados[0][13])
            self.edtPulso.setText(dados[0][14])
            self.edtTemp.setText(dados[0][15])
            self.edtGlicemia.setText(dados[0][16])
            self.edtPeso.setText(dados[0][17])
            self.edtAltura.setText(dados[0][18])
            self.txtHistorico.setText(dados[0][19])
            self.txtMedicacao.setText(dados[0][20])
            self.txtPrescricao.setText(dados[0][21])
            self.txtRetorno.setText(dados[0][22])
            self.edtHD.setText(dados[0][23])
            self.edtCID.setText(dados[0][24])
            self.edtAltura_2.setText(dados[0][28])
            self.profissional = dados[0][27]
        except:
            print()

    # EVENTO QUE RECUPERA NOME DO PROFISSIONAL E CRM
    def recuperando_nome_profissional(self):
        try:
            nome_profissional = self.banco.recupera_profissional()
            for identificacao in nome_profissional:
                self.cmbIdentificacao.addItem(identificacao[0])
        except:
            self.cmbIdentificacao.setDisabled(True)


    #MÉTODO QUE IRÁ SALVAR OS DADOS PARA UMA FUTURA AVALIAÇÃO
    def salvar(self):
        dados = {}
        dados['codAtendimento'] = os.environ['codigo_atendimento']
        dados['alojamento'] = self.edtAlojamento.text()
        dados['clinica']  = self.edtClinica.text()

        if self.chkHAS.isChecked():
            dados['has'] = 1
        else:
            dados['has'] = 0

        if self.chkDM.isChecked():
            dados['dm'] = 1
        else:
            dados['dm'] = 0

        if self.chkDAC.isChecked():
            dados['dac'] = 1
        else:
            dados['dac'] = 0

        if self.chkCirurgia.isChecked():
            dados['cirurgia'] = 1
        else:
            dados['cirurgia'] = 0

        dados['alergia'] = self.edtAlergia.text()
        dados['medicamentos'] = self.txtMedicamentos.document().toPlainText()
        dados['pa'] = self.edtPA.text()
        dados['pulso'] = self.edtPulso.text()
        dados['temp'] = self.edtTemp.text()
        dados['glicemia'] = self.edtGlicemia.text()
        dados['peso'] = self.edtPeso.text()
        dados['altura'] = self.edtAltura.text()
        dados['saturacao'] = self.edtAltura_2.text()
        dados['historico'] = self.txtHistorico.document().toPlainText()
        dados['prescricao'] = self.txtMedicacao.document().toPlainText()
        dados['anotacao'] = self.txtPrescricao.document().toPlainText()
        dados['retorno'] = self.txtRetorno.document().toPlainText()
        dados['hd'] = self.edtHD.text()
        dados['cid'] = self.edtCID.text()
        dados['profissional'] = self.profissional +", "+self.cmbIdentificacao.currentText()
        dados['reavaliacao'] = 'SIM'
        try:
            if self.btnIconeErrado.isActiveWindow():
                self.btnIconeErrado.hide()
                self.banco.atualiza_ficha_paciente(dados)
                self.limpa_campos()
                self.btnIconeVisto.show()
            else:
                self.btnIconeErrado.show()
        except:
            self.btnIconeErrado.show()


    #MÉTODO QUE IRÁ SALVAR OS DADOS PARA UMA FUTURA AVALIAÇÃO
    def concluir(self):
        dados = {}
        dados['codAtendimento'] = os.environ['codigo_atendimento']
        dados['alojamento'] = self.edtAlojamento.text()
        dados['clinica']  = self.edtClinica.text()

        if self.chkHAS.isChecked():
            dados['has'] = 1
        else:
            dados['has'] = 0

        if self.chkDM.isChecked():
            dados['dm'] = 1
        else:
            dados['dm'] = 0

        if self.chkDAC.isChecked():
            dados['dac'] = 1
        else:
            dados['dac'] = 0

        if self.chkCirurgia.isChecked():
            dados['cirurgia'] = 1
        else:
            dados['cirurgia'] = 0

        dados['alergia'] = self.edtAlergia.text()
        dados['medicamentos'] = self.txtMedicamentos.document().toPlainText()
        dados['pa'] = self.edtPA.text()
        dados['pulso'] = self.edtPulso.text()
        dados['temp'] = self.edtTemp.text()
        dados['glicemia'] = self.edtGlicemia.text()
        dados['peso'] = self.edtPeso.text()
        dados['altura'] = self.edtAltura.text()
        dados['saturacao'] = self.edtAltura_2.text()
        dados['historico'] = self.txtHistorico.document().toPlainText()
        dados['prescricao'] = self.txtMedicacao.document().toPlainText()
        dados['anotacao'] = self.txtPrescricao.document().toPlainText()
        dados['retorno'] = self.txtRetorno.document().toPlainText()
        dados['hd'] = self.edtHD.text()
        dados['cid'] = self.edtCID.text()
        dados['profissional'] = self.profissional +", "+self.cmbIdentificacao.currentText()
        dados['reavaliacao'] = 'NAO'
        try:
            if self.btnIconeErradoConcluir.isActiveWindow():
                self.btnIconeErradoConcluir.hide()
                self.banco.atualiza_ficha_paciente(dados)
                self.limpa_campos()
                self.btnIconeVistoConcluir.show()
            else:
                self.btnIconeErradoConcluir.show()
        except:
            self.btnIconeErradoConcluir.show()

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

    # LIMPANDO CAMPOS
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
        self.edtAltura_2.clear()
        self.txtHistorico.clear()
        self.txtMedicacao.clear()
        self.txtPrescricao.clear()
        self.txtRetorno.clear()
        self.edtHD.clear()
        self.edtCID.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog9()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())