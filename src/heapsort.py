import math

def agregarAHeap(heap,e):
    heapRoto=heap[:]
    heapRoto.append(e)

    ie=len(heapRoto)-1
    iRaizLocal=int(math.floor(ie/2))

    while heapRoto[iRaizLocal]<heapRoto[ie]: #implicito: rompe cuando iRaizLocal=ie=0

        #intercambio

        eRaizLocal=heapRoto[iRaizLocal]
        e=heapRoto[ie]

        heapRoto[iRaizLocal]=e
        heapRoto[ie]=eRaizLocal

        #preparar ie e iRaizLocal
        ie=iRaizLocal
        iRaizLocal=int(math.floor(ie/2))
    
    return heapRoto#esta arreglado


def arbolLocalEsHeap(heap,ie):
    iHojaIzq=ie*2+1
    iHojaDer=ie*2+2
    esHeap=True
    if iHojaIzq<len(heap) and heap[iHojaIzq]>heap[ie]:
        esHeap=False
    if iHojaDer<len(heap) and heap[iHojaDer]>heap[ie]:
        esHeap=False
    return esHeap


def iMayorHijo(heap,ie):
    iHojaIzq=ie*2+1
    iHojaDer=ie*2+2

    
    if iHojaIzq<len(heap) and iHojaDer<len(heap):
        return iHojaIzq if heap[iHojaIzq]>heap[iHojaDer] else iHojaDer #intercambio la cabeza con la mayor hoja
    else:
        if iHojaIzq<len(heap):
            return iHojaIzq
        if iHojaDer<len(heap):
            return iHojaDer
        else:
            return -1
    


def quitarCabezaDeHeap(heapAnterior):
    if len(heapAnterior)==1:
        return []
    
    heap=list(heapAnterior)
    heap[0]=heap.pop()

    ie=0#empieza arriba
    while not arbolLocalEsHeap(heap,ie):
        iIntercambiar = iMayorHijo(heap,ie)

        eRaizLocal=heap[ie]
        eIntercambiar=heap[iIntercambiar]

        heap[ie]=eIntercambiar
        heap[iIntercambiar]=eRaizLocal

        ie=iIntercambiar

    return heap


def heapsort(lista):
    heap=[]
    for e in lista:
        heap=agregarAHeap(heap,e)

    listaOrdenada=[]
    while len(heap)>0:
        listaOrdenada=[heap[0]]+listaOrdenada
        heap = quitarCabezaDeHeap(heap)
    
    return listaOrdenada
    

print(heapsort([8,7,15,24,0.5,3,0.1,97]))