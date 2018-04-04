

import swap

def ordenar(lista) #este es de orden O(n2)
i=0
j=0
for i in range[0,len(lista)-1] #comienza desde el 0 hasta el largo de la lista menos uno
	max=i
	for j in range [i+1, len(lista)] #este for va del segundo hasta el untimo inclusive
		if (lista[j]>lista[min]) #busca el menor entre todos
			max=j #aca tengo el subindice del mayor de todos
		swap(lista,i,max)#intercambiar entre el i y el maximo, recordar que comienza de 0
		j=j+1
i=i+1





