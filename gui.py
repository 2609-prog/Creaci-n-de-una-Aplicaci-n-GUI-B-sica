
import tkinter as tk
from tkinter import messagebox

# Funcion para agregar elementos a la lista
def agregar():
    dato = entrada.get() # Obtiene el texto del campo 
    if dato.strip() == "":# Validar si esta vacio
        messagebox.showwarning("Atención", "No puedes agregar un campo vacío.")

    else:
        lista.insert(tk.END, dato) # Inserta al final de la lista
        entrada.delete(0, tk.END)# Limpia el campo de texto

# Función para limpiar la seleccion de toda la lista
def limpiar():
    seleccion = lista.curselection()
    if seleccion: # Si hay un item seleccionado
        lista.delete(seleccion)
    
    else: # Si no hay seleccion, limpiar toda la lista 
        lista.delete(0, tk.END)

# Crear una ventana principla
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica - Lista de Datos")
ventana.geometry("400x300")
ventana.config(bg="#f0f0f0")

# Etiqueta
label = tk.Label(ventana, text="Ingrese un dato:", font=("Arial", 12), bg="#f0f0f0")
label.pack(pady=5)

# Campo de texto
entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=5)

# Botones
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
boton_agregar.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar, bg="#f44336", fg="white", font=("Arial", 10, "bold"))
boton_limpiar.pack(pady=5)

# Lista para mostrar datos
lista = tk.Listbox(ventana, font=("Arial", 12), width=40, height=8)
lista.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()

