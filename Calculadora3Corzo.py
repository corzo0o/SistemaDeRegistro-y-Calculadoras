import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class CalculadoraBase:
    """Núcleo de lógica compartido."""
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


class CalculadoraTogaApp(toga.App):
    def startup(self):
        # Elimina todos los menús y comandos automáticos por defecto de Toga
        self.commands.clear()

        self.logic = CalculadoraBase()
        self.main_window = toga.MainWindow(title="Calculadora - Toga", size=(400, 580))
        self.historial_lines = []

        # Pantalla de resultados
        self.txt_pantalla = toga.TextInput(readonly=True, style=Pack(flex=1, padding=5))
        
        # Historial de operaciones
        self.txt_historial = toga.MultilineTextInput(readonly=True, style=Pack(flex=1, padding=5))

        # Botones organizados en filas
        botones = [
            ['C', '(', ')', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]

        button_box = toga.Box(style=Pack(direction=COLUMN, padding=2))
        for fila in botones:
            row_box = toga.Box(style=Pack(direction=ROW, padding=2))
            for texto in fila:
                btn = toga.Button(texto, on_press=self.on_click_boton, style=Pack(flex=1, padding=2))
                row_box.add(btn)
            button_box.add(row_box)

        # Contenedor principal sin menús
        main_box = toga.Box(
            style=Pack(direction=COLUMN, padding=10),
            children=[
                toga.Label("Pantalla:", style=Pack(padding_bottom=2)),
                self.txt_pantalla,
                toga.Label("Historial (Últimas 5 operaciones):", style=Pack(padding_top=5, padding_bottom=2)),
                self.txt_historial,
                toga.Label("Controles:", style=Pack(padding_top=5, padding_bottom=2)),
                button_box
            ]
        )

        self.main_window.content = main_box
        self.main_window.show()

    def on_click_boton(self, widget):
        texto = widget.text
        if texto == 'C':
            res = self.logic.limpiar()
            self.txt_pantalla.value = res
        elif texto == '=':
            resultado, operacion = self.logic.calcular()
            self.txt_pantalla.value = resultado
            if operacion:
                self.historial_lines.append(operacion)
                if len(self.historial_lines) > 5:
                    self.historial_lines.pop(0)
                self.txt_historial.value = "\n".join(self.historial_lines)
        else:
            res = self.logic.agregar(texto)
            self.txt_pantalla.value = res

def main():
    return CalculadoraTogaApp('Calculadora Toga', 'org.beeware.calculadora')

if __name__ == '__main__':
    main().main_loop()