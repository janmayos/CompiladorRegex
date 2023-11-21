import re
from AnalisisLexico import genera_lista_tokens
from Token import Token

def determina_bien_escrito(cadena,cadena_lexema,regextokens_linea,numlinea):
	ban = True
	for nombre in regextokens_linea:
		if re.fullmatch(regextokens_linea[nombre]["regex"], cadena):
			if "Eval" in regextokens_linea[nombre]:
				if not re.fullmatch(regextokens_linea[nombre]["Eval"], cadena_lexema):
					print("Linea no reconocida '"+cadena_lexema+"'"+" "+str(numlinea))
					exit(0)
			print("Esta bien escrito: '"+ cadena + "' "+nombre+" "+str(numlinea))
			ban = False
			break
	if(ban):
		print("Linea no reconocida '"+cadena+"'"+" "+str(numlinea))
if __name__ == '__main__':
	regex_base_sintac = {
		"datonorm" : "(ID|COMILLA_SIMPLE.+COMILLA_SIMPLE|COMILLA_DOBLE.+COMILLA_DOBLE|(Numeros|Numero)(PUNTO(Numeros|Numero))?)",
		"dato" : "((ID|COMILLA_SIMPLE.+COMILLA_SIMPLE|COMILLA_DOBLE.+COMILLA_DOBLE|(Numeros|Numero)(PUNTO(Numeros|Numero))?)|(PARENTESIS_ABRE(ID|COMILLA_SIMPLE.+COMILLA_SIMPLE|COMILLA_DOBLE.+COMILLA_DOBLE|(Numeros|Numero)(PUNTO(Numeros|Numero))?)PARENTESIS_CIERRA))",
		"operadores_comparacion" : "(IGUALIGUAL|EXCLAMACIONIGUAL|MENOR_QUE|MAYOR_QUE|MENOR_QUEIGUAL|MAYOR_QUEIGUAL)"
		
	}
	regex_base_complex = {
		"comparación" : "("+regex_base_sintac["dato"]+")("+regex_base_sintac["operadores_comparacion"]+")("+regex_base_sintac["dato"]+")",
		"comparacion_parentesis" : "PARENTESIS_ABRE("+"("+regex_base_sintac["dato"]+")("+regex_base_sintac["operadores_comparacion"]+")("+regex_base_sintac["dato"]+")"+")PARENTESIS_CIERRA",
		"comparacion_full" : "(("+"("+regex_base_sintac["dato"]+")("+regex_base_sintac["operadores_comparacion"]+")("+regex_base_sintac["dato"]+")"+")|("+"PARENTESIS_ABRE("+"("+regex_base_sintac["dato"]+")("+regex_base_sintac["operadores_comparacion"]+")("+regex_base_sintac["dato"]+")"+")PARENTESIS_CIERRA"+"))",			
	}
	regextokens_linea = {
		"Variables_asinación" : {
			"regex": "PR(ID(COMA|(IGUAL(Numeros|COMILLA_SIMPLEIDCOMILLA_SIMPLE|COMILLA_DOBLE(ID)*COMILLA_DOBLE|ID)))*)+PUNTO_COMA"
		},
		"Definir_funcion" : {
			"regex" : "(PRID|ID)(PARENTESIS_ABRE((PARENTESIS_CIERRALLAVE_ABRE)|(PARENTESIS_CIERRA)|(PRID(COMAPRID)*((PARENTESIS_CIERRALLAVE_ABRE)|(PARENTESIS_CIERRA)))))"
		},
		"Libreria" : {
			"regex" : "NUMERALIDMENOR_QUE(ID|(IDPUNTOID))MAYOR_QUE"
		},
		"Imprimir_cout" : {
			"regex" : "(PRDOS_PUNTOSDOS_PUNTOS)?PR(MENOR_QUEMENOR_QUE((PARENTESIS_ABRE(ID|COMILLA_DOBLE+.+COMILLA_DOBLE)PARENTESIS_CIERRA)|(ID|COMILLA_DOBLE+.+COMILLA_DOBLE)))+PUNTO_COMA"
		},
		"Obtener_cin" : {
			"regex" : "PRMAYOR_QUEMAYOR_QUE((PARENTESIS_ABREIDPARENTESIS_CIERRA)|(ID))PUNTO_COMA"
		},
		"Using_namespace_std" : {
			"regex" : "PRPRPRPUNTO_COMA",
			"Eval" : "usingnamespacestd;"
		},
		"if" : {
			"regex" : "PRPARENTESIS_ABRE"+regex_base_complex["comparacion_full"]+"PARENTESIS_CIERRA",
		}
	}
	#PR_.+(PARENTESIS_ABRE(((PARENTESIS_CIERRALLAVE_ABRE)|(PARENTESIS_CIERRA)|(ID(COMAID)*((PARENTESIS_CIERRALLAVE_ABRE)|(PARENTESIS_CIERRA))))))
	for listatoken in genera_lista_tokens():
		cadena_linea = ""
		cadena_lexema = ""
		numlinea = 0
		if len(listatoken) != 0:
			for token in listatoken:
				cadena_linea += token.get_tipo()
				cadena_lexema += token.get_lexema()
				numlinea = token.get_linea()
			determina_bien_escrito(cadena_linea.strip(),cadena_lexema.strip(),regextokens_linea,numlinea)