# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmLimpiar.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrmLimpiar(object):
    def setupUi(self, FrmLimpiar):
        FrmLimpiar.setObjectName("FrmLimpiar")
        FrmLimpiar.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(FrmLimpiar)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 70, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 110, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 150, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(600, 190, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 70, 521, 191))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 300, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 350, 391, 141))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        FrmLimpiar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FrmLimpiar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        FrmLimpiar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FrmLimpiar)
        self.statusbar.setObjectName("statusbar")
        FrmLimpiar.setStatusBar(self.statusbar)

        self.retranslateUi(FrmLimpiar)
        QtCore.QMetaObject.connectSlotsByName(FrmLimpiar)

    def retranslateUi(self, FrmLimpiar):
        _translate = QtCore.QCoreApplication.translate
        FrmLimpiar.setWindowTitle(_translate("FrmLimpiar", "MainWindow"))
        self.pushButton.setText(_translate("FrmLimpiar", "Encriptar"))
        self.pushButton_2.setText(_translate("FrmLimpiar", "Limpiar"))
        self.pushButton_3.setText(_translate("FrmLimpiar", "Cargar Archivo"))
        self.pushButton_4.setText(_translate("FrmLimpiar", "Guardar archivo"))
        self.label.setText(_translate("FrmLimpiar", "Mensaje"))
        self.label_3.setText(_translate("FrmLimpiar", "Mensaje Encriptado"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmLimpiar = QtWidgets.QMainWindow()
    ui = Ui_FrmLimpiar()
    ui.setupUi(FrmLimpiar)
    FrmLimpiar.show()
    sys.exit(app.exec_())