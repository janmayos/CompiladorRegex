import re
from Token import Token



#Se declara una lista de las palabras reservadas en c++
palabras_reservadas = ["abstract","event","namespace","static","as","explicit","new","string","base","extern","null","struct","bool","false","object","switch","break","finally","operator","this","byte","fixed","out","throw","case","float","override","true","catch","for","params","try","char","foreach","private","typeof","checked","goto","protected","uint","class","if","public","ulong","const","implicit","readonly","unchecked","continue","in","ref","unsafe","decimal","int","return","ushort","default","interface","sbyte","using","delegate","internal","sealed","virtual","do","is","short","volatile","double","lock","sizeof","void","else","long","stackalloc","while","enum","String","cout"]
#Se declara una lista de los simbolos aritmeticos
lista_simbolos_aritmeticos = {'-' : "RESTA",'+' : "SUMA",'*' : "MULTIPLICACIÓN",'/' : "DIVISIÓN",'%' : "MÓDULO","--" : "DECREMENTO","++" : "INCREMENTO"}
#Se declara una lista de los simbolos de puntuación conocidos
signos_puntuacion = {"#":"NUMERAL","<": "MENOR_QUE",">": "MAYOR_QUE","=": "IGUAL",".": "PUNTO","+": "MAS","-": "MENOS"," ": "DELIM_ESPACIO","(": "PARENTESIS_ABRE",")": "PARENTESIS_CIERRA","{": "LLAVE_ABRE","}": "LLAVE_CIERRA",",": "COMA",";": "PUNTO_COMA","*": "ASTERISCO","/": "DIAGONAL","!": "EXCLAMACION","_": "GUION_BAJO","'": "COMILLA_SIMPLE","\"" : "COMILLA_DOBLE","\n": "SALTO_LINEA","\\": "DIAGONAL_INVERTIDA",":": "DOS_PUNTOS","&": "AMPERSON","%":"PORCENTAJE"}

#Expresiones regulares basicas
regexstrbase = {
	"Letra" : "[a-zA-z-áéíóúÁÉÍÓÚ]",
	"Numero" : "[0-9]",
	"Numeros" : "[0-9]+",
	"Letras_numeros": "[a-zA-z-áéíóúÁÉÍÓÚ0-9]*"
}

#Expresiones regulares complejas
dic_regex_evalute = {
	"ID" : regexstrbase["Letra"]+regexstrbase["Letras_numeros"]    
	}


#Genera una lista recorriendo caracter por caracter hasta un caracter desconocido y los separa en una tupla
#de elementos y se retorna una lista
def lista_split_letras_numeros(cadena,aux_separador):
	auxcadena = ""
	for caracter in cadena:
		if  re.fullmatch( regexstrbase["Letra"], caracter) or re.fullmatch( regexstrbase["Numero"], caracter):
			auxcadena += caracter
			#print(auxcadena)
		else:
			if auxcadena == "":
				aux_separador.append(caracter)
			else:
				aux_separador.append(auxcadena)
				aux_separador.append(caracter)
				auxcadena = ""
	if auxcadena != "":
		aux_separador.append(auxcadena)
	

#Determina token que tiene caracteres no reconocidos en las expresiones regulares basicas
# y determina los token de la nueva lista de letras numeros
def determina_token_complejo(cadena,aux_lista_tokens,numlinea):
	aux_separador = []
	lista_split_letras_numeros(cadena,aux_separador)
	for separador in aux_separador:
		token = determinta_token(separador)
		#print(token)
		if token != None:
			aux_lista_tokens.append(Token(token,separador,separador,numlinea))
		else:
			print("Token no reconocido: "+separador)
			exit(0)
		
#Determina el vocabulario del token por palabras reservadas ID o numeros
def determinta_token(cadena):
	#print(cadena)
	if cadena in palabras_reservadas:
		return "PR"#"PR_"+cadena
	elif  re.fullmatch(dic_regex_evalute["ID"], cadena):
		return "ID"
	elif cadena in lista_simbolos_aritmeticos:
		return lista_simbolos_aritmeticos[cadena]
	elif cadena in signos_puntuacion:
		return signos_puntuacion[cadena]
	elif re.fullmatch( regexstrbase["Numeros"], cadena):
		return "Numeros"
	
def genera_lista_tokens():
	lista_tokens = []
	numlinea = 0
	with open("script.txt") as file:
		for linea in file:
			numlinea += 1
			aux_lista_tokens = []
			aux_split_espacios = linea.replace("\n","").split(" ")
			#print(aux_split_espacios)
			for cadena in aux_split_espacios:
				if cadena != '':
					token = determinta_token(cadena)
					if token != None:
						aux_lista_tokens.append(Token(token,cadena,cadena,numlinea))
					else:
						determina_token_complejo(cadena,aux_lista_tokens,numlinea)
			lista_tokens.append(aux_lista_tokens)        
	return lista_tokens		


if __name__ == '__main__':
	for token in genera_lista_tokens():
		if len(token) != 0:
			for auxtoken in token:
				print(str(auxtoken.get_info()))	