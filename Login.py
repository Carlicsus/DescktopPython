from FrmLogin import *
from Menu import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox  # Agregar QMessageBox aquí
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.lblMensaje.setText("Hola bienvenido a mi App")
        
        self.btnAceptar.clicked.connect(self.validar)
        self.btnCancelar.clicked.connect(self.salir)

    def validar(self):
        usuario = self.txtUsuario.text()
        contrasena = self.txtContrasena.text()
        
        print(usuario)
        print(contrasena)

        if usuario == "Admin" and contrasena == "1234":
            self.lblMensaje.setText("Aceso concedido xd")
            self.openMenu()
            self.hide()
        else:
            self.lblMensaje.setText("Aceso denegado")
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("Error de usuario o contraseña")
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()

    def openMenu(self):
        openNewWindow = Menu(self)
        openNewWindow.show()

    def salir(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("¿Seguro que desea salir?")
        msgBox.setWindowTitle("Salir")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.close()
            

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
    