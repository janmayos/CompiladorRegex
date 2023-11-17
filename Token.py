class Token:

    def __init__(self, tipo, lexema,literal,linea):
        self.tipo = tipo #TipoToken 
        self.lexema = lexema #String
        self.literal = literal#Object
        self.linea = linea#int


    def set_token_oftoken(self,token2):
        self.tipo = token2.get_tipo()
        self.lexema = token2.get_lexema()
        self.literal = token2.get_literal()
        self.linea = token2.get_linea()
    
    def get_tipo(self):
        return self.tipo
    
    def get_lexema(self):
        return self.lexema
    
    def get_literal(self):
        return self.literal
    
    def get_linea(self):
        return self.linea
    
    def set_tipo(self,tipo):
        self.tipo = tipo

    def set_lexema(self,lexema):
        self.lexema = lexema

    def set_literal(self,literal):
        self.literal = literal

    def set_linea(self,linea):
        self.linea = linea

    def limpiar_token(self):    
        self.tipo = None #TipoToken 
        self.lexema = None#String
        self.literal = None#Object
        self.linea = None#int
    
    def get_info(self):
        return "Tipo: "+str(self.tipo) +" Lexema: "+str(self.lexema) + " Literal: "+str(self.literal) + " Linea: "+ str(self.linea)