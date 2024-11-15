# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrmMenu(object):
    def setupUi(self, FrmMenu):
        FrmMenu.setObjectName("FrmMenu")
        FrmMenu.resize(1099, 826)
        self.centralwidget = QtWidgets.QWidget(FrmMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 290, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        FrmMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FrmMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1099, 21))
        self.menubar.setObjectName("menubar")
        self.menuEncriptar = QtWidgets.QMenu(self.menubar)
        self.menuEncriptar.setObjectName("menuEncriptar")
        self.menuDesencriptar = QtWidgets.QMenu(self.menubar)
        self.menuDesencriptar.setObjectName("menuDesencriptar")
        self.menuOpciones = QtWidgets.QMenu(self.menubar)
        self.menuOpciones.setObjectName("menuOpciones")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        FrmMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FrmMenu)
        self.statusbar.setObjectName("statusbar")
        FrmMenu.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuEncriptar.menuAction())
        self.menubar.addAction(self.menuDesencriptar.menuAction())
        self.menubar.addAction(self.menuOpciones.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(FrmMenu)
        QtCore.QMetaObject.connectSlotsByName(FrmMenu)

    def retranslateUi(self, FrmMenu):
        _translate = QtCore.QCoreApplication.translate
        FrmMenu.setWindowTitle(_translate("FrmMenu", "Sistema de encriptación de archivos"))
        self.pushButton.setText(_translate("FrmMenu", "Encriptar"))
        self.menuEncriptar.setTitle(_translate("FrmMenu", "Encriptar "))
        self.menuDesencriptar.setTitle(_translate("FrmMenu", "Desencriptar"))
        self.menuOpciones.setTitle(_translate("FrmMenu", "Opciones"))
        self.menuAyuda.setTitle(_translate("FrmMenu", "Ayuda"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmMenu = QtWidgets.QMainWindow()
    ui = Ui_FrmMenu()
    ui.setupUi(FrmMenu)
    FrmMenu.show()
    sys.exit(app.exec_())
