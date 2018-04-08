import sys
from importlib import import_module
import time

# esto lo que hace es agarrar un archivo.py y ejecutar las pruebas.
# ejecuta el metodo "ordenar" del modulo indicado
#
# POR EJEMPLO PARA PROBAR HEAPSORT:
# python src/probador.py heapsort resultados/heapsort.csv
# POR EJEMPLO PARA PROBAR PERO CASO DE HEAPSORT:
# python src/probador.py heapsort resultados/heapsort.csv menorAMayor
#
# PARA GENERAR LOS menorAMayor:
# python src/deshacer.py menorAMayor
#
# TODO ESTO ESTANDO PARADO EN LA RAIZ DEL REPO
#
# heapsort.py debe tener un metodo "ordenar" que acepete una lista y la devuelva ordenada, nada mas!


def probar(module_name, csv_name, amt):
    ordenar = getattr(import_module("search." + module_name), "ordenar")
    with open(csv_name, "r") as archivoCsv:
        lista = archivoCsv.read().split(",")[0:amt]
        lista = list(map(lambda x: float(x), lista))
        time_start = time.time()
        ordenar(lista)
        return time.time() - time_start


if __name__ == '__main__':

    print("primer argumento: modulo a probar")
    print("segundo argumento: archivo output")
    print("tercer argumento (opcional): posfijo de peor caso")

    nombre_modulo = sys.argv[1]
    nombre_reporte = sys.argv[2]
    nombres_archivos = []

    if len(sys.argv) == 4:
        posfijo = sys.argv[3]
        nombres_archivos = map(lambda x: "sets/" + str(x) + posfijo + ".csv", range(10))
    else:
        nombres_archivos = map(lambda x: "sets/" + str(x) + ".csv", range(10))

    nombres_archivos = list(nombres_archivos)
    print(nombres_archivos)
    cantidades = [50, 100, 500, 1000, 2000, 3000, 4000, 5000, 7500, 10000]
    with open(nombre_reporte, "w") as reporte:
        reporte.write(nombre_modulo + "," + ",".join(map(str, cantidades)) + "\n")  # encabezado

        for nArchivo in nombres_archivos:

            print("probando " + nArchivo)
            resultados = []
            for cantidad in cantidades:
                resultados.append(str(probar(nombre_modulo, nArchivo, cantidad)))
                print(cantidad)
            reporte.write(nArchivo + "," + ",".join(resultados) + "\n")
