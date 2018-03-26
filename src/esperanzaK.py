import math
from decimal import *
import operator as op
# fuente https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python

factoriales = {}
factoriales[0] = Decimal(1)
factoriales[1] = Decimal(1)
factorialMayor = 1


def factorialMem(n):
    global factorialMayor
    global factoriales

    if n <= factorialMayor:
        return factoriales[n]
    else:
        for i in range(factorialMayor, n + 1):
            factoriales[i] = factoriales[i - 1] * Decimal(i)
        factorialMayor = n
        return factoriales[n]


def ncr(n, r):
    f = factorialMem
    fn = f(n)
    fr = f(r)
    fnr = f(n - r)
    return fn / (fr * fnr)


# ESTO NO ANDA BIEN, PRECISION NUMERICAAAAA, Y HACER CACHE DE NCR!!
def esperanzaK(n):
    divisorComun = Decimal(ncr(n, n / 2) / 2)
    suma = Decimal(0.0)
    for k in range(1, n / 2):
        suma += ncr(n - k - 1, n / 2 - 1) * Decimal(k) / divisorComun
        if k % 10000 == 0:
            print(k)
    return suma


with open("resultados/esperanzaK.csv", "w") as reporte:
    reporte.write("n,E(K)\n")
    n = 2
    for i in range(20):
        esperanza = esperanzaK(n)
        reporte.write(str(n) + "," + str(esperanza) + "\n")
        n *= 2
