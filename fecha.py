# -*- coding: utf-8 -*-         

def anio(sFechaInicio, sFechaFinal):
    
    nDiaInicio, nMesInicio, nAnioInicio = (int(item) for item in sFechaInicio.split("/"))
    nDiaFinal, nMesFinal, nAnioFinal = (int(item) for item in sFechaFinal.split("/"))
    nAnioAuxiliar = nAnioFinal - nAnioInicio

    if (nMesFinal < nMesInicio):
        nAnioAuxiliar = nAnioAuxiliar - 1
    elif (nDiaFinal < nDiaInicio):
        nAnioAuxiliar = nAnioAuxiliar - 1
        
    return nAnioAuxiliar

# -------------------------------------------

sFechaInicio = input("Fecha nacimiento: ")
sFechaFinal = input("Fecha destino: ")

print(f"Edad: {anio(sFechaInicio, sFechaFinal)}")



#--------------------------------------------------------------------------

if __name__ == '__main__':
	main()
