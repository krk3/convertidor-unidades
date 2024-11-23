import tkinter as tk
from tkinter import ttk

# Funciones de conversión
def convertir():
    valor = float(entry_value.get())
    tipo_conversion = combo_type.get()

    if tipo_conversion == "Longitud":
        if combo_from.get() == "Metros" and combo_to.get() == "Kilómetros":
            resultado = valor / 1000
        elif combo_from.get() == "Kilómetros" and combo_to.get() == "Metros":
            resultado = valor * 1000
        elif combo_from.get() == "Metros" and combo_to.get() == "Centímetros":
            resultado = valor * 100
        elif combo_from.get() == "Centímetros" and combo_to.get() == "Metros":
            resultado = valor / 100
        else:
            resultado = valor
    elif tipo_conversion == "Peso":
        if combo_from.get() == "Kilogramos" and combo_to.get() == "Gramos":
            resultado = valor * 1000
        elif combo_from.get() == "Gramos" and combo_to.get() == "Kilogramos":
            resultado = valor / 1000
        else:
            resultado = valor
    elif tipo_conversion == "Temperatura":
        if combo_from.get() == "Celsius" and combo_to.get() == "Fahrenheit":
            resultado = (valor * 9/5) + 32
        elif combo_from.get() == "Fahrenheit" and combo_to.get() == "Celsius":
            resultado = (valor - 32) * 5/9
        else:
            resultado = valor

    label_result.config(text=f"Resultado: {resultado}")

# Crear la ventana principal
root = tk.Tk()
root.title("Convertidor de Unidades")
root.geometry("400x400")
root.configure(bg="#f7f7f7")

# Título
title = tk.Label(root, text="Convertidor de Unidades", font=("Arial", 16, "bold"), bg="#f7f7f7")
title.pack(pady=20)

# Entrada de valor
entry_value = tk.Entry(root, font=("Arial", 14), bd=2, relief="solid")
entry_value.pack(pady=10)

# Selección de tipo de conversión
combo_type = ttk.Combobox(root, values=["Longitud", "Peso", "Temperatura"], font=("Arial", 12), state="readonly")
combo_type.set("Longitud")
combo_type.pack(pady=10)

# Selección de unidad de origen
combo_from = ttk.Combobox(root, values=["Metros", "Kilómetros", "Centímetros", "Kilogramos", "Gramos", "Celsius", "Fahrenheit"], font=("Arial", 12), state="readonly")
combo_from.set("Metros")
combo_from.pack(pady=10)

# Selección de unidad de destino
combo_to = ttk.Combobox(root, values=["Metros", "Kilómetros", "Centímetros", "Kilogramos", "Gramos", "Celsius", "Fahrenheit"], font=("Arial", 12), state="readonly")
combo_to.set("Kilómetros")
combo_to.pack(pady=10)

# Botón para convertir
convert_button = tk.Button(root, text="Convertir", font=("Arial", 12), bg="#28a745", fg="white", command=convertir)
convert_button.pack(pady=20)

# Etiqueta para mostrar el resultado
label_result = tk.Label(root, text="Resultado: ", font=("Arial", 14), bg="#f7f7f7")
label_result.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
