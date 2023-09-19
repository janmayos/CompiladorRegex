import re
from termcolor import colored

palabras_reservadas = ["abstract","event","namespace","static","as","explicit","new","string","base","extern","null","struct","bool","false","object","switch","break","finally","operator","this","byte","fixed","out","throw","case","float","override","true","catch","for","params","try","char","foreach","private","typeof","checked","goto","protected","uint","class","if","public","ulong","const","implicit","readonly","unchecked","continue","in","ref","unsafe","decimal","int","return","ushort","default","interface","sbyte","using","delegate","internal","sealed","virtual","do","is","short","volatile","double","lock","sizeof","void","else","long","stackalloc","while","enum"]
simbolos_aritmeticos = {
    
}


signos_puntuacion = {"<": "MENOR_QUE",">": "MAYOR_QUE","=": "IGUAL",".": "PUNTO","+": "MAS","-": "MENOS"," ": "DELIM_ESPACIO","(": "PARENTESIS_ABRE",")": "PARENTESIS_CIERRA","{": "LLAVE_ABRE","}": "LLAVE_CIERRA",",": "COMA",";": "PUNTO_COMA","*": "ASTERISCO","/": "DIAGONAL","!": "EXCLAMACION","_": "GUION_BAJO","'": "COMILLA_SIMPLE","\"" : "COMILLA_DOBLE","\n": "SALTO_LINEA","\\": "DIAGONAL_INVERTIDA",":": "DOS_PUNTOS","&": "AMPERSON"}

pat = re.compile(r"[a-zA-Z_]{1}[a-zA-Z1-9_-]*@+[a-zA-Z_]+.[a-zA-Z_]+")

with open("correos.txt") as file:
    for linea in file:
        if re.fullmatch(pat, linea.rstrip()):
            print(colored(f"'{linea.rstrip()}'\tMAIL!", 'green'))
        else:
            print(colored(f"'{linea.rstrip()}'\tNO MAIL", 'red'))
