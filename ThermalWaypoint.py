# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cataterimca22.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!
import re
from sys import path
from os.path import abspath, dirname
from __init__ import Waypoint
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(194, 247)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.button_gerar = QtGui.QPushButton(self.centralwidget)
        self.button_gerar.setGeometry(QtCore.QRect(50, 70, 85, 26))
        self.button_gerar.setObjectName(_fromUtf8("button_gerar"))
        self.button_gerar.hide()
        #quando o botao e clicado, algo e conectado
        self.button_gerar.clicked.connect(self.valor_termica)
        self.nofileselected = QtGui.QLabel(self.centralwidget)
        self.nofileselected.setGeometry(QtCore.QRect(0, 0, 191, 41))
        self.nofileselected.setObjectName(_fromUtf8("nofileselected"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(130, 40, 51, 21))
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        #esconde a doublespinbox
        self.doubleSpinBox.hide()
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(8, 40, 121, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        #esconde a label
        self.label_2.hide()
        self.sucesso = QtGui.QLabel(self.centralwidget)
        self.sucesso.setEnabled(True)
        self.sucesso.setGeometry(QtCore.QRect(10, 170, 171, 41))
        self.sucesso.setObjectName(_fromUtf8("sucesso"))
        self.sucesso.hide() #esconder
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 194, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArquivo = QtGui.QMenu(self.menubar)
        self.menuArquivo.setObjectName(_fromUtf8("menuArquivo"))
        self.menuSobre = QtGui.QMenu(self.menubar)
        self.menuSobre.setObjectName(_fromUtf8("menuSobre"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbrir_Ctrl_O = QtGui.QAction(MainWindow)
        self.actionAbrir_Ctrl_O.setObjectName(_fromUtf8("actionAbrir_Ctrl_O"))
        self.actionAbrir_Ctrl_O.setShortcut("Ctrl+O")
        self.actionAbrir_Ctrl_O.triggered.connect(self._open_file_cb)
        self.actionSobre = QtGui.QAction(MainWindow)
        self.actionSobre.setObjectName(_fromUtf8("actionSobre"))
        #self.actionSobre.triggered.connect(self.file_save)
        self.menuArquivo.addAction(self.actionAbrir_Ctrl_O)
        self.menuSobre.addAction(self.actionSobre)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())
        self.diretorio_do_arquivo = ''
        self.w = None

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ThermalWaypoint V0.1", None))
        self.button_gerar.setText(_translate("MainWindow", "Gerar!", None))
        self.nofileselected.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\">Selecione um arquivo IGC!</span></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "Intensidade mínima:", None))
        self.sucesso.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#0000ff;\">Rota Gerada com Sucesso!</span></p></body></html>", None))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo", None))
        self.menuSobre.setTitle(_translate("MainWindow", "Ajuda", None))
        self.actionAbrir_Ctrl_O.setText(_translate("MainWindow", "Abrir...", None))
        self.actionSobre.setText(_translate("MainWindow", "Sobre...", None))

    def _open_file_cb(self, MainWindow):
        #encontrar diretorio do arquivo
        self.diretorio_do_arquivo = QtGui.QFileDialog.getOpenFileName(caption='Abrir Arquivo IGC')
        self.sucesso.hide()
        if self.diretorio_do_arquivo != '':
         self.nofileselected.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#0000ff;\">Arquivo Selecionado!</span></p></body></html>", None))    
         self.label_2.show()
         self.doubleSpinBox.show()
         self.button_gerar.show()

    
    def valor_termica(self, MainWindow):
        subida = float(self.doubleSpinBox.text()[0]+"."+self.doubleSpinBox.text()[2])
        arquivo = open(str(self.diretorio_do_arquivo.toUtf8()).decode('utf-8'),'r')
        leitura = arquivo.readlines()
        leitura = filter(lambda s: s[0]=='B', leitura)
        linhas = len(leitura)
        name = QtGui.QFileDialog.getSaveFileName(caption='Salvar Arquivo')
        f = open(str(name.toUtf8()).decode('utf-8')+".cup","w")
        
        #checar o tamanho da variação de segundos de uma linha para outra
        #verificando qual das duas variaçoes é > 0 e colocando o resultado numa variavel
        variacaolinha = int(leitura[2][5:7]) - int(leitura[1][5:7])
        if ( variacaolinha == 0 ):
          variacaolinha = int(leitura[1][5:7]) - int(leitura[0][5:7])
                  
        #calcular o delta por todo o arquivo
        z = 1
        i = 1
        calculo0 = float(leitura[z-1][31:35])
        while (int(z) < int(linhas)):      
           #identifica as termais e coloca em out2
           calculo = (float(leitura[z][31:35]) - float(calculo0)) / float(variacaolinha)
           calculo0 = float(leitura[z][31:35])
           if (float(calculo) >= float(subida)):
             linha = leitura[z-1]
             linha = linha.strip()
             altura    = re.findall(r'(?<=A\d{5})\d{5}', linha)[0]
             alturaint = int(altura) #alguns registros tem que tirar o -5 pela ausência dos 00000
             latitude  = linha[7:15] # linha[7:14] + linha[14]
             longitude = linha[15:24] # linha[15:23] + linha[23]
             lat       = latitude[:4] + "." + latitude[4:]
             long      = longitude[:5] + "." + longitude[5:]
             wp = Waypoint(None,"",lat,long,alturaint,i)
             i += 1
             print >>f, wp
           z +=1
          
        f.flush()
        f.close()
        self.sucesso.show()

        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
