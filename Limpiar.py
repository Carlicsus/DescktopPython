from FrmLimpiar import *
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from PyQt5.QtWidgets import QFileDialog, QMessageBox # Importa QFileDialog para abrir archivos
from datetime import *
import base64
from PyQt5.QtGui import QPixmap
import os
from PIL import Image
from io import BytesIO



class Limpiar(QtWidgets.QMainWindow, Ui_FrmLimpiar):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)
        
        self.btn_encriptar.clicked.connect(self.encriptarAES)
        self.btn_limpiar.clicked.connect(self.limpiarEncrip)
        self.btn_cargar.clicked.connect(self.cargarArchivoEncrip)  # Conectar el botón con la función cargarArchivo
        self.btn_save.clicked.connect(self.guardarArchivoEncrip)  # Conectar el botón con la función guardarArchivo
        
        self.btn_desencriptar.clicked.connect(self.desencriptarAES)
        self.btn_limpiar_2.clicked.connect(self.limpiarDes)
        self.btn_cargar_2.clicked.connect(self.cargarArchivo)  # Conectar el botón con la función cargarArchivo
        self.btn_save_2.clicked.connect(self.guardarArchivo)

        
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
        self.txtMensageEncrip.setText(b64_ciphertext)
        
    def limpiarEncrip(self):
        self.txtMensageEncrip.clear()
        self.txt_mensaje.clear()

    def cargarArchivoEncrip(self):
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Archivos de texto (*.txt);;Todos los archivos (*)", options=opciones)

        if archivo:
            with open(archivo, 'r', encoding='utf-8') as f:
                contenido = f.read()
                print(contenido)
                self.txt_mensaje.setText(contenido)
                
    def guardarArchivoEncrip(self):
        texto_encriptado = self.txtMensageEncrip.text()

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
                
    def desencriptarAES(self):
        # Obtener el texto encriptado desde el label_4
        b64_ciphertext = self.txt_mensaje_2.toPlainText()

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
            self.txtMensageDesencrip.setText(data.decode('utf-8'))  # Mostrar el mensaje desencriptado

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", f"Error al desencriptar el texto: {str(e)}")
        
    def limpiarDes(self):
        self.txtMensageDesencrip.clear()
        self.txt_mensaje_2.clear()

    def cargarArchivo(self):
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Archivos de texto (*.txt);;Todos los archivos (*)", options=opciones)

        if archivo:
            with open(archivo, 'r', encoding='utf-8') as f:
                contenido = f.read()
                self.txt_mensaje_2.setText(contenido)
                
    def guardarArchivo(self):
        texto_desencriptado = self.txtMensageDesencrip.text()

        if not texto_desencriptado:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "No hay texto encriptado para guardar.")
            return

        fecha=datetime.now()
        fechaFormat=fecha.strftime("%m-%d-%Y%H-%M-%S")

        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", f"{fechaFormat}", "Archivos de texto (*.txt);;Todos los archivos (*)", options=opciones)

        if archivo:
            with open(archivo, 'w', encoding='utf-8') as f:
                f.write(texto_desencriptado)
    