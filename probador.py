#esto lo que hace es agarrar un archivo.py y ejecutar las pruebas.
#ejecuta el metodo "ordenar" del modulo indicado
#
# POR EJEMPLO PARA PROBAR HEAPSORT:
# python probador.py heapsort resultados/heapsort.csv
#
# heapsort.py debe tener un método "ordenar" que acepete una lista y la devuelva ordenada, nada más!


from importlib import import_module
import time

def probar(nombreModulo,nombreCsv,cantidad):
    ordenar=getattr(import_module(nombreModulo),"ordenar")
    with open(nombreCsv,"r") as archivoCsv:
        lista=archivoCsv.read().split(",")[0:cantidad]
        lista=map(lambda x : float(x),lista)
        tiempoPrincipio=time.time()
        ordenar(lista)
        return time.time()-tiempoPrincipio

import sys
print("primer argumento: modulo a probar")
print("segundo argumento: archivo output")

nombreModulo=sys.argv[1]
nombreRporte=sys.argv[2]
cantidades=[50,100,500,1000,2000,3000,4000,5000,7500,10000]
with open(nombreRporte,"w") as reporte:
    reporte.write(nombreModulo+","+",".join(map(str,cantidades)))#encabezado

    for nroArchivo in range(10):
        nArchivo="sets/"+str(nroArchivo)+".csv"
        print("probando "+nArchivo)
        resultados=[]
        for cantidad in cantidades:
            resultados.append(str(probar(nombreModulo,nArchivo,cantidad)))
            print(cantidad)
        reporte.write(nArchivo+","+",".join(resultados)"\n")

            


