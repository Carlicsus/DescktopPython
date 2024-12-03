from FrmMenu import *
from Limpiar import *
from Desencriptar import *

class Menu(QtWidgets.QMainWindow, Ui_FrmMenu):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.openEncript)

        self.menuEncriptar.addAction("Encriptar", self.openEncript)
        self.menuEncriptar.addAction("Desencriptar", self.openDesencript)

    def openEncript(self):
        openNewWindow = Limpiar(self)
        openNewWindow.show()
        self.hide()
        
    def openDesencript(self):
        openNewWindow = Desencriptar(self)
        openNewWindow.show()
        self.hide()
        