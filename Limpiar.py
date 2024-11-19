from FrmLimpiar import *
from cryptography.hazmat.primitives import padding

class Limpiar(QtWidgets.QMainWindow, Ui_FrmLimpiar):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)
        
        self.btn_encriptar.clicked.connect(self.encriptarAES)
        
    def encriptarAES(self):
        data= self.txt_mensaje.toPlainText()

        key= b"12345678912345678912345678912345" #32
        iv = b"TI_UTXJ2024ENCRI"
        
        padder= padding.PKCS7(128).padder()
        print(padder)