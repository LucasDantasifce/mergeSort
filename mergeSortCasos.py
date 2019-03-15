from random import randint, shuffle
import matplotlib as mpl
import timeit


Dlista = [10000, 20000, 30000, 40000, 50000]


def geraLista(tam):
    lista = []
    for i in range(tam):
        lista.append(randint(0,tam))
    shuffle(lista)

    return lista



def merge(v, esq, dir):
    aux = []
    swapsAux = 0
    i = j = 0
    while i < len(esq) and j < len(dir):
        if esq[i] < dir[j]:
            aux.append(esq[i])
            swapsAux += 1
            i += 1
        else:
            aux.append(dir[j])
            swapsAux += 1
            j += 1
    while i < len(esq):
        aux.append(esq[i])
        swapsAux += 1
        i += 1
    while j < len(dir):
        aux.append(dir[j])
        swapsAux += 1
        j += 1
    v = aux

    return v


def mergeSort(v):
    if len(v) is 1:
        return v
    meio = int(len(v)/2)
    esq = v[:meio]
    dir = v[meio:]
    esq = mergeSort(esq)
    dir = mergeSort(dir)
    v = merge(v, esq, dir)
    return v


mpl.use('Agg')
import matplotlib.pyplot as plt
def desenhaGrafico(x,y,ym,yp,xl = "Tamanho", yl = "Tempo"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Pior Tempo")
    ax.plot(x,ym, label = "Melhor Tempo")
    ax.plot(x,yp, label = "Medio Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('GraficoMerge.png')

MelhorCaso = []
PiorCaso = []
MedioCaso = []

for i in Dlista:
    medio = geraLista(i)
    melhor = sorted(medio)
    pior = sorted(melhor, reverse=True)

    MelhorCaso.append(timeit.timeit("aux={}\naux = mergeSort(aux)".format(melhor.copy()),setup="from __main__ import mergeSort",number=1))
    PiorCaso.append(timeit.timeit("aux={}\naux = mergeSort(aux)".format(pior.copy()),setup="from __main__ import mergeSort",number=1))
    MedioCaso.append(timeit.timeit("aux={}\naux = mergeSort(aux)".format(medio.copy()),setup="from __main__ import mergeSort",number=1))
    print("Ordenado um i em Dlista!")


desenhaGrafico(Dlista,MedioCaso,MelhorCaso,PiorCaso)

import itertools as it
tamlista = list(it.permutations(list(range(6))))
tempoIteracao = []
listaOrig = []
for lista in tamlista:
    tempoIteracao.append(timeit.timeit("mergeSort({})".format(list(lista).copy()),setup="from __main__ import mergeSort",number=1))
    listaOrig.append(list(lista))

print("O tempo minimo foi de {}".format(min(tempoIteracao)))
print("lista que teve tempo minimo foi:{}".format(listaOrig[tempoIteracao.index(min(tempoIteracao))]))
print("O tempo maximo foi de {}".format(max(tempoIteracao)))
print("lista que teve tempo maximo foi:{}".format(listaOrig[tempoIteracao.index(max(tempoIteracao))]))


