def insertar(elemento,lista):
	#l=len(lista)
	#print(str(elemento)+"/"+str(lista))

	lista = list(lista)
	resultado = []
	while len(lista) > 0:
		e = lista.pop()
		if e >= elemento:
			resultado = [e] + resultado
		else:
			lista = lista + [e]
			break
	#lr=len(resultado)
	#print(str(lr)+"/"+str(l))
	
	
	return lista + [elemento] + resultado

def insercion(lista):
	lista = list(lista)#copia
	resultado = []
	for e in lista:
		resultado = insertar(e, resultado)
	return resultado

def ordenar(lista):
	return insercion(lista)