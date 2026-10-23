import tkinter as tk
from tkinter import ttk
from negocio.negocio_categoria import listar_categorias_activas

def cargar_categorias():
    datos = listar_categorias_activas()
    habilitado = "Habilitado"

    for fila in datos:
        treeview.insert("", tk.END, values=(
            fila.id_categoria, 
            fila.nombre, 
            fila.descripcion,
            habilitado
        ))

def refrescar_categorias():
    for item in treeview.get_children():
        treeview.delete(item)
    cargar_categorias()

# creamos el objeto de la clase Tkinter
ventana = tk.Tk()
ventana.title("Sistema PyME")
ventana.geometry("900x600")

sidebar = tk.Frame(ventana, bg="#0f172a", width=220)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

contenido = tk.Frame(ventana, bg="#f4f6fb")
contenido.pack(side="left", fill="both", expand=True)

tk.Label(
    sidebar,
    text="Sistema PyME",
    bg="#0f172a",
    fg="white",
    font=("Segoe UI", 14, "bold"),
).pack(anchor="w", padx=20, pady=(24, 20))

tk.Label(
    contenido,
    text="Categorias",
    bg="#f4f6fb",
    fg="#0f172a",
    font=("Segoe UI", 20, "bold"),
).pack(anchor="w", padx=20, pady=(24, 2))

etiqueta = tk.Label(
    contenido, 
    text="Clasificacion de los productos del inventario",
    bg="#f4f6fb",
    fg="#64748b",
    font=("Segoe UI", 11, "bold")
)
etiqueta.pack(anchor="w", padx=20, pady=(0, 20))

opciones = ["Panel", "Productos", "Categorias"]

for opcion in opciones:
    btn = tk.Button(
        sidebar,
        text=opcion,
        bg="#f4f6fb",
        fg="#0f172a",
        bd=0,
        pady=10,
        anchor="w",
        padx=15,
    )
    btn.pack(fill="x", pady=2, padx=5)

boton_refrescar = ttk.Button(contenido, text="Refrescar", command=refrescar_categorias)
boton_refrescar.pack(padx=40, pady=10)

columnas = ("id", "nombre", "descripcion", "estado")

# Crear un Frame contenedor para la treeview y el scrollbar
tabla_categorias = ttk.Frame(contenido)
tabla_categorias.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)

treeview = ttk.Treeview(tabla_categorias, columns=columnas, show="headings")

# encabezado
treeview.heading("id", text="ID")
treeview.heading("nombre", text="Nombre")
treeview.heading("descripcion", text="Descripcion")
treeview.heading("estado", text="Estado")

# configurar cada columna
treeview.column("id", width=60, anchor=tk.CENTER, stretch=False)
treeview.column("nombre", width=150, anchor=tk.W, stretch=False)
treeview.column("descripcion", width=250, anchor=tk.W)
treeview.column("estado", width=100, anchor=tk.CENTER, stretch=False)

# crear un scrollbar con orientacion vertical
scrollbar = ttk.Scrollbar(tabla_categorias, orient=tk.VERTICAL, command=treeview.yview)

# vincular el treeview al scrollbar
treeview.configure(yscrollcommand=scrollbar.set)

treeview.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


cargar_categorias()

# Abrir ventana
ventana.mainloop()
