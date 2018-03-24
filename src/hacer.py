#programa que hace los sets de datos: python hacer.py set.csv 500


import random

def hacer(nombre,cantidad):
    numeros=[]
    for i in range(cantidad):
        numeros.append(str(random.random()))
    archivo = open(nombre,"w")
    archivo.write(",".join(numeros))
    archivo.close()




import sys
if len(sys.argv)==1:
    for i in range(10):
        hacer("sets/"+str(i)+".csv",10000)
else:
    hacer(sys.argv[1],int(sys.argv[2]))

