def swap(lista, indice, indiceminimo):
    aux=lista[indice]
    lista[indice]=lista[indiceminimo]
    lista[indiceminimo]=aux

def ordenar(lista): #este es de orden O(n2)
    #i=0
    #j=0
    for i in range(len(lista)-1): #comienza desde el 0 hasta el largo de la lista menos uno
        min=i
        for j in range(i+1, len(lista)): #este for va del segundo hasta el untimo inclusive
            if lista[j]<lista[min]: #busca el menor entre todos
                min=j #aca tengo el subindice del menor de todos
        if min != i:
            swap(lista,i,min)#intercambiar, recordar que comienza de 0
    #j=j+1
    #i=i+1
    return lista

print(ordenar([3,2,1]))
print(ordenar([7,4,1,10,11,3,22]))
