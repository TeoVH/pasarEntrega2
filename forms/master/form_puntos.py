import tkinter as tk
from config import  COLOR_CUERPO_PRINCIPAL


class FormularioPuntosDesign():

    def __init__(self, panel_principal):

        # Crear paneles: barra superior
        self.barra_superior = tk.Frame( panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False) 

        # Crear paneles: barra inferior
        self.barra_inferior = tk.Frame( panel_principal)
        self.barra_inferior.pack(side=tk.BOTTOM, fill='both', expand=True)  

        # Primer Label con texto
        self.labelTitulo = tk.Label(
            self.barra_superior, text="Empresas de recolección")
        self.labelTitulo.config(fg="#222d33", font=("Roboto", 30), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)

        # Segundo Label con la información de las empresas en forma de lista
        empresas_info = [
            "Ecogras\nDirección: Cl. 37b, Germania, Itagüi, Antioquia\nTeléfono: 301 3639730",
            "Empresa 2\nDirección: Direccion2\nTeléfono: Tel2\nCorreo: correo2@example.com",
            "Empresa 3\nDirección: Direccion3\nTeléfono: Tel3\nCorreo: correo3@example.com",
            "Empresa 4\nDirección: Direccion4\nTeléfono: Tel4\nCorreo: correo4@example.com",
        ]

        padding_between_lines = 10
        empresas_text_with_padding = "\n\n".join(
            [line + " " * padding_between_lines for line in empresas_info])

        self.labelEmpresas = tk.Label(
            self.barra_inferior, text=empresas_text_with_padding, justify=tk.CENTER)
        self.labelEmpresas.config(fg="#000000", font=("Arial", 12), pady=10, bg=COLOR_CUERPO_PRINCIPAL)
        self.labelEmpresas.pack(side=tk.TOP, fill='both', expand=True)