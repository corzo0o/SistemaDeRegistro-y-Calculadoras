import wx

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


class CalculadoraWxFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Calculadora - wxPython", size=(400, 600))

        self.logic = CalculadoraBase()
        panel = wx.Panel(self)
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Pantalla
        self.txt_pantalla = wx.TextCtrl(panel, style=wx.TE_RIGHT | wx.TE_READONLY)
        self.txt_pantalla.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        main_sizer.Add(self.txt_pantalla, 0, wx.ALL | wx.EXPAND, 10)

        # Historial
        main_sizer.Add(wx.StaticText(panel, label="Historial (Últimas 5 operaciones):"), 0, wx.LEFT, 10)
        self.list_historial = wx.ListBox(panel, choices=[])
        main_sizer.Add(self.list_historial, 1, wx.ALL | wx.EXPAND, 10)

        # Botones en Grid
        grid_sizer = wx.GridSizer(rows=5, cols=4, hgap=5, vgap=5)
        botones = [
            'C', '(', ')', '÷',
            '7', '8', '9', '×',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '='
        ]

        for texto in botones:
            btn = wx.Button(panel, label=texto, size=(-1, 45))
            btn.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
            btn.Bind(wx.EVT_BUTTON, lambda evt, t=texto: self.on_click_boton(t))
            grid_sizer.Add(btn, 0, wx.EXPAND)

        main_sizer.Add(grid_sizer, 0, wx.ALL | wx.EXPAND, 10)
        panel.SetSizer(main_sizer)
        self.Centre()

    def on_click_boton(self, texto):
        if texto == 'C':
            res = self.logic.limpiar()
            self.txt_pantalla.SetValue(res)
        elif texto == '=':
            resultado, operacion = self.logic.calcular()
            self.txt_pantalla.SetValue(resultado)
            if operacion:
                self.list_historial.Append(operacion)
                if self.list_historial.GetCount() > 5:
                    self.list_historial.Delete(0)
        else:
            res = self.logic.agregar(texto)
            self.txt_pantalla.SetValue(res)

if __name__ == "__main__":
    app = wx.App()
    frame = CalculadoraWxFrame()
    frame.Show()
    app.MainLoop()