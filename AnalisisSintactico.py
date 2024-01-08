import re
from AnalisisLexico import genera_lista_tokens
from Token import Token

def determina_bien_escrito(cadena,cadena_lexema,regextokens_linea,numlinea,operacion_full_dosdatos_full_final):
	#comentario al final de caracter conocido
	comentario = "DIVISIONDIVISION.*"
	comentario_real = "\\/\\/.*"
	ban = True
	bantipodato = True
	#https://es.scribd.com/document/325651719/Los-tipos-de-datos-en-C-docx
	#http://www.gridmorelos.uaem.mx/~mcruz/cursos/varydat.pdf
	tipodato = { 
		"int" : "(SUMA|RESTA)?((Numero|Numeros)|ID|("+operacion_full_dosdatos_full_final+"))",
		"signedint" : "(SUMA|RESTA)?((Numero|Numeros)|ID|("+operacion_full_dosdatos_full_final+"))",
		"unsigned" : "(SUMA)?((Numero|Numeros)|ID|("+operacion_full_dosdatos_full_final+"))",
		"float": "(SUMA|RESTA)?((Numero|Numeros)(PUNTO(Numero|Numeros))?|ID|("+operacion_full_dosdatos_full_final+"))",
		"double": "(SUMA|RESTA)?((Numero|Numeros)(PUNTO(Numero|Numeros))?|ID|("+operacion_full_dosdatos_full_final+"))",
		"char" : "(COMILLA_SIMPLE.*COMILLA_SIMPLE)|(Numero|Numeros)",
		"bool" : "Numero",
		"short" : "(SUMA|RESTA)?((Numero|Numeros)|ID|("+operacion_full_dosdatos_full_final+"))",
		"signedshort" : "(SUMA|RESTA)?((Numero|Numeros)|ID|("+operacion_full_dosdatos_full_final+"))",
		"unsignedshort" : "(SUMA)?((Numero|Numeros)|ID|("+operacion_full_dosdatos_full_final+"))"
		


	}

	for nombre in regextokens_linea:
		if re.fullmatch("(("+regextokens_linea[nombre]["regex"]+")|("+regextokens_linea[nombre]["regex"]+comentario+"))", cadena):
			if "Definir_Variables" == nombre:
				for tipo in tipodato:
					if re.fullmatch(tipo+".*",cadena_lexema):
						for variabletipo in cadena[4:-10].split("COMA"):
							if variabletipo.find("IGUAL")!=-1:
								print(cadena_lexema,variabletipo,variabletipo[variabletipo.find("IGUAL")+5::])
								if re.fullmatch(tipodato[tipo],variabletipo[variabletipo.find("IGUAL")+5::]):
									print("Correcto tipo de dato")
								else:
									print("Tipo de dato no compatible "+cadena_lexema)
									exit(0)
						bantipodato = False
						break
				if bantipodato:
					print("Palabra reservada no incluida "+cadena_lexema)
					exit(0)
			if "Eval" in regextokens_linea[nombre]:
				if not re.fullmatch("(("+regextokens_linea[nombre]["Eval"]+")|("+regextokens_linea[nombre]["Eval"]+comentario_real+"))", cadena_lexema):
					print("Linea no reconocida EVAL '"+cadena_lexema+"'"+" "+str(numlinea))
					exit(0)
			print("Esta bien escrito: '"+ cadena + "' "+nombre+" "+str(numlinea))
			ban = False
			break
	if(ban):
		#Tiene comentario 
		if re.fullmatch(comentario, cadena):
			print("Tiene comentario")
			exit(0)
		print("Linea no reconocida '"+cadena+"'"+" "+str(numlinea))
		exit(0) #Termina si no reconoce linea
if __name__ == '__main__':

	#dato primitivo conocido 
	datonorm ="((ID)|(COMILLA_SIMPLE.+COMILLA_SIMPLE)|(COMILLA_DOBLE.+COMILLA_DOBLE)|(((RESTA|SUMA)?(Numeros|Numero))(PUNTO((RESTA|SUMA)?(Numeros|Numero)))?))"
	
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
	
	##Operacion matematica
	#dato primitivo conocido para operaciones matematicas
	datonorm_mat ="((ID)|(((RESTA|SUMA)?(Numeros|Numero))(PUNTO((RESTA|SUMA)?(Numeros|Numero)))?))"
	
	#dato con parentesis o sin parentesis
	dato_mat =  "(("+datonorm_mat+")|(PARENTESIS_ABRE("+datonorm_mat+")PARENTESIS_CIERRA))"


	#operadores de comparacion Menor que: < Mayor que: > Igual: = Diferente: != Menor o igual que: <= Mayor o igual que: >=

	operadores_mat = "(SUMA|RESTA|MULTIPLICACION|DIVISION|MODULO)"

	#Operacion matematica dos datos primitivos con los operadores e.g. 1 + 1
	operacion_normal="("+dato_mat+operadores_mat+dato_mat+")"
	
	#Operacion entre parentesis
	operacion_parentesis= "(PARENTESIS_ABRE("+operacion_normal+")PARENTESIS_CIERRA)"

	#Combinacion de operacion matematica con parentesis o sin parentesis

	operacion_full = "(("+operacion_normal+")|("+operacion_parentesis+"))"

	#Operacion combinacion 
	#Operaciones de mas datos mat
	operacion_full_dosdatos="(("+dato_mat+"|"+operacion_full+")(("+operadores_mat+")("+dato_mat+"|"+operacion_full+"))*)"
	
	#Union de operadores logicos con comparaciones encerrado entre parentesis 
	operacion_full_dosdatos_parentesis = "(PARENTESIS_ABRE("+operacion_full_dosdatos+")PARENTESIS_CIERRA)"
	
	#Union de operadores logicos con comparaciones encerrado entre parentesis o sin
	operacion_full_dosdatos_full="((("+operacion_full_dosdatos+")|("+operacion_full_dosdatos_parentesis+")))"
	
	##Union de operadores logicos con comparaciones encerrado entre parentesis o sin, ya sea una o otra
	operacion_full_dosdatos_full_final = "(("+operacion_full_dosdatos_full+")(("+operadores_mat+")("+operacion_full_dosdatos_full+"))*)+"

	#print(operacion_full_dosdatos)
	#exit(0)
	regextokens_linea = {
		"Definir_Variables" : { #http://www.gridmorelos.uaem.mx/~mcruz/cursos/varydat.pdf
			"regex": 
			"PR(PR)?(ID(COMA|(IGUAL("+operacion_full_dosdatos_full_final+"|"+comparacion_full_operador_logico_parentesis_full_final+"|((RESTA|SUMA)?(Numeros|Numero))|COMILLA_SIMPLE.*COMILLA_SIMPLE|COMILLA_DOBLE.*COMILLA_DOBLE|ID)))*)+PUNTO_COMA"
		},
		"Variables_asinacion" : {
			"regex": 
			"IDIGUAL(("+operacion_full_dosdatos_full_final+")|("+comparacion_full_operador_logico_parentesis_full_final+")|("+dato+"))PUNTO_COMA"
		},
		"Definir_funcion" : {
			"regex" : "(PRID|ID)(PARENTESIS_ABRE((PARENTESIS_CIERRALLAVE_ABRE)|(PARENTESIS_CIERRA)|(PRID(COMAPRID)*((PARENTESIS_CIERRALLAVE_ABRE)|(PARENTESIS_CIERRA)))))"
		},
		"Lamar_funcion" : {
			"regex" : "IDPARENTESIS_ABRE(((("+dato+"|("+operacion_full_dosdatos_full_final+")|("+comparacion_full_operador_logico_parentesis_full_final+"))(COMA("+dato+"|("+operacion_full_dosdatos_full_final+")|("+comparacion_full_operador_logico_parentesis_full_final+")))*)PARENTESIS_CIERRA)|(PARENTESIS_CIERRA))PUNTO_COMA"
		},
		"Libreria" : {
			"regex" : "NUMERALID((MENOR_QUE(ID|(IDPUNTOID))MAYOR_QUE)|(COMILLA_DOBLE(ID|(IDPUNTOID)|(PR))COMILLA_DOBLE))", #https://www.programarya.com/Cursos/C++/Bibliotecas-o-Librerias
			"Eval" : "#include.*"
		},
		"Imprimir_cout" : {
			"regex" : "(PRDOS_PUNTOSDOS_PUNTOS)?PR(MENOR_QUEMENOR_QUE((PARENTESIS_ABRE(ID|"+operacion_full_dosdatos_full_final+"|COMILLA_DOBLE+.+COMILLA_DOBLE)PARENTESIS_CIERRA)|(ID|"+operacion_full_dosdatos_full_final+"|COMILLA_DOBLE+.+COMILLA_DOBLE)))+PUNTO_COMA",
			"Eval" : "(cout.*;|std::cout.*;)"
		},
		"Obtener_cin" : {
			"regex" : "PRMAYOR_QUEMAYOR_QUE((PARENTESIS_ABREIDPARENTESIS_CIERRA)|(ID))PUNTO_COMA",
			"Eval" : "(cin.*;|std::cin.*;)"
		},
		"Using_namespace_std" : {
			"regex" : "PRPRPRPUNTO_COMA",
			"Eval" : "usingnamespacestd;"
		},
		"if" : {
			"regex" : "PRPARENTESIS_ABRE("+comparacion_full_operador_logico_parentesis_full_final+")((PARENTESIS_CIERRALLAVE_ABRE)|(PARENTESIS_CIERRA))",
			"Eval" : "if(.*)\\{?"
		},
		"switch" : {
			"regex" : "PRPARENTESIS_ABRE(ID)((PARENTESIS_CIERRALLAVE_ABRE)|(PARENTESIS_CIERRA))",
			"Eval" : "switch(.*)\\{?"
		},
		"Comentario" : {
			"regex" : "DIVISIONDIVISION.*"
		},
		"Llaves_contenedor" : {
			"regex" : "(LLAVE_ABRE|LLAVE_CIERRA)"
		},
		"Case":{
			"regex" : "(PR"+datonorm+"DOS_PUNTOS)",
			"Eval" : "case.*:"
		},
		"default":{
			"regex" : "(PRDOS_PUNTOS)",
			"Eval" : "default:"
		}
	}
	"""
		"Operacion_mat": {
			"regex" : operacion_full_dosdatos_full_final+"PUNTO_COMA"
		}
	"""		
	#print(regextokens_linea["Lamar_funcion"]["regex"])
	#exit(0)
	incremento_decremento = "(IDSUMASUMA|IDRESTARESTA)"
	regextokens_linea["incremento_decremento"]={
			"regex" : "("+incremento_decremento+"PUNTO_COMA)"
		}
	for_center = "("+regextokens_linea["Definir_Variables"]["regex"]+comparacion_full+"PUNTO_COMA("+incremento_decremento+"(COMA)?)+)"
	regextokens_linea["for"]={
			"regex" : "PRPARENTESIS_ABRE("+for_center+")((PARENTESIS_CIERRALLAVE_ABRE)|(PARENTESIS_CIERRA))",
			"Eval" : "for(.*)\\{?"
		}
	regextokens_linea["forinfinite"]={
			"regex" : "PRPARENTESIS_ABREPUNTO_COMAPUNTO_COMAPARENTESIS_CIERRA",
			"Eval" : "for(.*)\\{?"
		}
	regextokens_linea["Palabra_reservada"]={
			"regex" : "PRPUNTO_COMA",
			"Eval" : "break;|continue;"
		}
	
	regextokens_linea["return"]={
			"regex" : "(PR(("+operacion_full_dosdatos_full_final+")|("+comparacion_full_operador_logico_parentesis_full_final+")|("+dato+"))PUNTO_COMA)",
			"Eval" : "return(.*);"
		}
	regextokens_linea["Variables_asinacion_funcion"]={
		"regex" : "IDIGUAL"+regextokens_linea["Lamar_funcion"]["regex"]
	}
	regextokens_linea["Definir_Variables_funcion"]={
		"regex" : "PRIDIGUAL"+regextokens_linea["Lamar_funcion"]["regex"]
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
			determina_bien_escrito(cadena_linea.strip(),cadena_lexema.strip(),regextokens_linea,numlinea,operacion_full_dosdatos_full_final)