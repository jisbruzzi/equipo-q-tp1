def swap(lista, indice, indiceminimo):
	aux=lista[indice]
	lista[indice]=lista[indiceminimo]
	lista[indiceminimo]=aux

def quicksort(lista, inf, sup): #cuando se lo llama se lo invoca con inf=0 y sup=largo de la lista
	if inf<sup:
		elem_div=lista[sup]
		i=inf-1
		j=sup
		cont=1
		while cont:
			i+=1
			while i<len(lista) and lista[i] < elem_div:
				j-=1
				while lista[j] > elem_div:
					if i<j:
						swap (lista, i, j)
					else:
						cont=0 #actua como rompedor del while ya que los indices se cruzan
		swap (lista, i, sup)
		ordenar(lista, inf, i-1)
		ordenar(lista, i+1, sup)
	return lista

def ordenar(lista):
	return quicksort(lista,0,len(lista)-1)

print(ordenar([3,2,1]))
print(ordenar([7,4,1,10,11,3,22]))

