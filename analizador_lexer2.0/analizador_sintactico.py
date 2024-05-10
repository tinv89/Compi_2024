#analizador sintactico
from clases import error
from expresiones import *
from instrucciones import *

class analizador_sintactico:
    def __init__(self):
        self.listatokens=[]
        self.listaerroressin=[]
        self.contador=0
        
    def analizar(self,tokens):
        self.listatokens=tokens
        self.listaerroressin=[]
        entorno={} #Guarda la variable y darle valor
        empezar=self.inicio() #llama a la funcion inicio
        empezar.ejecutar(entorno)
        
    def inicio(self):
        instru=self.instrucciones()
        return inicio(instru)
    
    def instrucciones(self):
        instru=self.instruccion()
        instru2=self.instrucciones2()
        return instrucciones(instru,instru2)
    
    def instrucciones2(self):
        if self.listatokens[self.contador].tipo=="EOF":
            print("Analisis Sintactico realizado con exito")
            return instrucciones2(None,None)
        else:
            instru=self.instruccion()
            instru2=self.instrucciones2()
            return instrucciones2(instru,instru2)
        
    def instruccion(self):    
        print(self.listatokens[self.contador].tipo)
        print(self.listatokens[self.contador].lexema)
        if self.listatokens[self.contador].tipo=="PR" and self.listatokens[self.contador].lexema=='int':
            instru=self.declaracion_entero()
            return instruccion(instru)
        
        elif self.listatokens[self.contador].tipo=="PR" 