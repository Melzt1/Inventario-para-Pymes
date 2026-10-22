import tkinter as tk

# creamos el objeto de la clase Tkinter
ventana = tk.Tk()
ventana.title("Sistema PyME")
ventana.geometry("900x600")

etiqueta = tk.Label(ventana, text="Hola. Interfaz")
etiqueta.pack(pady=40)


def probando_command():
    etiqueta.config(text="HOLA, ESTOY EN DESARROLLO")

boton1 = tk.Button(ventana, text="Boton de test", command=probando_command)
boton1.pack(pady=40)

boton2 = tk.Button(ventana, text="Segundo boton", command=lambda:etiqueta.config(text="Hola. Interfaz"))
boton2.pack(pady=10)
# Abrir ventana
ventana.mainloop()