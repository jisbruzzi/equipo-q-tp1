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

h=[]
h=agregarAHeap(h,1)
print(h)
h=agregarAHeap(h,9)
print(h)
h=agregarAHeap(h,15)
print(h)
h=agregarAHeap(h,2)
print(h)
h=agregarAHeap(h,15)
print(h)
h=agregarAHeap(h,18)
print(h)
h=agregarAHeap(h,19)
print(h)
h=agregarAHeap(h,0.3)
print(h)
h=agregarAHeap(h,45)
print(h)

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
    


def quitarCabezaDeHeap(heap):
    heap=list(heap)
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



    

h=quitarCabezaDeHeap(h)
print(h)
h=quitarCabezaDeHeap(h)
print(h)
h=quitarCabezaDeHeap(h)
print(h)
h=quitarCabezaDeHeap(h)
print(h)
h=quitarCabezaDeHeap(h)
print(h)
h=quitarCabezaDeHeap(h)
print(h)
h=quitarCabezaDeHeap(h)
print(h)
h=quitarCabezaDeHeap(h)
print(h)