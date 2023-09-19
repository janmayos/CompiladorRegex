from enum import Enum


signos_puntuacion = {"<": "MENOR_QUE",
">": "MAYOR_QUE",
"=": "IGUAL",
".": "PUNTO",
"+": "MAS",
"-": "MENOS",
" ": "DELIM_ESPACIO",
"(": "PARENTESIS_ABRE",
")": "PARENTESIS_CIERRA",
"{": "LLAVE_ABRE",
"}": "LLAVE_CIERRA",
",": "COMA",
";": "PUNTO_COMA",
"*": "ASTERISCO",
"/": "DIAGONAL",
"!": "EXCLAMACION",
"_": "GUION_BAJO",
"'": "COMILLA_SIMPLE",
"\"" : "COMILLA_DOBLE",
"\n": "SALTO_LINEA",
"\\": "DIAGONAL_INVERTIDA",
":": "DOS_PUNTOS",
"&": "AMPERSON"}


class TipoVocabulario(Enum):
    # Crear un tipoToken por palabra reservada
    # Crear un tipoToken: identificador una cadena y numero
    NUMERO=1
    DIGITO=2
    DIGITO_FLOTANTE = 3
    DIGITO_EXPONENTE = 4
    LETRA = 5
    CADENA = 6
    IDENTIFICADOR = 7
    
    # Crear un tipoToken por cada "Signo del lenguaje" (ver clase Scanner)
    PUNTO = 8
    MENOS = 9 
    MAS = 10
    PARENTESIS_ABRE = 11
    PARENTESIS_CIERRA = 12
    LLAVE_CIERRA = 13
    LLAVE_ABRE = 14
    COMA = 15
    PUNTO_COMA = 16
    ASTERISCO = 17
    DIAGONAL = 18
    EXCLAMACION = 19
    NO_IGUAL = 20
    IGUAL = 21
    IGUAL_COMPARAR = 22
    GUION_BAJO = 23
    
    COMILLA_SIMPLE = 24
    COMILLA_DOBLE = 25
    
    # Operaciones
    LE = 26
    NE = 27
    LT = 28
    EQ = 29
    GE = 30
    GT = 31
    
    MENOR_QUE = 32
    MAYOR_QUE = 33
    
    # Palabras clave:
    Y = 34
    CLASE = 35
    ADEMAS = 36
    FALSO = 37
    PARA = 38
    FUN = 39
    SI = 40
    NULO = 41
    O = 42
    IMPRIMIR = 43
    RETORNAR = 44
    SUPER = 45
    ESTE = 46
    VERDADERO = 47
    VAR = 48
    MIENTRAS = 49
    
    #DELIM
    DELIM_ESPACIO = 50
    
    # Final de cadena
    EOF = 51
    SALTO_LINEA = 52
    DIAGONAL_INVERTIDA = 53
    DOS_PUNTOS = 54
    AMPERSON = 55
    