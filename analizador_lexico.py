from unicodedata import decimal
#from cv2 import cartToPolar
import re

class analizador_lexico():
    def __int__(self):
        #crear la cadena donde se guardan los tokens
        self.lista_tokens = []
        self.lista_errores = [] #se crea una cadena donde se guardan los errores
    def analizar(self, contenido):
        self.lista_tokens = []
        self.lista_errores = []
        #indicando que se finaliza el texto
        contenido += "$"
        #Contador 
        indice = 0
        #indicar linea o posicion del token
        linea = 1
        columna = 1
        buffer = ""
        buffer1= ""
        estado = "a"
        decimal = "false"
        
        #Recorrer cada caracter del contenido del texto
        #while indice < len(contenido):#longitud del texto
            #guardar caracter guardado
            #caracter = contenido(indice)
            #if estado == "a": #equivalencia
                #verificacion de signos
                #if caracter == "+" or caracter == "-" or caracter == "=" or caracter == "*" or caracter == "/" or caracter == "<" or caracter == ">" or caracter == ".": #tablas de verdad o se ejecuta una o es otra
                    #buffer = caracter
                    #columna += 1
                    #self.lista_tokens.append(token("OP", buffer, linea, columna))
                    #buffer = ""
                    #estado = "a"
                   
                    