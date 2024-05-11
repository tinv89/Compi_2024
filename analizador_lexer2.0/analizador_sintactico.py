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
        
        elif self.listatokens[self.contador].tipo=="PR" and self.listatokens[self.contador].lexema=="String":
            instru=self.declaracion_string()
            return instruccion(instru)
        elif self.listatokens[self.contador].tipo=="PR" and self.listatokens[self.contador].lexema=="char":
            instru=self.declaracion_char()
            return instruccion(instru)
        elif self.listatokens[self.contador].tipo=="PR" and self.listatokens[self.contador].lexema=="float":
            instru=self.declaracion_float()
            return instruccion(instru)
        elif self.listatokens[self.contador].tipo=="PR" and self.listatokens[self.contador].lexema=="System" and self.listatokens[self.contador+4].lexema=="println":
            instru=self.imprimir_consalto()
            return instruccion(instru)
        elif self.listatokens[self.contador].tipo=="PR" and self.listatokens[self.contador].lexema=="System" and self.listatokens[self.contador+4].lexema=="println":
            instru=self.declaracion_sinsalto()
            return instruccion(instru)
        else:
            self.contador+=1
            return error_sin(self.listaerroressin,self.listatokens[self.contador].linea,self.listatokens[self.contador].columna)
        
    def declaracion_entero(self):
        if self.listatokens[self.contador].tipo=="PR" and self.listatokens[self.contador].lexema=="int":
            self.contador+=1
            if self.listatokens[self.contador].tipo=="ID":
                id=self.listatokens[self.contador].lexema
                self.contador+=1
                if self.listatokens[self.contador].tipo=="OP" and self.listatokens[self.contador].lexema=="=":
                    self.contador+=1
                    if (self.listatokens[self.contador].tipo=="NUM" and self.listatokens[self.contador].tipo2==1) or self.listatokens[self.contador].tipo=="ID":
                        exp=self.valor()
                        print(isinstance(exp,int))
                        print(str(exp))
                        if self.listatokens[self.contador-1].lexema.isnumeric()==True:
                            if self.listatokens[self.contador].tipo=="DEL" and self.listatokens[self.contador].lexema==";":
                                self.contador+=1
                                return declaracion(id,exp) #expresion
                            else:
                                self.contador+=1
                                return error_sem(self.listaerroressin,self.listatokens[self.contador-1].linea,self.listatokens[self.contador-1].columna)                            
                        else:
                            self.contador+=1
                            return error_sem(self.listaerroressin,self.listatokens[self.contador-1].linea,self.listatokens[self.contador-1].columna)
        self.contador+=1
        return error_sin(self.listaerroressin,self.listatokens[self.contador-1].linea,self.listatokens[self.contador-1].columna)
    
    def declaracion_string(self):
        if self.listatokens[self.contador].tipo=="PR" and self.listatokens[self.contador].lexema=="String":
            self.contador+=1
            if self.listatokens[self.contador].tipo=="ID":
                id=self.listatokens[self.contador].lexema
                self.contador+=1
                if self.listatokens[self.contador].tipo=="OP" and self.listatokens[self.contador].lexema=="=":
                    self.contador+=1
                    if self.listatokens[self.contador].tipo=="CAD":
                        exp=self.valor()
                        if type(self.listatokens[self.contador-1].lexema.remplace('"',''))==str:
                            if self.listatokens[self.contador].tipo=="DEL" and self.listatokens[self.contador].lexema==";":
                                self.contador+=1
                                return declaracion(id,exp) #expresion
                            else:
                                self.contador+=1
                                return error_sin(self.listaerroressin,self.listatokens[self.contador-1].linea,self.listatokens[self.contador-1].columna)
                        else:
                            self.contador+=1
                            return error_sin(self.listaerroressin,self.listatokens[self.contador-1].linea,self.listatokens[self.contador-1].columna)
        self.contador+=1
        return error_sin(self.listaerroressin,self.listatokens[self.contador-1].linea,self.listatokens[self.contador-1].columna)
    
    def declaracion_char(self):
        if self.listatokens[self.contador].tipo=="PR" and self.listatokens[self.contador].lexema=="char":
            self.contador+=1
            if self.listatokens[self.contador].tipo=="ID":
                id=self.listatokens[self.contador].lexema
                self.contador+=1
                if self.listatokens[self.contador].tipo=="OP" and self.listatokens[self.contador].lexema=="=":
                    self.contador+=1
                    if self.listatokens[self.contador].tipo=="CAR":
                        exp=self.valor()
                        if len(self.listatokens[self.contador-1].lexema.remplace("'",""))==1:
                            if self.listatokens[self.contador].tipo=="DEL" and self.listatokens[self.contador].lexema==";":
                                self.contador+=1
                                return declaracion(id,exp)#expresion
                            else:
                                self.contador+=1
                                return error_sin(self.listaerroressin,self.listatokens[self.contador-1].linea,self.listatokens[self.contador-1].columna)
        self.contador+=1
        return error_sin(self.listaerroressin,self.listatokens[self.contador-1].linea,self.listatokens[self.contador].columna)
        
    def declaracion_float(self):
        if self.listatokens[self.contador].tipo=="PR" and self.listatokens[self.contador].lexema=="float":
            self.contador+=1
            if self.listatokens[self.contador].tipo=="ID":
                id=self.listatokens[self.contador].lexema
                self.contador+=1
                if self.listatokens[self.contador].tipo=="OP" and self.listatokens[self.contador].lexema=="=":
                    self.contador+=1
                    if self.listatokens[self.contador].tipo=="NUM" and self.listatokens[self.contador].tipo2==2:
                        exp=self.valor()
                        if isinstance(float(self.listatokens[self.contador-1].lexema),float)==True:
                            if self.listatokens[self.contador].tipo=="DEL" and self.listatokens[self.contador].lexema==";":
                                self.contador+=1
                                return declaracion(id,exp) #expresion
                            else:
                                self.contador+=1
                                return error_sem(self.listaerroressin,self.listatokens[self.contador-1].lista,self.listatokens[self.contador-1].columna)
                        else:
                            self.contador+=1
                            return error_sem(self.listaerroressin,self.listatokens[self.contador-1].linea,self.listatokens[self.contador-1].columna)
        self.contador+=1
        return error_sin(self.listaerroressin,self.listatokens[self.contador-1].linea,self.listatokens[self.contador-1].columna)
    
    def valor(self):
        if self.listatokens[self.contador].tipo=="CAD":
            self.contador+=1
            return expresion_literal("CAD", self.listatokens[self.contador-1].lexema)
        elif self.listatokens[self.contador].tipo=="NUM" and self.listatokens[self.contador].tipo2==1:
            self.contador+=1
            println(str(self.listatokens[self.contador-1].lexema))
            return expresion_literal("NUM", self.listatokens[self.contador-1].lexema)
        elif self.listatokens[self.contador].tipo=="ID":
            lex=self.listatokens[self.contador].lexema
            self.contador+=1
            return expresion_identificador(lex)
        elif self.listatokens[self.contador].tipo=="CAR":
            lex=self.listatokens[self.contador].lexema
            self.contador+=1
            return expresion_literal("CAR", self.listatokens[self.contador-1].lexema)
        elif self.listatokens[self.contador].tipo=="NUM" and self.listatokens[self.contador].tipo2==2:
            lex=self.listatokens[self.contador].lexema
            self.contador+=1
            return expresion_literal("DEC", self.listatokens[self.contador].lexema)
        else:
            self.contador+=1
            return error_sem(self.listaerroressin,self.listatokens[self.contador-1].linea,self.listatokens[self.contador-1].columna)
        
    
    def declaracion_consalto(self):
        if self.listatokens[self.contador].tipo=="PR" and self.listatokens[self.contador].lexema=="System":
            self.contador+=1
            if self.listatokens[self.contador].tipo=="OP" and self.listatokens[self.contador].lexema==".":
                self.contador+=1
                if self.listatokens[self.contador].tipo=="PR" and self.listatokens[self.contador].lexema=="out":
                    self.contador+=1
                    if self.listatokens[self.contador].tipo=="OP" and self.listatokens[self.contador].lexema==".":
                        self.contador+=1
                        if self.listatokens[self.contador].tipo=="PR" and self.listatokens[self.contador].lexema=="println":
                            self.contador+=1
                            if self.listatokens[self.contador].tipo=="DEL" and self.listatokens[self.contador].lexema=="(":
                                self.contador+=1
                                exp=self.valor()
                                if self.listatokens[self.contador].tipo=="DEL" and self.listatokens[self.contador].lexema==")":
                                    self.contador+=1
                                    if self.listatokens[self.contador].tipo=="DEL" and self.listatokens[self.contador].lexema==";":
                                        self.contador+=1
                                        return print(exp)
        return error_sin(self.listaerroressin,self.listatokens[self.contador-1].linea,self.listatokens[self.contador-1].columna)
        
    def declaracion_sinsalto(self):
        if self.listatokens[self.contador].tipo=="PR" and self.listatokens[self.contador].lexema=="System":
            self.contador+=1
            if self.listatokens[self.contador].tipo=="OP" and self.listatokens[self.contador].lexema==".":
                self.contador+=1
                if self.listatokens[self.contador].tipo=="PR" and self.listatokens[self.contador].lexema=="out":
                    self.contador+=1
                    if self.listatokens[self.contador].tipo=="OP" and self.listatokens[self.contador].lexema==".":
                        self.contador+=1
                        if self.listatokens[self.contador].tipo=="PR" and self.listatokens[self.contador].lexema=="print":
                            self.contador+=1
                            if self.listatokens[self.contador].tipo=="DEL" and self.listatokens[self.contador].lexema=="(":
                                self.contador+=1
                                exp=self.valor()
                                if self.listatokens[self.contador].tipo=="DEL" and self.listatokens[self.contador].lexema==")":
                                    self.contador+=1
                                    if self.listatokens[self.contador].tipo=="DEL" and self.listatokens[self.contador].lexema==";":
                                        self.contador+=1
                                        return printsn(exp)
        return error_sin(self.listaerroressin,self.listatokens[self.contador-1].linea,self.listatokens[self.contador-1].columna)        
        
                   
        
                        
                                
                                                  
                                    