#!coding=utf8
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
    stack = [(inf, sup)]
    while stack:
        inf, sup = stack.pop()
        mid_point = partition(lista, inf, sup)

        if mid_point > inf:
            stack.append((inf, mid_point - 1))

        if mid_point < sup:
            stack.append((mid_point + 1, sup))

    return lista


def ordenar(lista):
    return quicksort(lista, 0, len(lista) - 1)
