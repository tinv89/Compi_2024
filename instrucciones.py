#sirve para ejecutar instrucciones
from turtle import update
from expresiones import *
from clases import error
salida=""
#inicio intrucciones e intrucciones2 e intruccion sirven para recursividad del analizador
class inicio():
    def __init__(self, instrucciones):
        self.instrucciones=instrucciones
    def ejecutar(self,entorno):
        self.instrucciones.ejecutar(entorno)

class instrucciones():
    def __init__(self, instruccion,instrucciones2):
            self.instruccion=instruccion
            self.instrucciones2=instrucciones2
    def ejecutar(self,entorno):
        self.instruccion.ejecutar(entorno)
        self.instrucciones2.ejecutar(entorno)


class instrucciones2():
    def __init__(self, instruccion,instrucciones2):
            self.instruccion=instruccion
            self.instrucciones2=instrucciones2
    def ejecutar(self,entorno):
        if self.instruccion and self.instrucciones2:
            self.instruccion.ejecutar(entorno)
            self.instrucciones2.ejecutar(entorno)
            
class instruccion():
    def __init__(self, instruccion):
        self.instruccion=instruccion
    def ejecutar(self,entorno):
        self.instruccion.ejecutar(entorno)
#guardar el nombre de la variable y el valor de la variable en un diccionario 
class declaracion():
    def __init__(self,id,exp):
        self.id=id
        self.exp=exp
    def ejecutar(self,entorno):
        valor=self.exp.get_Valor(entorno)
        entorno.update({self.id:valor})
#error sin y error sem errores 
class error_sin():
    def __init__(self,listaerror,linea,columna):
        self.listaerror=listaerror
        self.linea=linea
        self.columna=columna

    def ejecutar(self,entorno):
       self.listaerror.append(error("","Error Sintactico",self.linea, self.columna))

class error_sem():
    def __init__(self,listaerror,linea,columna):
        self.listaerror=listaerror
        self.linea=linea
        self.columna=columna

    def ejecutar(self,entorno):
       self.listaerror.append(error("","Error Semantico",self.linea, self.columna))
#ejecutar la instruccion para imprimir el salto de linea 
class println():
    def __init__(self,exp):
        self.exp=exp

    def ejecutar(self,entorno):
        global salida
        valor=self.exp.get_Valor(entorno)
        salida+=str(valor)+"\n"
#para retornar el texto que se va imprimir de salida
def ob_salida():
    global salida
    return salida
    #para vaciar la salida
def set_salida(txt):
    global salida
    salida=txt
#ejecutar la instruccion para imprimir sin el salto de linea
class printsn():
    def __init__(self,exp):
        self.exp=exp

    def ejecutar(self,entorno):
        global salida
        valor=self.exp.get_Valor(entorno)
        salida+=str(valor)
