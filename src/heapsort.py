import math


def agregar_a_heap(heap, e):
    heap_roto = heap[:]
    heap_roto.append(e)

    ie = len(heap_roto) - 1
    i_raiz_local = int(math.floor(ie / 2))

    while heap_roto[i_raiz_local] < heap_roto[ie]:  # implicito: rompe cuando i_raiz_local=ie=0

        # intercambio

        e_raiz_local = heap_roto[i_raiz_local]
        e = heap_roto[ie]

        heap_roto[i_raiz_local] = e
        heap_roto[ie] = e_raiz_local

        # preparar ie e i_raiz_local
        ie = i_raiz_local
        i_raiz_local = int(math.floor(ie / 2))

    return heap_roto  # esta arreglado


def arbol_local_es_heap(heap, ie):
    i_hoja_izq = ie * 2 + 1
    i_hoja_der = ie * 2 + 2
    es_heap = True
    if i_hoja_izq < len(heap) and heap[i_hoja_izq] > heap[ie]:
        es_heap = False
    if i_hoja_der < len(heap) and heap[i_hoja_der] > heap[ie]:
        es_heap = False
    return es_heap


def i_mayor_hijo(heap, ie):
    i_hoja_izq = ie * 2 + 1
    i_hoja_der = ie * 2 + 2

    if i_hoja_izq < len(heap) and i_hoja_der < len(heap):
        # intercambio la cabeza con la mayor hoja
        return i_hoja_izq if heap[i_hoja_izq] > heap[i_hoja_der] else i_hoja_der
    else:
        if i_hoja_izq < len(heap):
            return i_hoja_izq
        if i_hoja_der < len(heap):
            return i_hoja_der
        else:
            return -1


def quitar_cabeza_de_heap(heap_anterior):
    if len(heap_anterior) == 1:
        return []

    heap = list(heap_anterior)
    heap[0] = heap.pop()

    ie = 0  # empieza arriba
    while not arbol_local_es_heap(heap, ie):
        i_intercambiar = i_mayor_hijo(heap, ie)

        e_raiz_local = heap[ie]
        e_intercambiar = heap[i_intercambiar]

        heap[ie] = e_intercambiar
        heap[i_intercambiar] = e_raiz_local

        ie = i_intercambiar

    return heap


def heapsort(lista):
    heap = []
    for e in lista:
        heap = agregar_a_heap(heap, e)

    lista_ordenada = []
    while len(heap) > 0:
        lista_ordenada = [heap[0]] + lista_ordenada
        heap = quitar_cabeza_de_heap(heap)

    return lista_ordenada


print(heapsort([8, 7, 15, 24, 0.5, 3, 0.1, 97]))
