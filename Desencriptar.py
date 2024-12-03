from FrmDesencriptar import *
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from PyQt5.QtWidgets import QFileDialog  # Importa QFileDialog para abrir archivos
from datetime import *
import base64


class Desencriptar(QtWidgets.QMainWindow, Ui_Desincriptar):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)
        
        self.btn_desencriptar.clicked.connect(self.desencriptarAES)
        self.btn_limpiar.clicked.connect(self.limpiar)
        self.btn_cargar.clicked.connect(self.cargarArchivo)  # Conectar el botón con la función cargarArchivo
        self.btn_save.clicked.connect(self.guardarArchivo)  # Conectar el botón con la función guardarArchivo
        
    def desencriptarAES(self):
        # Obtener el texto encriptado desde el label_4
        b64_ciphertext = self.txt_mensaje.toPlainText()

        if not b64_ciphertext:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "No hay texto encriptado para desencriptar.")
            return

        try:

            ciphertext = base64.b64decode(b64_ciphertext)
            
            # Clave e IV para desencriptar
            key = b"12345678912345678912345678912345"  # 32 bytes
            iv = b"TI_UTXJ2024ENCRI"

            # Desencriptar los datos
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            padded_data = decryptor.update(ciphertext) + decryptor.finalize()

            # Eliminar el padding
            unpadder = padding.PKCS7(128).unpadder()
            data = unpadder.update(padded_data)
            data += unpadder.finalize()

            # Convertir el texto desencriptado de vuelta a cadena
            self.label_4.setText(data.decode('utf-8'))  # Mostrar el mensaje desencriptado

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", f"Error al desencriptar el texto: {str(e)}")
        
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