# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inicio.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from cadastro import Ui_Dialog2
from ficha_atendimento import Ui_Dialog3
from consultas import Ui_Dialog4
from reavaliacao import Ui_Dialog7
from cadastro_profissional import Ui_Dialog8


#Essas classes é referente a tradução dos dias da semana e dos meses do ano
import semana
import mes

#Essa classe é para pegar o dia do mês e o ano
import datetime

#Essas variaveis é para o dia do mês e o ano
data = datetime.date.today()
dia = data.strftime("%d")
ano = data.strftime("%Y")

#Aqui estou traduzindo os dias da semana e os meses do ano para português
dia_semana = semana.dia_da_semana()
mes_ano = mes.mes_do_ano()


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(631, 347)
        iconTela = QtGui.QIcon()
        iconTela.addFile("img/enfermagem.png")
        Dialog.setWindowIcon(iconTela)
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_atende = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_atende.setGeometry(QtCore.QRect(60, 0, 51, 51))
        self.pushButton_atende.setText("")
        iconAtende = QtGui.QIcon()
        iconAtende.addPixmap(QtGui.QPixmap("img/atendimento.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_atende.setIcon(iconAtende)
        self.pushButton_atende.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_atende.setObjectName("pushButton_atende")
        self.pushButton_sair = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sair.setGeometry(QtCore.QRect(180, 0, 51, 51))
        self.pushButton_sair.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/saida.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_sair.setIcon(icon)
        self.pushButton_sair.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_sair.setObjectName("pushButton_sair")
        self.pushButton_cadastrar_profissional = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cadastrar_profissional.setGeometry(QtCore.QRect(120, 0, 50, 50))
        self.pushButton_cadastrar_profissional.setText("")
        iconProf = QtGui.QIcon()
        iconProf.addPixmap(QtGui.QPixmap("img/cadastrar_profissional2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_cadastrar_profissional.setIcon(iconProf)
        self.pushButton_cadastrar_profissional.setIconSize(QtCore.QSize(50,52))
        self.pushButton_cadastrar_profissional.setObjectName("pushButton_cadastrar_profissional")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.pushButton_add.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/user-add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_add.setIcon(icon1)
        self.pushButton_add.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_ficha = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ficha.setGeometry(QtCore.QRect(40, 120, 231, 141))
        self.pushButton_ficha.setObjectName("pushButton_ficha")
        self.pushButton_controle = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_controle.setGeometry(QtCore.QRect(360, 120, 231, 141))
        self.pushButton_controle.setObjectName("pushButton_controle")
        self.lblData = QtWidgets.QLabel(self.centralwidget)
        self.lblData.setGeometry(QtCore.QRect(150, 69, 340, 21))
        self.lblData.setTextFormat(QtCore.Qt.MarkdownText)
        self.lblData.setObjectName("lblData")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.pushButton_add, self.pushButton_sair)

        #Deixando a label com a data atual
        self.lblData.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:500;\">{dia_semana}, {dia} de {mes_ano} de {ano}</span></p></body></html>")

        #Fechando a tela atual
        self.pushButton_sair.clicked.connect(QApplication.instance().quit)

        #Botão para abrir a tela de cadastro
        self.pushButton_add.clicked.connect(self.abrir_cadastro)

        #Botão para abrir a tela de atendimento
        self.pushButton_atende.clicked.connect(self.abrir_atendimento)

        #Botão para abrir as fichas de atendimentos
        self.pushButton_ficha.clicked.connect(self.abrir_reavaliacao)

        #Botão para abrir as fichas de atendimentos
        self.pushButton_controle.clicked.connect(self.abrir_consultas)

        #Botão para abrir a tela de cadastro de profissional
        self.pushButton_cadastrar_profissional.clicked.connect(self.abrir_cadastro_profissional)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SISTEMA AMBULATÓRIO - INÍCIO"))
        self.pushButton_sair.autoFillBackground()
        self.pushButton_sair.setAutoDefault(False)
        self.pushButton_sair.setToolTip(_translate("Dialog", "Sair do Programa"))
        self.pushButton_add.setToolTip(_translate("Dialog", "Cadastrar Paciente"))
        self.pushButton_ficha.setText(_translate("Dialog", "   FICHAS DE \n"
"ATENDIMENTOS \n (REAVALIAÇÃO)"))
        self.pushButton_ficha.setToolTip(_translate("Dialog", "Verificar Fichas"))
        self.pushButton_controle.setText(_translate("Dialog", "CONTROLES DE\n"
"ATENDIMENTOS \n (CONSULTAS)"))
        self.pushButton_controle.setToolTip(_translate("Dialog", "Verificar Controles"))
        self.pushButton_atende.setToolTip(_translate("Dialog", "Atendimento ao Paciente"))
        self.pushButton_cadastrar_profissional.setToolTip(_translate("Dialog", "Cadastrar Profissional"))


    #Função para abrir a tela de cadastro
    def abrir_cadastro(self):
        telaCadatro = QtWidgets.QDialog()
        ui = Ui_Dialog2()
        ui.setupUi(telaCadatro)
        self.pushButton_add.setDisabled(True)
        telaCadatro.show()
        retornoCad = telaCadatro.exec_()
        if retornoCad == 0:
            self.pushButton_add.setDisabled(False)

    #Função para abrir a tela de atendimento
    def abrir_atendimento(self):
        telaAtendimento = QtWidgets.QDialog()
        ui = Ui_Dialog3()
        ui.setupUi(telaAtendimento)
        self.pushButton_atende.setDisabled(True)
        telaAtendimento.show()
        retornoAtend = telaAtendimento.exec_()
        if retornoAtend == 0:
            self.pushButton_atende.setDisabled(False)

    def abrir_consultas(self):
        telaConsultas = QtWidgets.QDialog()
        ui = Ui_Dialog4()
        ui.setupUi(telaConsultas)
        self.pushButton_controle.setDisabled(True)
        telaConsultas.show()
        retornoCon = telaConsultas.exec_()
        if retornoCon == 0:
            self.pushButton_controle.setDisabled(False)

    def abrir_reavaliacao(self):
        telaConsultas = QtWidgets.QDialog()
        ui = Ui_Dialog7()
        ui.setupUi(telaConsultas)
        self.pushButton_ficha.setDisabled(True)
        telaConsultas.show()
        retornoCon = telaConsultas.exec_()
        if retornoCon == 0:
            self.pushButton_ficha.setDisabled(False)

    def abrir_cadastro_profissional(self):
        telaCadastroProfissional = QtWidgets.QDialog()
        ui = Ui_Dialog8()
        ui.setupUi(telaCadastroProfissional)
        self.pushButton_cadastrar_profissional.setDisabled(True)
        telaCadastroProfissional.show()
        retornoCon = telaCadastroProfissional.exec_()
        if retornoCon == 0:
            self.pushButton_cadastrar_profissional.setDisabled(False)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
