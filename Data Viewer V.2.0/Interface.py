from cProfile import label
from cgi import test
from distutils.cmd import Command
from hashlib import new
from importlib.util import set_loader
from select import select
from sre_parse import State
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ventana import *
import pymysql
from Connection import *

class ventana(Frame):

    conexiones=Connection()

    def __init__(self, master=None):
        super().__init__(master,width=1300,height=400)
        self.master = master
        self.pack()
        self.create_widgets()
        self.Dataview()
        self.HabilitarBox("disabled")
        self.HabilitarBotones("normal")
        self.HabilitarGuardar_Elminar("disabled")
        self.Id=-1

    def Dataview(self):
        Data=self.conexiones.consulta_dato()
        for row in Data:
            self.grid.insert("",END,text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6]))
        if len(self.grid.get_children()) >0:
            self.grid.selection_set(self.grid.get_children()[0])

    def HabilitarBox(self, estado):
        self.Id_box.configure(state=estado)
        self.fecha_box.configure(state=estado)
        self.valor_box.configure(state=estado)
        self.Num_box.configure(state=estado)
        self.UES_box.configure(state=estado)
        self.Producto_box.configure(state=estado)

    def LimpiarBox(self):
        self.Id_box.delete(0,END)
        self.fecha_box.delete(0,END)
        self.valor_box.delete(0,END)
        self.Num_box.delete(0,END)
        self.UES_box.delete(0,END)
        self.Producto_box.delete(0,END)

    def HabilitarBotones(self, estado):
        self.NuevoBoton.configure(state=estado)
        self.ModificarBoton.configure(state=estado)
        self.EliminarBoton.configure(state=estado)
        self.ImportarBoton.configure(state=estado)
        self.ExportarBoton.configure(state=estado)

    def HabilitarGuardar_Elminar(self, estado):
        self.GuardarBoton.configure(state=estado)
        self.CancelarBoton.configure(state=estado)

    def NBotton(self):
        self.HabilitarBox("normal")
        self.HabilitarBotones("disabled")
        self.HabilitarGuardar_Elminar("normal")
        self.LimpiarBox()
        self.Id_box.focus()

    def MBotton(self):
        seleccion=self.grid.focus()
        clave=self.grid.item(seleccion, 'text')

        if clave =='':
            messagebox.showwarning("Modificar",'Debes selecionar un elemento')
        else:
            self.Id=clave
            self.HabilitarBox("normal")
            valores=self.grid.item(seleccion,'values')
            self.LimpiarBox()
            self.HabilitarGuardar_Elminar("normal")
            self.HabilitarBotones("disabled")
            self.Id_box.focus()
            self.Id_box.insert(0,valores[0])
            self.fecha_box.insert(0,valores[1])
            self.valor_box.insert(0,valores[2])
            self.Num_box.insert(0,valores[3])
            self.UES_box.insert(0,valores[4])
            self.Producto_box.insert(0,valores[5])
            self.Producto_box.insert(0,valores[6])
        

    def EBotton(self):
        seleccion=self.grid.focus()
        clave=self.grid.item(seleccion,'text')

        if clave =='':
            messagebox.showwarning("Eliminar",'Debes selecionar un elemento')
        
        else:
            valores=self.grid.item(seleccion,'values')
            datos=str(clave)+ ","+valores[0]+","+valores[1]+","+valores[2]+","+valores[3]+","+valores[4]+","+valores[5]
            respuesta=messagebox.askquestion("Eliminar","Deseas elimiar el registro seleccionado?\n"+datos)

            if respuesta == messagebox.YES:
                n=self.conexiones.eliminar_dato(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar",'Elementos Elminados Correctamente')
                    self.LimpiarGuardado()
                    self.Dataview()
                else:
                    messagebox.showwarning("Eliminar",'No fueron eliminado los elementos')

    def GBotton(self):
        if self.Id == -1:
            self.conexiones.insertar_dato(self.Id_box.get(),self.fecha_box.get(),self.valor_box.get(),self.Num_box.get(),self.UES_box.get(),self.Producto_box.get())
            messagebox.showinfo("Insertar",'Elemento insertado correctamente')
        else:
            self.conexiones.modificar_dato(self.Id,self.Id_box.get(),self.fecha_box.get(),self.valor_box.get(),self.Num_box.get(),self.UES_box.get(),self.Producto_box.get())
            messagebox.showinfo("Modificar", "Elemento insertado correctamente")
            self.Id = -1
        self.Dataview()
        self.LimpiarGuardado()
        self.LimpiarBox()
        self.HabilitarGuardar_Elminar("disabled")
        self.HabilitarBotones("normal")
        self.HabilitarBox("disabled")

    def LimpiarGuardado(self):
        for item in self.grid.get_children():
            self.grid.delete(item)

    def CBotton(self):
        cancelar=messagebox.askquestion("Cancealr",'Esta seguro que quiere cancelar la operacion')
        if cancelar == messagebox.YES:
            self.LimpiarBox()
        self.HabilitarGuardar_Elminar("disabled")
        self.HabilitarBotones("normal")
        self.HabilitarBox("disabled")

    def IBotton(self):
        pass

    def ExBotton(self):
        pass

    def create_widgets(self):
        frame1= Frame(self, bg="#EBEFF3")
        frame1.place(x=0,y=0,width=100,height=400)

        self.NuevoBoton=Button(frame1, text="Nuevo",command=self.NBotton,bg="#E6C11B",fg="black")
        self.NuevoBoton.place(x=5,y=50,width=80,height=30,)

        self.ModificarBoton=Button(frame1, text="Modificar",command=self.MBotton,bg="#E6C11B",fg="black")
        self.ModificarBoton.place(x=5,y=90,width=80,height=30)

        self.EliminarBoton=Button(frame1, text="Eliminar",command=self.EBotton,bg="#E6C11B",fg="black")
        self.EliminarBoton.place(x=5,y=130,width=80,height=30)

        self.ImportarBoton=Button(frame1, text="Importar",command=self.IBotton,bg="#E6C11B",fg="black")
        self.ImportarBoton.place(x=5,y=170,width=80,height=30)

        self.ExportarBoton=Button(frame1, text="Exportar",command=self.ExBotton,bg="#E6C11B",fg="black")
        self.ExportarBoton.place(x=5,y=210,width=80,height=30)

        frame2= Frame(self, bg="#0F5AAB")
        frame2.place(x=101,y=0,width=200,height=400)

        Id_txt=Label(frame2,text="Identificacion:",fg="white",bg="#0F5AAB")
        Id_txt.place(x=3,y=5)
        self.Id_box=Entry(frame2)
        self.Id_box.place(x=3,y=25,width=190,height=20)

        fecha_txt=Label(frame2,text="Fecha de Transacción:",fg="white",bg="#0F5AAB")
        fecha_txt.place(x=3,y=55)
        self.fecha_box=Entry(frame2)
        self.fecha_box.place(x=3,y=75,width=190,height=20)

        valor_txt=Label(frame2,text="Valor de Transacción:",fg="white",bg="#0F5AAB")
        valor_txt.place(x=3,y=105)
        self.valor_box=Entry(frame2)
        self.valor_box.place(x=3,y=125,width=190,height=20)
        
        Num_txt=Label(frame2,text="Cantidad de Productos:", fg="white", bg="#0F5AAB")
        Num_txt.place(x=3,y=155)
        self.Num_box=Entry(frame2)
        self.Num_box.place(x=3,y=175,width=190,height=20)

        UES_txt=Label(frame2,text="UES:", fg="white", bg="#0F5AAB")
        UES_txt.place(x=3,y=205)
        self.UES_box=Entry(frame2)
        self.UES_box.place(x=3,y=225,width=190,height=20)

        Producto_txt=Label(frame2,text="Producto:", fg="white", bg="#0F5AAB")
        Producto_txt.place(x=3,y=255)
        self.Producto_box=Entry(frame2)
        self.Producto_box.place(x=3,y=275,width=190,height=20)

        self.GuardarBoton=Button(frame2,text="Guardar",command=self.GBotton,bg="white",fg="#0F5AAB")
        self.GuardarBoton.place(x=30,y=325,width=60,height=30)

        self.CancelarBoton=Button(frame2,text="Cancelar",command=self.CBotton,bg="white",fg="#AB0F0F")
        self.CancelarBoton.place(x=110,y=325,width=60,height=30)

        self.grid=ttk.Treeview(self,columns=("col1","col2","col3","col4","col5","col6"))

        self.grid.column("#0",width=50, anchor=CENTER)
        self.grid.column("col1",width=60,anchor=CENTER)
        self.grid.column("col2",width=60,anchor=CENTER)
        self.grid.column("col3",width=90, anchor=CENTER)
        self.grid.column("col4",width=90, anchor=CENTER)
        self.grid.column("col5",width=90, anchor=CENTER)
        self.grid.column("col6",width=90, anchor=CENTER)

        self.grid.heading("#0",text="Id")
        self.grid.heading("col1",text="Identificacion",anchor=CENTER)
        self.grid.heading("col2",text="Fecha de Transacción",anchor=CENTER)
        self.grid.heading("col3",text="Valor de Transacción", anchor=CENTER)
        self.grid.heading("col4",text="Cantidad de Productos", anchor=CENTER)
        self.grid.heading("col5",text="UES", anchor=CENTER)
        self.grid.heading("col6",text="Producto", anchor=CENTER)

        self.grid.place(x=300,y=0,width=1000,height=400)

 

