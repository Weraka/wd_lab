import numpy as np

tab = np.arange(1,16, dtype=int)
tab1 = []
for i in tab:
    tab1.append(3**tab[i-1])
print(tab1)


lista1 = np.arange(1,10,dtype=float)
lista2 = lista1.astype('int64')
print(lista2)

n = int(input("Podaj wymiar tablicy"))
tablica = np.shape(n)
print(tablica)

a = int(input("Podstawa operacji potegowania"))
b = int(input("Ilosc kolejnych poteg do wygenerowania"))
wynik = np.logspace(2,4,num = b, base = a, dtype=int)
print(wynik)
