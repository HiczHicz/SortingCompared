#..........................PLIK CSV...........................#
import csv
from random import random
import sort

l = []
for n in range(10, 1000 + 1, 10):
    lista = [random() for _ in range(n)]
    l.append((lista))

wyniki=[]
for list in l:
    n=len(list)
    list_qs = list[:]
    list_hs = list[:]
    list_is = list[:]
    list_bs = list[:]
    lpq=sort.quickSort(list_qs, 0, len(list_qs) - 1)
    lph=sort.heapSort(list_hs)
    lpi = sort.insertionSort(list_is)
    lpb = sort.bubbleSort(list_bs)
    wyniki.append([n,lpq,lph,lpi,lpb])

with open('porownania.csv', 'w', newline='') as f:
    writer = csv.writer(f,delimiter=';')
    writer.writerow(['Length','Quick Sort','Heap Sort','Insertion Sort','Bubble Sort'])
    writer.writerows(wyniki)