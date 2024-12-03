from FrmLimpiar import *
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from PyQt5.QtWidgets import QFileDialog  # Importa QFileDialog para abrir archivos
from datetime import *
import base64



class Limpiar(QtWidgets.QMainWindow, Ui_FrmLimpiar):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)
        
        self.btn_encriptar.clicked.connect(self.encriptarAES)
        self.btn_limpiar.clicked.connect(self.limpiar)
        self.btn_cargar.clicked.connect(self.cargarArchivo)  # Conectar el botón con la función cargarArchivo
        self.btn_save.clicked.connect(self.guardarArchivo)  # Conectar el botón con la función guardarArchivo


        
    def encriptarAES(self):
        data= self.txt_mensaje.toPlainText()

        key= b"12345678912345678912345678912345" #32
        iv = b"TI_UTXJ2024ENCRI"
        
        padder= padding.PKCS7(128).padder()
        padded_data = padder.update(data.encode('utf-8'))
        padded_data += padder.finalize()
        cipher = Cipher(algorithms.AES(key),modes.CBC(iv), backend = default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data)+encryptor.finalize()
        # Convertir el resultado en Base64 para poder manejarlo como texto
        b64_ciphertext = base64.b64encode(ciphertext).decode('utf-8')

        # Mostrar el texto encriptado (Base64) en la etiqueta
        self.label_4.setText(b64_ciphertext)
        
    def limpiar(self):
        self.label_4.clear()
        self.txt_mensaje.clear()

    def cargarArchivo(self):
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Archivos de texto (*.txt);;Todos los archivos (*)", options=opciones)

        if archivo:
            with open(archivo, 'r', encoding='utf-8') as f:
                contenido = f.read()
                self.txt_mensaje.setText(contenido)
                
    def guardarArchivo(self):
        texto_encriptado = self.label_4.text()

        if not texto_encriptado:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "No hay texto encriptado para guardar.")
            return

        fecha=datetime.now()
        fechaFormat=fecha.strftime("%m-%d-%Y%H-%M-%S")

        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", f"{fechaFormat}", "Archivos de texto (*.txt);;Todos los archivos (*)", options=opciones)

        if archivo:
            with open(archivo, 'w', encoding='utf-8') as f:
                f.write(texto_encriptado) 