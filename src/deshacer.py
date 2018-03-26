from importlib import import_module
import sys


def deshacer(nombreModulo, nombreCsv, nombreCsvSalida):
    desordenar = getattr(import_module(nombreModulo), "desordenar")
    with open(nombreCsv, "r") as archivoCsv:
        lista = archivoCsv.read().split(",")
        lista = map(lambda x: float(x), lista)
        ordenada=sorted(lista)
        desordenada=desordenar(ordenada)
        stringGuardar=",".join(map(str,desordenada))
        with open(nombreCsvSalida,"w") as archivoCsvSalida:
            archivoCsvSalida.write(stringGuardar)


print("primer argumento: modulo a probar")
print("segundo argumento: archivo entrada")
print("segundo argumento: archivo salida")

if len(sys.argv)>=4:
    nombreModulo = sys.argv[1]
    nombreEntrada = sys.argv[2]
    nombreSalida = sys.argv[3]
    deshacer(nombreModulo,nombreEntrada,nombreSalida)

if len(sys.argv)==2:
    nombreModulo = sys.argv[1]
    for i in range(10):
        nombreEntrada="sets/"+str(i)+".csv"
        nombreSalida="sets/"+str(i)+nombreModulo+".csv"
        deshacer(nombreModulo,nombreEntrada,nombreSalida)