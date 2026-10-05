import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QGridLayout,
    QListWidget,
    QMessageBox
)

class CalculadoraBase:
    """Clase con la lógica central de la calculadora compartida."""
    def __init__(self):
        self.expresion = ""

    def agregar(self, valor):
        self.expresion += str(valor)
        return self.expresion

    def limpiar(self):
        self.expresion = ""
        return self.expresion

    def calcular(self):
        try:
            exp_eval = self.expresion.replace('×', '*').replace('÷', '/')
            resultado = str(eval(exp_eval))
            operacion_completa = f"{self.expresion} = {resultado}"
            self.expresion = resultado
            return resultado, operacion_completa
        except Exception:
            self.expresion = ""
            return "Error", None


class CalculadoraConMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora 4 - Con Menú (PySide6)")
        self.setMinimumSize(400, 580)

        self.logic = CalculadoraBase()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Pantalla de resultados
        self.txt_pantalla = QLineEdit()
        self.txt_pantalla.setReadOnly(True)
        self.txt_pantalla.setStyleSheet("font-size: 24px; padding: 10px; background-color: #f0f0f0;")
        self.txt_pantalla.setAlignment(Qt.AlignmentFlag.AlignRight)
        main_layout.addWidget(self.txt_pantalla)

        # Historial de últimas 5 operaciones (Creado ANTES del menú)
        main_layout.addWidget(QLabel("Historial (Últimas 5 operaciones):"))
        self.list_historial = QListWidget()
        self.list_historial.setMaximumHeight(100)
        main_layout.addWidget(self.list_historial)

        # Botones de la calculadora
        grid_layout = QGridLayout()
        botones = [
            ('C', 0, 0), ('(', 0, 1), (')', 0, 2), ('÷', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('×', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0, 1, 2), ('.', 4, 2), ('=', 4, 3)
        ]

        for boton_info in botones:
            texto = boton_info[0]
            fila = boton_info[1]
            columna = boton_info[2]
            rowSpan = boton_info[3] if len(boton_info) > 4 else 1
            colSpan = boton_info[4] if len(boton_info) > 4 else 1

            btn = QPushButton(texto)
            btn.setStyleSheet("font-size: 18px; padding: 15px;")
            btn.clicked.connect(lambda checked, t=texto: self.on_click_boton(t))
            grid_layout.addWidget(btn, fila, columna, rowSpan, colSpan)

        main_layout.addLayout(grid_layout)

        # Creación de la barra de menú superior (AHORA SÍ, después de crear los componentes)
        self.crear_menu()

    def crear_menu(self):
        menu_bar = self.menuBar()

        # Menú Archivo
        menu_archivo = menu_bar.addMenu("Archivo")
        
        accion_limpiar_historial = QAction("Limpiar Historial", self)
        accion_limpiar_historial.triggered.connect(self.list_historial.clear)
        menu_archivo.addAction(accion_limpiar_historial)

        menu_archivo.addSeparator()

        accion_salir = QAction("Salir", self)
        accion_salir.triggered.connect(self.close)
        menu_archivo.addAction(accion_salir)

        # Menú Ayuda
        menu_ayuda = menu_bar.addMenu("Ayuda")
        accion_acerca = QAction("Acerca de", self)
        accion_acerca.triggered.connect(self.mostrar_acerca)
        menu_ayuda.addAction(accion_acerca)

    def mostrar_acerca(self):
        QMessageBox.information(
            self, 
            "Acerca de", 
            "Calculadora con Menú (PySide6)\nCalculadora creada por Gerson Corzo."
        )

    def on_click_boton(self, texto):
        if texto == 'C':
            res = self.logic.limpiar()
            self.txt_pantalla.setText(res)
        elif texto == '=':
            resultado, operacion = self.logic.calcular()
            self.txt_pantalla.setText(resultado)
            if operacion:
                self.list_historial.addItem(operacion)
                if self.list_historial.count() > 5:
                    self.list_historial.takeItem(0)
        else:
            res = self.logic.agregar(texto)
            self.txt_pantalla.setText(res)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculadoraConMenuWindow()
    window.show()
    sys.exit(app.exec())