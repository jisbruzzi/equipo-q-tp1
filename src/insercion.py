def insertar(elemento,lista):
	lista = list(lista)
	resultado = []
	while len(lista) > 0:
		e = lista.pop(0)
		if e < elemento:
			resultado = resultado + [e]
		else:
			lista=[e]+lista
			break
	return resultado+[elemento]+lista

def insercion(lista):
	lista = list(lista)#copia
	resultado = []
	for e in lista:
		resultado = insertar(e, resultado)
	return resultado

def ordenar(lista):
	return insercion(lista)