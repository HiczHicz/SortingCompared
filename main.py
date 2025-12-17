#..........................BUBBLE SORT...........................#
def bubbleSort(list):
    n=len(list)
    licznik=0
    for i in range(n-1):
        for j in range(n-1-i):
            licznik += 1
            if list[j]>list[j+1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return licznik

#..........................INSERTION SORT...........................#
def insertionSort(list):
    licznik = 0
    for i in range (1,len(list)):
        k=list[i]
        j=i-1
        while j>=0:
            licznik += 1
            if list[j]>k:
                list[j+1]=list[j]
                j-=1
            else:
                break
        list[j+1]=k
    return licznik

#..........................QUICK SORT...........................#
import sys
sys.setrecursionlimit(10**6) #zwiększenie limitu - na macbooku działa inaczej niż na windows, stąd konieczność tego importu

def partition(list, low, high):
    pivot = list[high]
    i = low - 1
    lpq=0
    for j in range(low, high):
        lpq+=1
        if list[j] <= pivot:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i + 1], list[high] = list[high], list[i + 1]
    return i + 1, lpq

def quickSort(list, low, high):
    lpq=0
    if low < high:
        p, lpq1 = partition(list, low, high)
        lpq += lpq1
        lpq2 = quickSort(list, low, p - 1)
        lpq3 = quickSort(list, p + 1, high)
        lpq += lpq2 + lpq3
    return lpq

#..........................HEAP SORT...........................#
def isMaxHeap(list):
    lph=0
    for i in range(1,len(list)):
        lph += i
        if list[i] > list[(i-1)//2]:
            return False , lph
    return True, lph

def maxHeapify(list,n,i):
    lph=0
    l,r = 2*i+1,2*i+2
    if l < n:
        lph += 1
        if list[l] > list[i]:
            largest = l
        else:
            largest = i
    else:
        largest = i

    if r < n :
        lph += 1
        if list[r] > list[largest]:
            largest = r

    if largest != i:
        list[i],list[largest] = list[largest],list[i]
        lph+=maxHeapify(list,n,largest)
    return lph

def buildMaxHeap(list):
    lph=0
    n = len(list)
    for i in range(n//2-1,-1,-1):
        lph+=maxHeapify(list,n,i)
    return lph

def heapSort(list):
    lph=0
    lph+=buildMaxHeap(list)
    for n in range(len(list),1,-1):
        list[0],list[n-1] = list[n-1],list[0]
        lph+=maxHeapify(list,n-1,0)
    return lph

#..........................PLIK CSV...........................#
import csv
from random import random

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
    lpq=quickSort(list_qs, 0, len(list_qs) - 1)
    lph=heapSort(list_hs)
    lpi = quickSort(list_qs, 0, len(list_qs) - 1)
    lpb = heapSort(list_hs)
    wyniki.append([n,lpq,lph,lpi,lpb])

with open('porownania.csv', 'w', newline='') as f:
    writer = csv.writer(f,delimiter=';')
    writer.writerow(['Length','Quick','Heap','Insertion','Bubble'])
    writer.writerows(wyniki)