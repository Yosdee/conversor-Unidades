import tkinter as tk
from tkinter import messagebox

# Tasa de conversion de USD a CRC  
tasaConversion = 514.21

# Funcion que lleva a cabo la conversion de CRC a USD
def convertirMOneda():
    """Función para convertir de USD a CRC."""
    try:
        montoUSD = float(entradaUSD.get())
        if montoUSD < 0:
              messagebox.showerror("Error", "Por favor, ingrese un valor numerico positivo.")
        else:
            montoCRC = montoUSD * tasaConversion
            etiquetaResultado.config(text=f"{montoUSD} USD = {montoCRC:.2f} CRC") 
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un valor numerico valido.")

# Función para limpiar los campos de entrada y salida.
def limpiarCampos():
    entradaUSD.delete(0, tk.END)
    etiquetaResultado.config(text="")

def cerrarAplicacion():
    """Función para confirmar el cierre de la aplicación."""
    respuesta = messagebox.askyesno("Salir", "¿Estas seguro de que deseas cerrar la aplicacion?")
    if respuesta:
        ventana.quit()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Moneda USD a CRC")
ventana.geometry("350x200")

# Manejar el cierre de la ventana con confirmación
ventana.protocol("WM_DELETE_WINDOW", cerrarAplicacion)

# Configurar las columnas para que el contenido quede centrado horizontalmente
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)

# Evitar que la fila superior se expanda
ventana.grid_rowconfigure(0, weight=0)
ventana.grid_rowconfigure(1, weight=0)
ventana.grid_rowconfigure(2, weight=0)  # La fila inferior se expandirá, empujando todo hacia arriba
ventana.grid_rowconfigure(3, weight=1)

# Entrada para monto en USD
etiquetaUSD = tk.Label(ventana, text="Monto en USD:")
etiquetaUSD.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entradaUSD = tk.Entry(ventana)
entradaUSD.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Botón para convertir de USD a CRC
botonConvertir = tk.Button(ventana, text="Convertir", command=convertirMOneda)
botonConvertir.grid(row=1, column=0, padx=10, pady=10, sticky="e")

# Botón para limpiar los campos
botonlimpiar = tk.Button(ventana, text="Limpiar", command=limpiarCampos)
botonlimpiar.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Etiqueta para mostrar el resultado
etiquetaResultado = tk.Label(ventana, text="", font=("Arial", 14), fg="blue")
etiquetaResultado.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Ejecutar la aplicación
ventana.mainloop()

