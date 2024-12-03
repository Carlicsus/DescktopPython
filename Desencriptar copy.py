from FrmDesencriptar import *
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from PyQt5.QtWidgets import QFileDialog  # Importa QFileDialog para abrir archivos
from datetime import *
from PyQt5.QtGui import QPixmap
import io
from PIL import Image
import base64


class Desencriptar(QtWidgets.QMainWindow, Ui_Desincriptar):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)
        
        self.btn_desencriptar.clicked.connect(self.desencriptarAES)
        self.btn_limpiar.clicked.connect(self.limpiar)
        self.btn_cargar.clicked.connect(self.cargarArchivo)  # Conectar el botón con la función cargarArchivo
        self.btn_save.clicked.connect(self.guardarArchivo)  # Conectar el botón con la función guardarArchivo
        
        self.btnCargarImg.clicked.connect(self.cargarImagen)
        self.btnDesencriptarImg.clicked.connect(self.desencriptarImagen)
        self.btnSaveImagen.clicked.connect(self.guardarImagen)
        
        self.imagen_encriptada = None
        self.imagen_desencriptada = None
        
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
    
    def cargarImagen(self):
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getOpenFileName(self, "Abrir archivo encriptado", "", "Archivos binarios (*.bin);;Todos los archivos (*)", options=opciones)

        if archivo:
            try:
                with open(archivo, "rb") as f:
                    self.imagen_encriptada = f.read()
                self.ImgEncriptada.setText("Imagen encriptada cargada correctamente.")
                self.ImgEncriptada.setStyleSheet("color: green;")
            except Exception as e:
                QtWidgets.QMessageBox.warning(self, "Error", f"No se pudo cargar la imagen: {str(e)}")
                
    def desencriptarImagen(self):
        if not self.imagen_encriptada:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Primero debes cargar una imagen encriptada.")
            return

        try:
            # Clave e IV para desencriptar
            key = b"12345678912345678912345678912345"  # 32 bytes
            iv = b"TI_UTXJ2024ENCRI"

            # Desencriptar los datos
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            decrypted_data = decryptor.update(self.imagen_encriptada) + decryptor.finalize()

            # Convertir datos desencriptados a una imagen
            image_stream = io.BytesIO(decrypted_data)
            image = Image.open(image_stream)

            # Mostrar imagen desencriptada en la interfaz
            image.save("temporal_desencriptada.png")  # Guardar temporalmente para mostrar
            pixmap = QPixmap("temporal_desencriptada.png")
            self.ImgDesencriptada.setPixmap(pixmap.scaled(self.ImgDesencriptada.size(), QtCore.Qt.KeepAspectRatio))
            self.imagen_desencriptada = image

            self.TxtImgDesencriptada.setText("Imagen desencriptada correctamente.")
            self.TxtImgDesencriptada.setStyleSheet("color: green;")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", f"Error al desencriptar la imagen: {str(e)}")
            
    def guardarImagen(self):
        if not self.imagen_desencriptada:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "No hay imagen desencriptada para guardar.")
            return

        opciones = QFileDialog.Options()
        fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        archivo, _ = QFileDialog.getSaveFileName(self, "Guardar imagen desencriptada", f"imagen_desencriptada_{fecha}.png", "Archivos de imagen (*.png);;Todos los archivos (*)", options=opciones)

        if archivo:
            try:
                self.imagen_desencriptada.save(archivo, format="PNG")
                QtWidgets.QMessageBox.information(self, "Éxito", "Imagen desencriptada guardada exitosamente.")
            except Exception as e:
                QtWidgets.QMessageBox.warning(self, "Error", f"No se pudo guardar la imagen: {str(e)}")