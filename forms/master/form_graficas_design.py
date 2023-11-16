import tkinter as tk
import util.generic as utl
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FormularioGraficasDesign():

    def __init__(self, panel_principal):
        # Crear un subgráfico usando Matplotlib
        figura = Figure(figsize=(8, 6), dpi=100)
        ax1 = figura.add_subplot(211)               
        
        # Ajustar la distribución para agregar espacio de separación en el eje Y
        figura.subplots_adjust(hspace=0.4)

        # Graficar en el subgráfico
        self.grafico1(ax1)

        # Agregar subgrafico a la ventana de Tkinter
        canvas = FigureCanvasTkAgg(figura, master=panel_principal)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def grafico1(self, ax):
        # Función para graficar el primer conjunto de datos como un gráfico de barras
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]

        # Cambiar a un gráfico de barras
        ax.bar(x, y, label='Gráfico 1', color='blue', alpha=0.7)

        # Personalizar el aspecto del gráfico
        ax.set_title('ACEITE RECICLADO POR DIA')
        ax.set_xlabel('Dia')
        ax.set_ylabel('Cantidad')
        ax.legend()

        # Añadir etiquetas a cada barra
        for i, v in enumerate(y):
            ax.text(x[i] - 0.1, v + 0.1, str(v), color='black')

        # Añadir cuadrícula
        ax.grid(axis='y', linestyle='--', alpha=0.7)
