# -*- coding: utf-8 -*-         

#--------------------------------------------------------------------------

def calcularAnios(sFechaInicial, sFechaFinal):
	nAnioAuxiliar = 0

	nDiaInicio, nMesInicio, nAnioInicio = (int(item) for item in sFechaInicial.split("/"))

	nDiaFinal, nMesFinal, nAnioFinal = (int(item) for item in sFechaFinal.split("/"))

	nAnioAuxiliar = nAnioFinal - nAnioInicio

	if (nMesFinal < nMesInicio) and (nDiaFinal < nDiaInicio):
		nAnioAuxiliar = nAnioAuxiliar - 1

	return nAnioAuxiliar

#--------------------------------------------------------------------------

def main():

	sFechaInicial = input("Fecha de inicio (DD/MM/AAAA): ")
	sFechaFinal = input("Fecha final (DD/MM/AAAA): ")
	
	print ("Cantidad de años: {}".format(calcularAnios(sFechaInicial, sFechaFinal)))

#--------------------------------------------------------------------------

if __name__ == '__main__':
	main()
