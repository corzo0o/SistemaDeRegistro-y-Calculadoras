import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QDialog,
    QLabel,
    QPushButton,
    QLineEdit,
    QTextEdit,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QFormLayout,
    QCheckBox,
    QRadioButton,
    QComboBox,
    QMessageBox
)

class RegistroWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Registro - Versión Normal")
        self.setMinimumSize(500, 600)

        # Widget central y layout principal
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        main_layout = QVBoxLayout(self.central_widget)

        # Título
        self.lbl_titulo = QLabel("Formulario de Registro de Usuario")
        self.lbl_titulo.setStyleSheet("font-size: 16px; font-weight: bold; margin-bottom: 10px;")
        main_layout.addWidget(self.lbl_titulo)

        # Usando QFormLayout para los datos personales
        form_layout = QFormLayout()
        
        self.txt_nombre = QLineEdit()
        self.txt_email = QLineEdit()
        self.txt_password = QLineEdit()
        self.txt_password.setEchoMode(QLineEdit.EchoMode.Password)
        
        form_layout.addRow(QLabel("Nombre completo:"), self.txt_nombre)
        form_layout.addRow(QLabel("Correo electrónico:"), self.txt_email)
        form_layout.addRow(QLabel("Contraseña:"), self.txt_password)
        
        main_layout.addLayout(form_layout)

        # Usando QGridLayout para opciones de selección (Género y Tipo de Cuenta)
        grid_layout = QGridLayout()
        
        grid_layout.addWidget(QLabel("Género:"), 0, 0)
        self.rb_masculino = QRadioButton("Masculino")
        self.rb_femenino = QRadioButton("Femenino")
        self.rb_otro = QRadioButton("Otro")
        
        gender_layout = QHBoxLayout()
        gender_layout.addWidget(self.rb_masculino)
        gender_layout.addWidget(self.rb_femenino)
        gender_layout.addWidget(self.rb_otro)
        grid_layout.addLayout(gender_layout, 0, 1)

        grid_layout.addWidget(QLabel("País:"), 1, 0)
        self.cmb_pais = QComboBox()
        self.cmb_pais.addItems(["Bolivia", "Argentina", "Chile", "Colombia", "México", "España", "Otro"])
        grid_layout.addWidget(self.cmb_pais, 1, 1)

        main_layout.addLayout(grid_layout)

        # Usando QCheckBox para preferencias
        self.chk_terminos = QCheckBox("Acepto los términos y condiciones")
        self.chk_newsletter = QCheckBox("Suscribirse al boletín de noticias")
        main_layout.addWidget(self.chk_terminos)
        main_layout.addWidget(self.chk_newsletter)

        # Usando QTextEdit para observaciones o biografía
        main_layout.addWidget(QLabel("Comentarios adicionales:"))
        self.txt_comentarios = QTextEdit()
        self.txt_comentarios.setMaximumHeight(100)
        main_layout.addWidget(self.txt_comentarios)

        # Botones de acción usando QHBoxLayout
        btn_layout = QHBoxLayout()
        self.btn_guardar = QPushButton("Registrar")
        self.btn_limpiar = QPushButton("Limpiar")
        
        self.btn_guardar.clicked.connect(self.realizar_registro)
        self.btn_limpiar.clicked.connect(self.limpiar_campos)
        
        btn_layout.addWidget(self.btn_guardar)
        btn_layout.addWidget(self.btn_limpiar)
        
        main_layout.addLayout(btn_layout)

    def realizar_registro(self):
        if not self.chk_terminos.isChecked():
            QMessageBox.warning(self, "Advertencia", "Debes aceptar los términos y condiciones.")
            return
        
        nombre = self.txt_nombre.text().strip()
        if not nombre:
            QMessageBox.warning(self, "Advertencia", "El campo de nombre es obligatorio.")
            return

        QMessageBox.information(self, "Éxito", f"¡Usuario {nombre} registrado correctamente!")

    def limpiar_campos(self):
        self.txt_nombre.clear()
        self.txt_email.clear()
        self.txt_password.clear()
        self.txt_comentarios.clear()
        self.chk_terminos.setChecked(False)
        self.chk_newsletter.setChecked(False)
        self.rb_masculino.setChecked(False)
        self.rb_femenino.setChecked(False)
        self.rb_otro.setChecked(False)
        self.cmb_pais.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistroWindow()
    window.show()
    sys.exit(app.exec())