import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class RegistroWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Registro - Versión CustomTkinter")
        self.geometry("500x650")
        self.minsize(500, 650)

        main_layout = ctk.CTkScrollableFrame(self, fg_color="transparent")
        main_layout.pack(fill="both", expand=True, padx=15, pady=15)

        lbl_titulo = ctk.CTkLabel(main_layout, text="Formulario de Registro de Usuario", font=ctk.CTkFont(size=16, weight="bold"))
        lbl_titulo.pack(anchor="w", pady=(0, 10))

        # Nombre
        ctk.CTkLabel(main_layout, text="Nombre completo:").pack(anchor="w", pady=(5, 0))
        self.txt_nombre = ctk.CTkEntry(main_layout, width=450)
        self.txt_nombre.pack(anchor="w", pady=(0, 5))

        # Email
        ctk.CTkLabel(main_layout, text="Correo electrónico:").pack(anchor="w", pady=(5, 0))
        self.txt_email = ctk.CTkEntry(main_layout, width=450)
        self.txt_email.pack(anchor="w", pady=(0, 5))

        # Password
        ctk.CTkLabel(main_layout, text="Contraseña:").pack(anchor="w", pady=(5, 0))
        self.txt_password = ctk.CTkEntry(main_layout, width=450, show="*")
        self.txt_password.pack(anchor="w", pady=(0, 10))

        # Género
        ctk.CTkLabel(main_layout, text="Género:").pack(anchor="w", pady=(5, 0))
        self.var_genero = ctk.StringVar(value="")
        gender_frame = ctk.CTkFrame(main_layout, fg_color="transparent")
        gender_frame.pack(anchor="w", pady=(0, 5))
        ctk.CTkRadioButton(gender_frame, text="Masculino", variable=self.var_genero, value="Masculino").pack(side="left", padx=(0, 15))
        ctk.CTkRadioButton(gender_frame, text="Femenino", variable=self.var_genero, value="Femenino").pack(side="left", padx=(0, 15))
        ctk.CTkRadioButton(gender_frame, text="Otro", variable=self.var_genero, value="Otro").pack(side="left")

        # País
        ctk.CTkLabel(main_layout, text="País:").pack(anchor="w", pady=(5, 0))
        self.cmb_pais = ctk.CTkComboBox(main_layout, values=["Bolivia", "Argentina", "Chile", "Colombia", "México", "España", "Otro"], width=450)
        self.cmb_pais.pack(anchor="w", pady=(0, 10))
        self.cmb_pais.set("Bolivia")

        # Checkboxes
        self.chk_terminos = ctk.CTkCheckBox(main_layout, text="Acepto los términos y condiciones")
        self.chk_terminos.pack(anchor="w", pady=5)
        self.chk_newsletter = ctk.CTkCheckBox(main_layout, text="Suscribirse al boletín de noticias")
        self.chk_newsletter.pack(anchor="w", pady=5)

        # Comentarios
        ctk.CTkLabel(main_layout, text="Comentarios adicionales:").pack(anchor="w", pady=(10, 0))
        self.txt_comentarios = ctk.CTkTextbox(main_layout, width=450, height=100)
        self.txt_comentarios.pack(anchor="w", pady=(0, 15))

        # Botones
        btn_frame = ctk.CTkFrame(main_layout, fg_color="transparent")
        btn_frame.pack(fill="x", pady=(5, 0))
        
        self.btn_guardar = ctk.CTkButton(btn_frame, text="Registrar", command=self.realizar_registro)
        self.btn_guardar.pack(side="left", expand=True, fill="x", padx=(0, 5))
        
        self.btn_limpiar = ctk.CTkButton(btn_frame, text="Limpiar", fg_color="gray", hover_color="darkgray", command=self.limpiar_campos)
        self.btn_limpiar.pack(side="right", expand=True, fill="x", padx=(5, 0))

    def realizar_registro(self):
        if not self.chk_terminos.get():
            messagebox.showwarning("Advertencia", "Debes aceptar los términos y condiciones.")
            return
        
        nombre = self.txt_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Advertencia", "El campo de nombre es obligatorio.")
            return

        messagebox.showinfo("Éxito", f"¡Usuario {nombre} registrado correctamente!")

    def limpiar_campos(self):
        self.txt_nombre.delete(0, "end")
        self.txt_email.delete(0, "end")
        self.txt_password.delete(0, "end")
        self.txt_comentarios.delete("1.0", "end")
        self.chk_terminos.deselect()
        self.chk_newsletter.deselect()
        self.var_genero.set("")
        self.cmb_pais.set("Bolivia")

if __name__ == "__main__":
    app = RegistroWindow()
    app.mainloop()