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

	#dato primitivo conocido 
	datonorm ="((ID)|(COMILLA_SIMPLE.+COMILLA_SIMPLE)|(COMILLA_DOBLE.+COMILLA_DOBLE)|((Numeros|Numero)(PUNTO(Numeros|Numero))?))"
	
	#dato con parentesis o sin parentesis
	dato =  "(("+datonorm+")|(PARENTESIS_ABRE("+datonorm+")PARENTESIS_CIERRA))"

	#operadores de comparacion Menor que: < Mayor que: > Igual: = Diferente: != Menor o igual que: <= Mayor o igual que: >=

	operadores_comparacion = "(IGUALIGUAL|EXCLAMACIONIGUAL|MENOR_QUE|MAYOR_QUE|MENOR_QUEIGUAL|MAYOR_QUEIGUAL)"
	
	#Dato con negación
	dato_exclamacion = "((EXCLAMACION)*"+dato+")"

	#Comparar dos datos primitivos con los operadores e.g. a < 1
	comparacion="("+dato_exclamacion+operadores_comparacion+dato_exclamacion+")"
	
	#Comparar dos datos primitivos con los operadores y encerrado entre parentesis con su posible negacion e.g. 
	# (a < 1)
	# !(!a <= 1)

	comparacion_parentesis= "((EXCLAMACION)*PARENTESIS_ABRE("+comparacion+")PARENTESIS_CIERRA)"

	#Combinacion de comparacion con parentesis o sin parentesis

	comparacion_full = "(("+comparacion+")|("+comparacion_parentesis+"))"
	
	# operadores logicos compuerta and or 
	operadorlogico = "(AMPERSONAMPERSON|PLECAPLECA)"
	
	
	#Union de operadores logicos con comparaciones 
	comparacion_full_operador_logico="(("+comparacion_full+")(("+operadorlogico+")("+comparacion_full+"))*)"
	
	#Union de operadores logicos con comparaciones encerrado entre parentesis 
	comparacion_full_operador_logico_parentesis = "(PARENTESIS_ABRE("+comparacion_full_operador_logico+")PARENTESIS_CIERRA)"
	
	#Union de operadores logicos con comparaciones encerrado entre parentesis o sin
	comparacion_full_operador_logico_parentesis_full="((("+comparacion_full_operador_logico+")|("+comparacion_full_operador_logico_parentesis+")))"
	
	##Union de operadores logicos con comparaciones encerrado entre parentesis o sin, ya sea una o otra
	comparacion_full_operador_logico_parentesis_full_final = "(("+comparacion_full_operador_logico_parentesis_full+")(("+operadorlogico+")("+comparacion_full_operador_logico_parentesis_full+"))*)+"
	#print(comparacion_full_operador_logico_parentesis_full_final)
	#exit(0)
	


	regextokens_linea = {
		"Variables_asinación" : {
			"regex": 
			"PR(ID(COMA|(IGUAL(Numeros|Numero|COMILLA_SIMPLEIDCOMILLA_SIMPLE|COMILLA_DOBLE(ID)*COMILLA_DOBLE|ID)))*)+PUNTO_COMA"
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
			"regex" : "PRPARENTESIS_ABRE("+comparacion_full_operador_logico_parentesis_full_final+")((PARENTESIS_CIERRALLAVE_ABRE)|(PARENTESIS_CIERRA))",
		},
		"Comentario" : {
			"regex" : "DIVISIÓNDIVISIÓN.*"
		},
		"Contenedor" : {
			"regex" : "(LLAVE_ABRE|LLAVE_CIERRA)"
		}
	}

	incremento_decremento = "(IDSUMASUMA|IDRESTARESTA)"
	regextokens_linea["incremento_decremento"]={
			"regex" : "("+incremento_decremento+"PUNTO_COMA)"
		}
	for_center = "("+regextokens_linea["Variables_asinación"]["regex"]+comparacion_full+"PUNTO_COMA("+incremento_decremento+"(COMA)?)+)"
	regextokens_linea["for"]={
			"regex" : "PRPARENTESIS_ABRE("+for_center+")((PARENTESIS_CIERRALLAVE_ABRE)|(PARENTESIS_CIERRA))"
		}
	regextokens_linea["forinfinite"]={
			"regex" : "PRPARENTESIS_ABREPUNTO_COMAPUNTO_COMAPARENTESIS_CIERRA"
		}
	regextokens_linea["Palabra_reservada"]={
			"regex" : "PRPUNTO_COMA"
		}
	
	regextokens_linea["return"]={
			"regex" : "(PR("+dato+")PUNTO_COMA)"
		}

	#print(regextokens_linea["if"]["regex"])
	#exit(0)
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