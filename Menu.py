from FrmMenu import *

class Menu(QtWidgets.QMainWindows, Ui_FrmMenu):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)