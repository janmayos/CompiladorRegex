import re
from AnalisisLexico import genera_lista_tokens
from Token import Token

def determina_bien_escrito(cadena,regextokens_linea,numlinea):
	ban = True
	for nombre in regextokens_linea:
		if re.fullmatch(regextokens_linea[nombre], cadena):
			print("Esta bien escrito: '"+ cadena + "' "+nombre+" "+str(numlinea))
			ban = False
			break
	if(ban):
		print("Linea no reconocida '"+cadena+"'"+" "+str(numlinea))
if __name__ == '__main__':
	regextokens_linea = {
		"Variables_asinación" : "PR(ID(COMA|(IGUAL(Numeros|COMILLA_SIMPLEIDCOMILLA_SIMPLE|COMILLA_DOBLE(ID)*COMILLA_DOBLE|ID)))*)+PUNTO_COMA",
		"Definir_funcion" : "(PRID|ID)(PARENTESIS_ABRE((PARENTESIS_CIERRALLAVE_ABRE)|(PARENTESIS_CIERRA)|(PRID(COMAPRID)*((PARENTESIS_CIERRALLAVE_ABRE)|(PARENTESIS_CIERRA)))))",
		"Libreria" : "NUMERALIDMENOR_QUE(ID|(IDPUNTOID))MAYOR_QUE"
	}
	#PR_.+(PARENTESIS_ABRE(((PARENTESIS_CIERRALLAVE_ABRE)|(PARENTESIS_CIERRA)|(ID(COMAID)*((PARENTESIS_CIERRALLAVE_ABRE)|(PARENTESIS_CIERRA))))))
	for listatoken in genera_lista_tokens():
		cadena_linea = ""
		numlinea = 0
		if len(listatoken) != 0:
			for token in listatoken:
				cadena_linea += token.get_tipo()
				numlinea = token.get_linea()
			determina_bien_escrito(cadena_linea.strip(),regextokens_linea,numlinea)