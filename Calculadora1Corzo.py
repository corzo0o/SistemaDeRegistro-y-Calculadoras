import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QListWidget
)

class CalculadoraBase:
    """Clase con la lógica central de la calculadora para compartir entre versiones."""
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
            # Reemplazamos símbolos visuales por operadores de Python seguros
            exp_eval = self.expresion.replace('×', '*').replace('÷', '/')
            resultado = str(eval(exp_eval))
            operacion_completa = f"{self.expresion} = {resultado}"
            self.expresion = resultado
            return resultado, operacion_completa
        except Exception:
            self.expresion = ""
            return "Error", None


class CalculadoraWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora 1 - Con Historial (PyQt6)")
        self.setMinimumSize(400, 550)

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

        # Historial de últimas 5 operaciones
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

    def on_click_boton(self, texto):
        if texto == 'C':
            res = self.logic.limpiar()
            self.txt_pantalla.setText(res)
        elif texto == '=':
            resultado, operacion = self.logic.calcular()
            self.txt_pantalla.setText(resultado)
            if operacion:
                # Agregar al historial manteniendo máximo 5 elementos
                self.list_historial.addItem(operacion)
                if self.list_historial.count() > 5:
                    self.list_historial.takeItem(0)
        else:
            res = self.logic.agregar(texto)
            self.txt_pantalla.setText(res)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculadoraWindow()
    window.show()
    sys.exit(app.exec())