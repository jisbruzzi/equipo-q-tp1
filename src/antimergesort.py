import math
import mergesort


def antimerge(ordenada):
    if len(ordenada) <= 1:
        return ordenada
    ordenadaSinUltimo = list(ordenada)
    ultimo = ordenadaSinUltimo.pop()

    indice_medio = int(math.floor(len(ordenadaSinUltimo) / 2))
    l1 = ordenadaSinUltimo[0:indice_medio] + [ultimo]
    l2 = ordenadaSinUltimo[indice_medio:]

    return l2, l1


def antimergesort(ordenada):
    if len(ordenada) <= 1:
        return ordenada

    l1, l2 = antimerge(ordenada)
    return antimergesort(l1) + antimergesort(l2)


def desordenar(ordenada):
    return antimergesort(ordenada)
