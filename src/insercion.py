def insertar(elemento,lista):
	menor=filter(lambda x: x <= elemento,lista)
	mayor=filter(lambda x: x >  elemento,lista)
	return menor + [elemento] + mayor

def insercion(lista):
	lista=list(lista)#copia
	resultado=[]
	for e in lista:
		resultado=insertar(e,resultado)
	return resultado


def ordenar(lista):
	return insercion(lista)
