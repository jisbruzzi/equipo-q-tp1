#merge de 2 listas ordenadas de menor a mayor
def merge(la,lb):
    l1=list(la)
    l2=list(lb)
    ret=[]
    while len(l1)>0 and len(l2)>0:
        if l1[0]<l2[0]:
            ret.append(l1[0])
            l1.pop(0)
        else:
            ret.append(l2[0])
            l2.pop(0)
    ret.extend(l1)
    ret.extend(l2)

    return ret

#mergesort
import math
def mergesort(lista):
    if len(lista)<=1:
        return lista

    indiceMedio=int(math.floor(len(lista)/2))
    l1=lista[0:indiceMedio]
    l2=lista[indiceMedio:]

    return merge(mergesort(l1),mergesort(l2))

print(mergesort([80,25,17,24,99,12,1,5,5,7,8,9,21,19,18,17,16,15]))