import flet as ft

def main(page: ft.Page):
    page.title = "Sistema de Registro - Versión Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    page.window_width = 520
    page.window_height = 700

    # Campos de texto
    txt_nombre = ft.TextField(label="Nombre completo:", width=450)
    txt_email = ft.TextField(label="Correo electrónico:", width=450)
    txt_password = ft.TextField(label="Contraseña:", password=True, can_reveal_password=True, width=450)

    # Género (RadioGroup)
    rb_genero = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Masculino", label="Masculino"),
            ft.Radio(value="Femenino", label="Femenino"),
            ft.Radio(value="Otro", label="Otro"),
        ])
    )

    # País (Dropdown)
    cmb_pais = ft.Dropdown(
        label="País",
        value="Bolivia",
        options=[
            ft.dropdown.Option("Bolivia"),
            ft.dropdown.Option("Argentina"),
            ft.dropdown.Option("Chile"),
            ft.dropdown.Option("Colombia"),
            ft.dropdown.Option("México"),
            ft.dropdown.Option("España"),
            ft.dropdown.Option("Otro"),
        ],
        width=450
    )

    # Checkboxes
    chk_terminos = ft.Checkbox(label="Acepto los términos y condiciones")
    chk_newsletter = ft.Checkbox(label="Suscribirse al boletín de noticias")

    # Comentarios adicionales
    txt_comentarios = ft.TextField(label="Comentarios adicionales:", multiline=True, min_lines=3, max_lines=5, width=450)

    # Función para mostrar notificaciones con SnackBar compatible
    def mostrar_mensaje(texto):
        page.snack_bar = ft.SnackBar(ft.Text(texto))
        page.snack_bar.open = True
        page.update()

    # Lógica de registro
    def realizar_registro(e):
        if not chk_terminos.value:
            mostrar_mensaje("Debes aceptar los términos y condiciones.")
            return
        
        nombre = txt_nombre.value.strip() if txt_nombre.value else ""
        if not nombre:
            mostrar_mensaje("El campo de nombre es obligatorio.")
            return

        mostrar_mensaje(f"¡Usuario {nombre} registrado correctamente!")

    # Lógica de limpieza
    def limpiar_campos(e):
        txt_nombre.value = ""
        txt_email.value = ""
        txt_password.value = ""
        txt_comentarios.value = ""
        chk_terminos.value = False
        chk_newsletter.value = False
        rb_genero.value = None
        cmb_pais.value = "Bolivia"
        page.update()

    # Botones
    btn_guardar = ft.Button(content="Registrar", on_click=realizar_registro)
    btn_limpiar = ft.Button(content="Limpiar", on_click=limpiar_campos)
    btn_row = ft.Row([btn_guardar, btn_limpiar], width=450)

    # Estructura principal en la página
    page.add(
        ft.Column([
            ft.Text("Formulario de Registro de Usuario", size=18, weight=ft.FontWeight.BOLD),
            txt_nombre,
            txt_email,
            txt_password,
            ft.Text("Género:"),
            rb_genero,
            cmb_pais,
            chk_terminos,
            chk_newsletter,
            txt_comentarios,
            ft.Container(height=10),
            btn_row
        ], 
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        spacing=12)
    )

if __name__ == "__main__":
    ft.run(main)