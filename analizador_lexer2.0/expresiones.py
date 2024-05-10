#identificar si es un arreglo o si es una cadena de enteros
class expresion_literal:
    def __init__(self,tipo,valor):
        self.tipo=tipo
        self.valor=valor
        
    def get_Valor(self,entorno):
            if self.tipo== "CADENA":
                return self.valor.replace('"', '')
            elif self.tipo=="NUMERO":
                return int(self.valor)
            elif self.tipo=="CARACTER":
                return self.valor.replace('"', '')
            elif self.tipo=="DECIMAL":
                return float(self.valor)
            
class expresion_identificador:
    def __init__(self,id):
        self.id=id
    def get_Valor(self,entorno):
        return entorno.get(self,id)
        
                    