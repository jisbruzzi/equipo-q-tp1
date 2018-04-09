# merge de 2 listas ordenadas de menor a mayor
import math


def merge(la, lb):

    l1 = list(la)
    l2 = list(lb)
    ret = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            ret.append(l1[0])
            l1.pop(0)
        else:
            ret.append(l2[0])
            l2.pop(0)
    ret.extend(l1)
    ret.extend(l2)

    return ret


def mergesort(lista):
    if len(lista) <= 1:
        return lista

    indice_medio = int(math.floor(len(lista) / 2))
    l1 = lista[0:indice_medio]
    l2 = lista[indice_medio:]

    return merge(mergesort(l1), mergesort(l2))


def ordenar(lista):
    return mergesort(lista)
