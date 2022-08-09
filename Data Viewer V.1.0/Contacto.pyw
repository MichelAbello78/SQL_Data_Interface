from cProfile import label
from tkinter import *
from tkinter.tix import COLUMN
from turtle import title, width
from plyer import notification

raiz=Tk()

raiz.title("Single Registration")
raiz.iconbitmap("Data Viewer - Box/DataConfig.ico")
raiz.config(bg="white")
raiz.geometry("450x350")

cuadro=Frame(raiz)
cuadro.pack()

#TITLE
title_nombre=Label(cuadro, text="Registro de Datos")
title_nombre.grid(row=0, column=2, padx=10, pady=10)


#FORM TEXT
label_nombre=Label(cuadro, text="Nombres:")
label_nombre.grid(row=1, column=1, padx=10, pady=10, sticky="e")

label_apellido=Label(cuadro, text="Apellidos:")
label_apellido.grid(row=2, column=1, padx=10, pady=10, sticky="e")

label_UES=Label(cuadro, text="Negocio:")
label_UES.grid(row=3, column=1, padx=10, pady=10, sticky="e")

label_producto=Label(cuadro, text="Producto:")
label_producto.grid(row=4, column=1, padx=10, pady=10, sticky="e")

label_valor=Label(cuadro, text="Valor:")
label_valor.grid(row=5, column=1, padx=10, pady=10, sticky="e")

label_NumTransacciones=Label(cuadro, text="# Transacciones:")
label_NumTransacciones.grid(row=6, column=1, padx=10, pady=10, sticky="e")

#FORM TABLE
cuadro_nombre=Entry(cuadro, width=50)
cuadro_nombre.grid(row=1, column=2, padx=10, pady=10)

cuadro_apellido=Entry(cuadro, width=50)
cuadro_apellido.grid(row=2, column=2, padx=10, pady=10)

cuadro_UES=Entry(cuadro, width=50)
cuadro_UES.grid(row=3, column=2,padx=10, pady=10)

cuadro_producto=Entry(cuadro, width=50)
cuadro_producto.grid(row=4, column=2, padx=10, pady=10)

cuadro_valor=Entry(cuadro, width=50)
cuadro_valor.grid(row=5, column=2, padx=10, pady=10)

cuadro_NumTransacciones=Entry(cuadro, width=50)
cuadro_NumTransacciones.grid(row=6, column=2, padx=10, pady=10)

#BOTTOM
def Registro():
    notification.notify(
    title='Single Registration',
    message='Dato ingreso con exito',
    app_icon='Data Viewer - Box/Data+.ico',
    timeout = 20)

boton_nombre=Button(cuadro, text="Registrar", width=20, command=Registro)
boton_nombre.grid(row=7, column=2, padx=10, pady=10)

raiz.mainloop()