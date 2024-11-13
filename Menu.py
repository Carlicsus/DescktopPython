from FrmMenu import *
from Limpiar import *

class Menu(QtWidgets.QMainWindow, Ui_FrmMenu):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.openEncript)

    def openEncript(self):
        openNewWindow = Limpiar(self)
        openNewWindow.show()
        self.hide()