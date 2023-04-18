#!/usr/bin/python3
# Skrypt sortujący tablice tak że elementy dotatnie są z lewej a ujemne z prawej strony
array = [-1,3,-4,2,-3,5,1,6,8,-7,-2,-5,10,-100,100,0,1,0]

def sort(A):
    
    lastIndex = len(A)-1
    arraySorted = False
    
    # Indexy 
    lewy = 0
    prawy = 1

    # Iteruj po tablicy porownujac po dwa elementy stojace obok siebie
    # Jesli z prawej jest dodatnia a z lewej ujemna zamien je miejscami
    # (Dodatnia liczba przepchana na lewo)
    while(not arraySorted):
        if(A[lewy] < 0 and A[prawy] >= 0):
            A[lewy], A[prawy] = A[prawy], A[lewy]

    # Wroc na poczatek gdy koniec tablicy
        if(prawy == lastIndex):
            prawy = 1
            lewy = 0    

    # Sprawdz czy tablica jest posortowana
    # Sposob: Nie moze byc liczby dodatniej z lewej strony obok ujemniej z prawej
    # arraySorted = False, Jesli tablica dalej nie jest posortowana i potrzebna jej kolejna iteracja
        arraySorted = True
        for i in range(0, lastIndex):
            if(A[i] < 0 and A[i+1] >= 0):
                arraySorted = False        
        
    # Jesli nie wracasz na koniec tablicy popchnij wskazniki w prawo o jeden index
        else:
            lewy = lewy + 1
            prawy = prawy + 1   
        

print("Przed:", array)    
sort(array)
print("Po    ", array)
