import re
from termcolor import colored


#Se declara una lista de las palabras reservadas en c++
palabras_reservadas = ["abstract","event","namespace","static","as","explicit","new","string","base","extern","null","struct","bool","false","object","switch","break","finally","operator","this","byte","fixed","out","throw","case","float","override","true","catch","for","params","try","char","foreach","private","typeof","checked","goto","protected","uint","class","if","public","ulong","const","implicit","readonly","unchecked","continue","in","ref","unsafe","decimal","int","return","ushort","default","interface","sbyte","using","delegate","internal","sealed","virtual","do","is","short","volatile","double","lock","sizeof","void","else","long","stackalloc","while","enum"]
#Se declara una lista de los simbolos aritmeticos
lista_simbolos_aritmeticos = {'-' : "Resta",'+' : "Suma",'*' : "Multiplicación",'/' : "División",'%' : "Módulo","--" : "Decremento","++" : "Incremento"}
#Se declara una lista de los simbolos de puntuación conocidos
signos_puntuacion = {"<": "MENOR_QUE",">": "MAYOR_QUE","=": "IGUAL",".": "PUNTO","+": "MAS","-": "MENOS"," ": "DELIM_ESPACIO","(": "PARENTESIS_ABRE",")": "PARENTESIS_CIERRA","{": "LLAVE_ABRE","}": "LLAVE_CIERRA",",": "COMA",";": "PUNTO_COMA","*": "ASTERISCO","/": "DIAGONAL","!": "EXCLAMACION","_": "GUION_BAJO","'": "COMILLA_SIMPLE","\"" : "COMILLA_DOBLE","\n": "SALTO_LINEA","\\": "DIAGONAL_INVERTIDA",":": "DOS_PUNTOS","&": "AMPERSON","%":"PORCENTAJE"}

regexstrbase = {
    "Letra" : "[a-zA-z-áéíóúÁÉÍÓÚ]",
    "Numero" : "[0-9]",
    "Numeros" : "[0-9]+",
    "Letras_numeros": "[a-zA-z-áéíóúÁÉÍÓÚ0-9]*"
}

dic_regex_evalute = {
    "ID" : regexstrbase["Letra"]+regexstrbase["Letras_numeros"]    
    }

auxlinea = None
lista_tokens = []

def determina_token_complejo(cadena,aux_lista_tokens):
    auxcadena = ""
    ban_caracter = True
    for caracter in cadena:
        if  ban_caracter and (re.fullmatch( regexstrbase["Letra"], caracter) or re.fullmatch( regexstrbase["Numero"], caracter)):
            auxcadena += caracter
            print(auxcadena)
        else:
            if auxcadena == "":
                token = determinta_token(caracter)
                if token != None:
                    aux_lista_tokens.append(token)
                else:
                    print("Token no reconocido  "+cadena)
                    exit(0)
            else:
                token = determinta_token(auxcadena)
                print(token,ban_caracter)
                if token != None:
                    aux_lista_tokens.append(token)
                    auxcadena = caracter
                    if ban_caracter:

                        ban_caracter = False
                    else:
                        if  re.fullmatch( regexstrbase["Letra"], auxcadena) or re.fullmatch( regexstrbase["Numero"], auxcadena):
                            ban_caracter = True
                else:
                    print("Token no reconocido  "+cadena)
                    exit(0)
        
    if not ban_caracter: 
        token = determinta_token(auxcadena)
        print(token)
        if token != None:
            aux_lista_tokens.append(token)
        else:
            print("Token final no reconocido  "+cadena)
            exit(0)
    
def determinta_token(cadena):
    print(cadena)
    if cadena in palabras_reservadas:
        return "PR_"+cadena
    elif  re.fullmatch(dic_regex_evalute["ID"], cadena):
        return "ID"
    elif cadena in signos_puntuacion:
        return signos_puntuacion[cadena]
    elif re.fullmatch( regexstrbase["Numeros"], cadena):
        return "Numeros"
    

with open("script.txt") as file:
    for linea in file:
        aux_lista_tokens = []
        aux_split_espacios = linea.replace("\n","").split(" ")
        print(aux_split_espacios)
        for cadena in aux_split_espacios:
            if cadena != '':
                token = determinta_token(cadena)
                if token != None:
                    aux_lista_tokens.append(token)
                else:
                    determina_token_complejo(cadena,aux_lista_tokens)
            
        print(colored(f"{str(aux_lista_tokens)}", 'green'))
        #if re.fullmatch(pat, linea.rstrip()):
        #    print(colored(f"'{linea.rstrip()}'\tMAIL!", 'green'))
        #else:
        #    print(colored(f"'{linea.rstrip()}'\tNO MAIL", 'red'))
