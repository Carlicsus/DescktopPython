from FrmLogin import *

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.lblMensaje.setText("Hola bienvenido a mi App")
        
        self.btnAceptar.clicked.connect(self.validar)

    def validar(self):
        usuario = self.txtUsuario.text()
        contrasena = self.txtContrasena.text()
        
        print(usuario)
        print(contrasena)

        if usuario == "Admin" and contrasena == "1234":
            self.lblMensaje.setText("Aceso concedido xd")
        else:
            self.lblMensaje.setText("Aceso denegado")
            

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
    