from unicodedata import decimal
#from cv2 import cartToPolar
from clases import token, error
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
        while indice < len(contenido):#longitud del texto
            #guardar caracter evaluado
            caracter = contenido(indice)
            if estado == "a": #equivalencia
                #verificacion de signos
                if caracter == "+" or caracter == "-" or caracter == "=" or caracter == "*" or caracter == "/" or caracter == "<" or caracter == ">" or caracter == ".": #tablas de verdad o se ejecuta una o es otra
                    buffer = caracter
                    columna += 1
                    self.lista_tokens.append(token("OP", buffer, linea, columna))
                    buffer = ""
                    estado = "a"
                elif caracter==";" or caracter=="," or caracter=="(" or caracter==")" or caracter=="[" or caracter=="]" or caracter=="{" or caracter=="}" or caracter==":":
                    buffer=caracter
                    columna+=1
                    self.lista_tokens.append(token("DEL",buffer,linea,columna))
                    buffer=""
                    estado="a"
                    #evalua si existe un salto de linea lo omite
                elif caracter=="\n":
                    columna=1
                    linea+=1
                elif caracter=="\t":
                    columna+=1
                elif caracter==" ":
                    columna+=1
                    #para verificar si es una letra
                elif re.search('[a-zA-Z]', caracter) or caracter == '_':
                    buffer=caracter
                    columna+=1
                    estado="b"
                elif caracter.isdigit():
                    buffer=caracter
                    buffer1=caracter
                    columna+=1
                    estado="c"
                elif caracter=='"':
                    buffer=caracter
                    columna+=1
                    estado="d"
                elif caracter=="'":
                    buffer=caracter
                    columna+=1
                    for i in range(32,256):
                        #para ver si es un caracter
                        if str(contenido[indice+1])==str(chr(i)):
                            buffer+=contenido[indice+1]
                            columna+=1
                            if contenido[indice+2]=="'":
                                buffer+=contenido[indice+2]
                                columna+=1
                                self.lista_tokens.append(token("CAR", buffer,linea,columna))
                                buffer=""
                                estado="a"
                                indice+=2
                            else:
                                self.lista_errores.append(error("ERROR",buffer,linea,columna))
                                buffer=""
                                estado="a"
                                indice+=2  
                    buffer=""
                    estado="a"
                elif caracter=="$":
                    buffer=caracter
                    columna+=1
                    self.lista_tokens.append(token("EOF",buffer,linea,columna))
                    buffer=""
                    estado="a"
                    print("Analisis Lexico hecho correctamente")
                else:
                    self.lista_errores.append(error(caracter,"ERROR",linea,columna))
                    buffer=""
                    columna+=1
            elif estado=="b":
                #verficamos palabras reservadas
                if re.search('[a-zA-Z]', caracter) or caracter == '_' or re.search('\d', caracter):
                    buffer+=caracter
                    columna+=1
                    estado="b"
                else:
                    reservadas = ['assert', 'bool', 'break', 'case', 'catch', 'char', 'class', 'continue', 'default', 'do', 'double', 'else', 'enum', 'extends', 
                        'false', 'finally', 'float', 'for', 'if', 'implements', 'import', 'instanceof', 'int', 'interface', 'main', 'new', 'null', 'out',
                        'package', 'private', 'protected', 'public', 'return', 'static', 'String', 'System','switch', 'this', 'throw', 'throws', 'true', 'try', 
                        'var', 'void', 'while', 'boolean', 'extends', 'print', 'println', 'include'] 
                    val=0
                    for reser in reservadas:
                        if buffer==reser:
                            self.lista_tokens.append(token("PR",buffer,linea,columna)) 
                            #se coloca uno para indicar que si es una palabra reservada
                            val=1
                    if val==0:
                        self.lista_tokens.append(token("ID",buffer,linea,columna))
                
                    buffer=""
                    estado="a"
                    #regresar al estado
                    indice-=1        
            elif estado=="c":
                #verifica si es digito
                if caracter.isdigit():
                    #buffer para entero
                    buffer+=caracter
                    #buffer para decimal
                    buffer1+=caracter
                    columna+=1
                    estado="c"
                elif caracter==".":
                    decimal=True
                    buffer1+=caracter
                    columna+=1
                    estado="c"
                else: 
                    if decimal==False:
                        nuevo=token("NUM",buffer,linea,columna)
                        #indica que es entero
                        nuevo.tipo2=1
                        self.lista_tokens.append(nuevo)
                    else: 
                        nuevo=token("NUM",buffer1,linea,columna)
                        #indica que es decimal
                        nuevo.tipo2=2
                        self.lista_tokens.append(nuevo)
                    buffer=""
                    indice-=1
                    estado="a"
                    
            elif estado=="d":
                if caracter=='"':
                    buffer+=caracter
                    columna+=1
                    self.lista_tokens.append(token("CAD",buffer,linea,columna))
                    buffer=""
                    estado="a"
                elif caracter=="\n":
                    columna=1
                    linea+=1
                    #si termina con ' pero inicia con "
                elif caracter=="'":
                    buffer+=caracter
                    columna+=1
                    self.lista_errores.append(error(buffer,"ERROR",linea,columna))
                    buffer=""
                    estado="a"
                else:
                    buffer+=caracter
                    columna+=1
                    estado="d"
           
            #para que recorra caracter es su indice
            indice+=1
              
                    
                    