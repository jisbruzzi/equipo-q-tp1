
def ordenar(lista):
	i=0
	j=0
	auxiliar=0
	while i< (len(lista)-1): #recorro la lista de punta a punta
		j=i
		while (j>0) and (lista[i]<lista [j-1]): #aca llego la hora de intercambiar donde cada operacion de cambio de valor es O(1)
			auxiliar=lista[j]
			lista[j]=lista[j-1]
			lista[j-1]=auxiliar
			j=j-1
		i+=1
	return lista

print(ordenar([3,2,1]))
print(ordenar([7,4,1,10,11,3,22]))