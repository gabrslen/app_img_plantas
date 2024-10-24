
import tkinter as tk
from tkinter import colorchooser

# Parâmetros ajustáveis
params = {
    'gradient_ksize': 3,  # Tamanho do kernel para cálculo do gradiente (ímpares entre 1-7)
    'threshold_value': 127,  # Valor de limiar para binarização (0-255)
    'markers_ksize': 3,  # Tamanho do kernel para cálculo dos marcadores (ímpares entre 3-11)
    'contour_thickness': 2,  # Espessura dos contornos (1-5 px)
    'epsilon': 0.01,  # Precisão dos contornos (0.001-0.1)
    'contour_color': (0, 255, 0),  # Cor dos contornos (formato RGB)
    'numero_clusters': 5,  # Quantidade de clusters para segmentação (2-10)
    'contraste': 1.5,  # Ajuste de contraste (0.5-3.0)
    'brilho': 20  # Ajuste de brilho (-100 a 100)
}

def ajustar_parametros():
    root = tk.Tk()
    root.title("Ajustar Parâmetros")

    def escolher_cor():
        cor = colorchooser.askcolor(title="Escolha a cor do contorno")[0]
        if cor:
            params['contour_color'] = tuple(int(c) for c in cor)
            
    
    def salvar_e_fechar():
        params['gradient_ksize'] = int(gradient_ksize_var.get())
        params['threshold_value'] = int(threshold_var.get())
        params['markers_ksize'] = int(markers_ksize_var.get())
        params['contour_thickness'] = int(contour_thickness_var.get())
        params['epsilon'] = float(epsilon_var.get())
        params['numero_clusters'] = int(numero_clusters_var.get())
        params['contraste'] = float(contraste_var.get())
        params['brilho'] = int(brilho_var.get())
        root.destroy()
        
    
    gradient_ksize_var = tk.StringVar(value=params['gradient_ksize'])
    threshold_var = tk.StringVar(value=params['threshold_value'])
    markers_ksize_var = tk.StringVar(value=params['markers_ksize'])
    contour_thickness_var = tk.StringVar(value=params['contour_thickness'])
    epsilon_var = tk.StringVar(value=params['epsilon'])
    numero_clusters_var = tk.StringVar(value=params['numero_clusters'])
    contraste_var = tk.StringVar(value=params['contraste'])
    brilho_var = tk.StringVar(value=params['brilho'])

    tk.Label(root, text="Gradient Kernel Size (1-7):").grid(row=0, column=0, sticky='w')
    gradient_ksize_spinbox = tk.Spinbox(root, from_=1, to=7, increment=2, textvariable=gradient_ksize_var, width=5)
    gradient_ksize_spinbox.grid(row=0, column=1)

    tk.Label(root, text="Threshold Value (0-255):").grid(row=1, column=0, sticky='w')
    threshold_spinbox = tk.Spinbox(root, from_=0, to=255, increment=1, textvariable=threshold_var, width=5)
    threshold_spinbox.grid(row=1, column=1)

    tk.Label(root, text="Markers Kernel Size (3-11):").grid(row=2, column=0, sticky='w')
    markers_ksize_spinbox = tk.Spinbox(root, from_=3, to=11, increment=2, textvariable=markers_ksize_var, width=5)
    markers_ksize_spinbox.grid(row=2, column=1)

    tk.Label(root, text="Contour Thickness (1-5 px):").grid(row=3, column=0, sticky='w')
    contour_thickness_spinbox = tk.Spinbox(root, from_=1, to=5, increment=1, textvariable=contour_thickness_var, width=5)
    contour_thickness_spinbox.grid(row=3, column=1)

    tk.Label(root, text="Epsilon (0.001-0.1):").grid(row=4, column=0, sticky='w')
    epsilon_spinbox = tk.Spinbox(root, from_=0.001, to=0.1, increment=0.001, textvariable=epsilon_var, width=5)
    epsilon_spinbox.grid(row=4, column=1)

    tk.Label(root, text="Número de Clusters (2-10):").grid(row=5, column=0, sticky='w')
    numero_clusters_spinbox = tk.Spinbox(root, from_=2, to=10, increment=1, textvariable=numero_clusters_var, width=5)
    numero_clusters_spinbox.grid(row=5, column=1)

    tk.Label(root, text="Contraste (0.5-3.0):").grid(row=6, column=0, sticky='w')
    contraste_spinbox = tk.Spinbox(root, from_=0.5, to=3.0, increment=0.1, textvariable=contraste_var, width=5)
    contraste_spinbox.grid(row=6, column=1)

    tk.Label(root, text="Brilho (-100 a 100):").grid(row=7, column=0, sticky='w')
    brilho_spinbox = tk.Spinbox(root, from_=-100, to=100, increment=1, textvariable=brilho_var, width=5)
    brilho_spinbox.grid(row=7, column=1)

    tk.Button(root, text="Escolher Cor do Contorno", command=escolher_cor).grid(row=8, column=0, columnspan=2)
    tk.Button(root, text="Salvar", command=salvar_e_fechar).grid(row=9, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    ajustar_parametros()
    print("Parâmetros ajustados:", params)
