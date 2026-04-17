import tkinter as tk
from tkinter import messagebox
from operaciones import OperacionesMatematicas

ventana = tk.Tk()
ventana.title("Índice de Masa Corporal")
ventana.geometry("350x180")

# Labels y Entries
tk.Label(ventana, text="Peso (kg):", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
entrada_peso = tk.Entry(ventana, width=15)  # padre es 'ventana'
entrada_peso.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Altura (m):", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
entrada_altura = tk.Entry(ventana, width=15) 
entrada_altura.grid(row=1, column=1, padx=10, pady=10)

# Función del botón
def calcular():
    try:
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get())
        if altura > 3 :
             messagebox.showerror("Error", "Ingresa la altura en metros, ejemplo: 1.80")
             return
        oper = OperacionesMatematicas()
        resultado = oper.imc(peso, altura)
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Error", "Ingresa números válidos")

# Botón
tk.Button(ventana, text="Calcular", command=calcular, width=12).grid(row=2, column=0, columnspan=2, pady=15)

ventana.mainloop()