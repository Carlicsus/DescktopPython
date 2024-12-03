from FrmDesencriptar import *
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from PyQt5.QtWidgets import QFileDialog, QMessageBox # Importa QFileDialog para abrir archivos
from datetime import *
from PyQt5.QtGui import QPixmap
import io
from PIL import Image
import base64


class Desencriptar(QtWidgets.QMainWindow, Ui_Desincriptar):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)
        
        self.btnCargarImg.clicked.connect(self.cargarImagen)
        self.btnEncriptarImg.clicked.connect(self.encriptarImagen)
        self.btnSaveImagen.clicked.connect(self.guardarImagenEncriptada)
        
        self.btnCargarImg2.clicked.connect(self.cargarImagenDesencrip)
        self.btnDesencriptarImg.clicked.connect(self.desencriptarImagen)
        self.btnSaveImagen2.clicked.connect(self.guardarImagenDesencrip)
        
        self.imagen_encriptada2 = None
        self.imagen_desencriptada = None
        self.imagen_original = None
        self.imagen_encriptada = None
        
    def cargarImagenDesencrip(self):
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getOpenFileName(self, "Abrir archivo encriptado", "", "Archivos binarios (*.bin);;Todos los archivos (*)", options=opciones)

        if archivo:
            try:
                with open(archivo, "rb") as f:
                    self.imagen_encriptada2 = f.read()
                self.ImgEncriptada2.setText("Imagen encriptada cargada correctamente.")
                self.ImgEncriptada2.setStyleSheet("color: green;")
            except Exception as e:
                QtWidgets.QMessageBox.warning(self, "Error", f"No se pudo cargar la imagen: {str(e)}")
                
    def desencriptarImagen(self):
        if not self.imagen_encriptada2:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Primero debes cargar una imagen encriptada.")
            return

        try:
            # Clave e IV para desencriptar
            key = b"12345678912345678912345678912345"  # 32 bytes
            iv = b"TI_UTXJ2024ENCRI"

            # Desencriptar los datos
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            decrypted_data = decryptor.update(self.imagen_encriptada2) + decryptor.finalize()

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
            
    def guardarImagenDesencrip(self):
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
                
    def cargarImagen(self):
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getOpenFileName(
            self, "Abrir imagen", "", "Imágenes (*.png *.jpg *.jpeg);;Todos los archivos (*)", options=opciones
        )

        if archivo:
            self.imagen_original = archivo
            self.ImgNormal.setText("Imagen cargada correctamente")
            pixmap = QtGui.QPixmap(archivo)
            self.ImgNormal.setPixmap(pixmap.scaled(self.ImgNormal.size(), QtCore.Qt.KeepAspectRatio))
    
    def encriptarImagen(self):
        if not self.imagen_original:
            QMessageBox.warning(self, "Advertencia", "No se ha cargado ninguna imagen para encriptar.")
            return

        key = b"12345678912345678912345678912345"  # Clave AES de 32 bytes
        iv = b"TI_UTXJ2024ENCRI"  # IV de 16 bytes

        try:
            # Leer la imagen y convertirla en datos binarios
            with open(self.imagen_original, "rb") as img_file:
                datos_imagen = img_file.read()

            # Encriptar los datos
            padder = padding.PKCS7(128).padder()
            padded_data = padder.update(datos_imagen) + padder.finalize()

            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            self.imagen_encriptada = encryptor.update(padded_data) + encryptor.finalize()

            self.ImgEncriptada.setText("Imagen encriptada correctamente")
            pixmap = QtGui.QPixmap("img/encriptar_shell.png")
            self.ImgEncriptada.setPixmap(pixmap.scaled(self.ImgEncriptada.size(), QtCore.Qt.KeepAspectRatio))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error al encriptar la imagen: {str(e)}")
            
    def guardarImagenEncriptada(self):
        if not self.imagen_encriptada:
            QMessageBox.warning(self, "Advertencia", "No hay imagen encriptada para guardar.")
            return

        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getSaveFileName(
            self, "Guardar imagen encriptada", "", "Archivos binarios (*.bin);;Todos los archivos (*)", options=opciones
        )

        if archivo:
            try:
                with open(archivo, "wb") as f:
                    f.write(self.imagen_encriptada)
                QMessageBox.information(self, "Éxito", "Imagen encriptada guardada correctamente.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Ocurrió un error al guardar la imagen: {str(e)}")