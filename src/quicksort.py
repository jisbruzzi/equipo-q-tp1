include swap

def ordenar(lista, inf, sup): #cuando se lo llama se lo invoca con inf=0 y sup=largo de la lista
if (inf<sup)
	elem_div=lista[sup]
	aux
	i=inf-1
	j=sup
	cont=1
	while cont
		while (lista[i++] < elem_div)
			while (lista[j--] > elem_div)
				if (i<j)
					swap (lista, i, j)
				else
					cont=0 #actua como rompedor del while ya que los indices se cruzan
	swap (lista, i, sup)
	ordenar(lista, inf, i-1)
	ordenar(lista, i+1, sup)



