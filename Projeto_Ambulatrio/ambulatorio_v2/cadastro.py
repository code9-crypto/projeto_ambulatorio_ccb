# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from banco import Acesso_banco
import os


class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(747, 246)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/enfermagem.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 731, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.edtNome = QtWidgets.QLineEdit(Dialog)
        self.edtNome.setGeometry(QtCore.QRect(90, 20, 270, 20))
        self.edtNome.setObjectName("edtNome")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.edtMC = QtWidgets.QLineEdit(Dialog)
        self.edtMC.setGeometry(QtCore.QRect(463, 20, 220, 20))
        self.edtMC.setObjectName("edtMC")
        self.cmbIdentidade = QtWidgets.QComboBox(Dialog)
        self.cmbIdentidade.setGeometry(QtCore.QRect(686, 20, 35, 20))
        self.cmbIdentidade.addItem("M")
        self.cmbIdentidade.addItem("C")
        self.cmbIdentidade.addItem("I")
        self.cmbIdentidade.setObjectName("cmbIdentidade")
        self.edtIdentidade = QtWidgets.QLineEdit(Dialog)
        self.edtIdentidade.setGeometry(QtCore.QRect(725, 20, 15, 20))
        self.edtIdentidade.setReadOnly(True)
        self.edtIdentidade.setObjectName("edtIdentidade")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 731, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.edtCidade = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.edtCidade.setObjectName("edtCidade")
        self.horizontalLayout_2.addWidget(self.edtCidade)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.edtEstado = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.edtEstado.setObjectName("edtEstado")
        self.horizontalLayout_2.addWidget(self.edtEstado)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.edtPais = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.edtPais.setObjectName("edtPais")
        self.horizontalLayout_2.addWidget(self.edtPais)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(9, 89, 731, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.edtIdade = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.edtIdade.setMaxLength(2)
        self.edtIdade.setObjectName("edtIdade")
        self.horizontalLayout_3.addWidget(self.edtIdade)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.comboBox.setMaxVisibleItems(2)
        self.comboBox.addItem("M")
        self.comboBox.addItem("F")
        self.comboBox.setMinimumContentsLength(0)
        self.comboBox.setIconSize(QtCore.QSize(16, 16))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.edtTelefone = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.edtTelefone.setObjectName("edtTelefone")
        self.horizontalLayout_3.addWidget(self.edtTelefone)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.edtComum = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.edtComum.setObjectName("edtComum")
        self.horizontalLayout_3.addWidget(self.edtComum)
        self.btnSalvar = QtWidgets.QPushButton(Dialog)
        self.btnSalvar.setGeometry(QtCore.QRect(134, 170, 161, 31))
        self.btnSalvar.setAutoDefault(False)
        self.btnSalvar.setObjectName("btnSalvar")
        self.btnLimpar = QtWidgets.QPushButton(Dialog)
        self.btnLimpar.setGeometry(QtCore.QRect(420, 170, 161, 31))
        self.btnLimpar.setAutoDefault(False)
        self.btnLimpar.setObjectName("btnLimpar")

        #ÍCONE DE VISTO
        self.btnIconeVisto = QtWidgets.QPushButton(Dialog)
        self.btnIconeVisto.setGeometry(QtCore.QRect(300, 167, 33, 33))
        self.btnIconeVisto.setAutoDefault(False)
        self.btnIconeVisto.setObjectName("btnIconeVisto")
        self.iconVisto = QtGui.QIcon()
        self.iconVisto.addPixmap(QtGui.QPixmap("img/visto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIconeVisto.setIcon(self.iconVisto)
        self.btnIconeVisto.setIconSize(QtCore.QSize(40, 40))
        self.btnIconeVisto.hide()

        #ÍCONE DE ERRO
        self.btnIconeErrado = QtWidgets.QPushButton(Dialog)
        self.btnIconeErrado.setGeometry(QtCore.QRect(300, 171, 30, 30))
        self.btnIconeErrado.setAutoDefault(False)
        self.btnIconeErrado.setObjectName("btnIconeErrado")
        self.iconErrado = QtGui.QIcon()
        self.iconErrado.addPixmap(QtGui.QPixmap("img/errado4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIconeErrado.setIcon(self.iconErrado)
        self.btnIconeErrado.setIconSize(QtCore.QSize(55, 55))
        self.btnIconeErrado.hide()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #Conectando ao banco
        self.banco = Acesso_banco.Banco_de_dados()
        self.banco.conectar()

        #Botão que limpa todos os campos
        self.btnLimpar.clicked.connect(self.limpar_campos)

        #Limitando e formatando campos através do método
        self.limitando_e_formatando_campos()

        #Botão que salva dos dados
        self.btnSalvar.clicked.connect(self.salvando_dados)

        #Chamando método de buscar as identidades assim que abrir a tela através da mudança na combobox das identidades
        self.cmbIdentidade.activated.connect(self.busca_identidade)

        #Chamando método de buscar identidade assim que janela abrir
        self.busca_identidade_sem_parametro()




    #MÉTODO QUE SALVA OS DADOS DO PACIENTE
    def salvando_dados(self):
        info = {}
        info['nome'] = self.edtNome.text()
        info['ministerio'] = self.edtMC.text()
        info['identidade'] = self.cmbIdentidade.currentText()+"-"+self.edtIdentidade.text()
        info['cidade'] = self.edtCidade.text()
        info['estado'] = self.edtEstado.text()
        info['pais'] = self.edtPais.text()
        info['idade'] = self.edtIdade.text()
        info['sexo'] = self.comboBox.currentText()
        info['tel'] = self.edtTelefone.text()
        info['comum'] = self.edtComum.text()
        try:
            if info['nome'] != "" and info['ministerio'] != "" and info['cidade'] != "" and info['estado'] != "" and info['pais'] != "" and info['idade'] != "" and info['sexo'] != "" and info['tel'] != "" and info['comum'] != "":
                os.environ['nome_paciente'] = info['nome']
                self.banco.cadastrar_paciente(info)
                if self.btnIconeErrado.isActiveWindow():
                    self.btnIconeErrado.hide()
                    self.btnIconeVisto.show()
                    self.cmbIdentidade.setCurrentIndex(0)
                    self.busca_identidade_sem_parametro()
                else:
                    self.btnIconeVisto.show()

                self.limpar_campos()
            else:
                self.btnIconeErrado.show()
        except:
            self.btnIconeErrado.show()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SISTEMA AMBULATÓRIO - CADASTRO DO PACIENTE"))
        self.label.setText(_translate("Dialog", "Nome Completo:"))
        self.label_2.setText(_translate("Dialog", "Ministério/Cargo:"))
        self.label_3.setText(_translate("Dialog", "Cidade:"))
        self.label_4.setText(_translate("Dialog", "Estado:"))
        self.label_5.setText(_translate("Dialog", "País:"))
        self.label_6.setText(_translate("Dialog", "Idade:"))
        self.label_7.setText(_translate("Dialog", "Sexo:"))
        self.label_8.setText(_translate("Dialog", "Tel/Cel:"))
        self.label_10.setText(_translate("Dialog", "Comum Congregação:"))
        self.btnSalvar.setText(_translate("Dialog", "SALVAR"))
        self.btnLimpar.setText(_translate("Dialog", "LIMPAR"))

    #MÉTODO QUE LIMPA OS CAMPOS
    def limpar_campos(self):
        self.edtNome.clear()
        self.edtMC.clear()
        self.edtPais.clear()
        self.edtComum.clear()
        self.edtIdade.clear()
        self.edtCidade.clear()
        self.edtEstado.clear()
        self.edtTelefone.clear()

    #MÉTODO QUE FORMATA E FORMATA OS CAMPOS
    def limitando_e_formatando_campos(self):
        self.edtNome.setMaxLength(30)
        self.edtIdade.setMaxLength(2)
        self.edtIdade.setInputMask("00")
        self.edtTelefone.setMaxLength(15)
        self.edtTelefone.setInputMask("(00)000000000")
        self.edtComum.setMaxLength(19)
        self.edtMC.setMaxLength(40)
        self.edtCidade.setMaxLength(25)
        self.edtEstado.setMaxLength(25)
        self.edtPais.setMaxLength(15)

    #MÉTODO QUE PEGA SOMENTE A IDENTIDADE
    def busca_identidade(self, indice):
        try:
            if indice == 0:
                letra = "M"
                identidades = self.banco.busca_identidade(letra)
                verifica = identidades == []
                if verifica == True:
                    self.edtIdentidade.setText("1")
                else:
                    next = int(identidades[0][0][2]) + 1
                    self.edtIdentidade.setText(str(next))
            elif indice == 1:
                letra = "C"
                identidades = self.banco.busca_identidade(letra)
                verifica = identidades == []
                if verifica == True:
                    self.edtIdentidade.setText("1")
                else:
                    next = int(identidades[0][0][2]) + 1
                    self.edtIdentidade.setText(str(next))
            elif indice == 2:
                letra = "I"
                identidades = self.banco.busca_identidade(letra)
                verifica = identidades == []
                if verifica == True:
                    self.edtIdentidade.setText("1")
                else:
                    next = int(identidades[0][0][2]) + 1
                    self.edtIdentidade.setText(str(next))
        except:
            print()

    #MÉTODO QUE BUSCA IDENTIDADE MAS SEM PARAMÊTRO
    def busca_identidade_sem_parametro(self):
        try:
            identidade = self.banco.busca_identidade_sem_parametro()
            verifica = identidade == []
            if verifica == True:
                self.edtIdentidade.setText("1")
            else:
                next = int(identidade[0][0][2]) + 1
                self.edtIdentidade.setText(str(next))
        except:
            print()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())