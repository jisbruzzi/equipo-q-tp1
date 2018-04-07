#!coding=utf8

from random import shuffle


def partition(lista, inf, sup):
    pivot = lista[sup]
    index = inf - 1

    for i in range(inf, sup):
        if lista[i] <= pivot:
            index += 1
            lista[i], lista[index] = lista[index], lista[i]

    lista[sup], lista[index + 1] = lista[index + 1], lista[sup]
    return index + 1


def quicksort(lista, inf, sup):
    if inf < sup:
        mid_point = partition(lista, inf, sup)
        low_mid_point = mid_point
        while inf < low_mid_point:
            low_mid_point = partition(lista, inf, low_mid_point - 1)

        while mid_point + 1 < sup:
            mid_point = partition(lista, mid_point + 1, sup)
    return lista


def ordenar(lista):
    return quicksort(lista, 0, len(lista) - 1)

