#para identificar si es un arreglo si es una cadena un entero
class expresion_literal:
    def __init__(self, tipo, valor):
        self.tipo=tipo
        self.valor=valor


    def get_Valor(self,entorno):
        #obtiene la cadena sin comillas
        if self.tipo=="CAD":
            return self.valor.replace('"', '')
        #obtiene numero entero   
        elif self.tipo=="NUM":
            return int(self.valor)
        #obtiene caracter sin comillas
        elif self.tipo=="CAR":
            return self.valor.replace("'","")
        #obtiene numero decimal
        elif self.tipo=="DEC":
            return float(self.valor)
    
class expresion_identificador:
    def __init__(self,id):
        self.id=id
    #para retornar el valor del identificador
    def get_Valor(self,entorno):
        return entorno.get(self.id)
