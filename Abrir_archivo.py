import tkinter as abrir
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext as st
from tkinter import Scrollbar as sd
import sys 
from tkinter import filedialog as fd 
import re as r 

#Primera Clase Creando Funciones 
class Aplicacion: 
    ventana = abrir.Tk()
    tokens = []
    
    #Primera funcion
    def __init__(self): 
        self.agregar_menu() #self llama algo existente en la clase funcion o metodo
        self.scrolledtext1 = st.ScrolledText(self.ventana, width = 60, height = 25) #Definiendo el alto y ancho de la ventana
        self.scrolledtext1.grid(column = 0, row = 0, padx = 10, pady = 10)#definiendo las coordenadas de la ventada
        
        self.scrolledtext2 = st.ScrolledText(self.ventana, width = 60, height = 25)
        self.scrolledtext2.grid(column = 1, row = 0, padx = 10, pady = 10)
        
        self.scrolledtext3 = st.ScrolledText(self.ventana, width = 125, height = 10)
        self.scrolledtext3.grid(column = 0, row = 1, padx = 10, pady = 10, columnspan = 2)
        self.ventana.mainloop()
        
    def agregar_menu(self):
        menubar = abrir.Menu(self.ventana)
        self.ventana.config(menu = menubar)
        opciones1 = abrir.Menu(menubar, tearoff = 0)
        opciones1.add_command(label = "Abrir Archivo", command = self.abrir)
        menubar.add_cascade(label = "Archivo", menu = opciones1)
        menubar.add_command(label = "Compilar", command = self.compilar)
        menubar.add_command(label = "Tabla", command = self.ventanaTabla)
        
    def abrir(self):
        nombredoc = fd.askopenfilename(initialdir = "C:\Escritorio", title = "Seleccione Archivo", 
                                       filetypes = (("txt files", "*.txt"), ("Todos los Archivos", "*.*")))  
        if nombredoc !='':#Verifica si se selecciono un archivo
            archi1 = open(nombredoc, "r", encoding = "utf-8") #Aperturando el archivo para su lectura y validación
            contenido = archi1.read()#Lectura del documento
            contenido1 = contenido.replace(' ','')#Se elimina cualquier espacio en blanco y junta todo
            print(contenido1)#imprimir el texto purificado
            archi1.close()
            self.scrolledtext1.delete("1.0", abrir.END)#Se borra todo el texto que quedo en el scrolltext1 que esta asociado al a clase 
            self.scrolledtext1.insert("1.0", contenido)
            
            
    def compilar(self):
        #set_salida("")
        cadena = self.scrolledtext1.get("1.0", abrir.END)#get envio y recepción toma lo que encontro en columna 1 fila 0        
              
    
    def ventanaTabla(self): # Se dibuja la tabla
        self.ventana.deiconify()
        win = abrir.Toplevel()
        win.geometry('900x250')
        win.configure(bg = '#58B2E5')
        #Para no modificar el tamaño de la ventana
        win.resizable(0,0)
        
        tv = ttk.Treeview(win)
        tv = ttk.Treeview(win, columns= ("tipo", "valor_ini", "alcance")) #Ventana de la tabla de simbolos
        tv.pack(side = abrir.TOP)
        
        #Se traen los parametros con los que se llenara la tabla 
        tv.column("#0", width = 200)
        tv.column("tipo", width = 200, anchor = CENTER)
        tv.column("valor_ini", width = 200, anchor = CENTER)
        tv.column("alcance", width = 200, anchor = CENTER)
        
        #Titulos de columnas
        tv.heading("#0", text = "Nombre Identificador", anchor = CENTER)
        tv.heading("tipo", text = "Tipo", anchor = CENTER)
        tv.heading("valor_ini", text = "Valor Inicial", anchor = CENTER)
        tv.heading("alcance", text = "Alcance", anchor = CENTER)
        
        
Aplicacion1 = Aplicacion()        