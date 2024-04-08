import numpy as np

a = np.array([0,1])           #tablica
print(a)

a = np.arange(2)
print(a)                         #tablica od 0

print(a.dtype)                  #typ danych
a = np.array(['a','b','c',1,2,3])           #
print(a)                            #tablica
print(a.dtype)

a = np.arange(2, dtype='int32')
print(a.dtype)
b = a.astype('float')       #zamiana inta na floata
print(b)
print(b.dtype)
print(b.shape)              #rozmiar

m = np.array((np.arange(2), np.arange(2)))
print(m)                                     #macierz
print(m.shape)

n = np.array([[2, 3, 4],
               [5, 6, 7]], dtype='float')          #macierz ze zmienieniem typu danych
print(n)

zera = np.zeros((5,5))
jedynki = np.ones((4,4))
print(zera)                 #tablica z zerami o wym 5x5
print(jedynki)              #tablica z jedynkami o wym 4x4
print(zera.dtype)
print(jedynki.dtype)

pusta = np.empty((2,2))
print(pusta)
poz_1 = pusta[1,1]              #XD
poz_2 = pusta[0,1]
print(poz_1)
print(poz_2)

macierz = np.array([[1,2], [3,4]])      #macierz
print(macierz)

liczby = np.arange(1,2,0.1)     #wypelnienie tablicy od 1 do 2 co 0.1
print(liczby)

liczby_lin = np.linspace(1,2,5, endpoint=False)
print(liczby_lin)

z = np.indices((5,3))           #macierz trzojwymiarowa 5x3, kazdy wiersz zaczyna sie od zera w gore
print(z)                        #daje macierz, gdzie 1 wiersz sklada sie z zer, potem jedynek, itd
print(z.shape)
print(z[0,2,1])                 #tablica 0 (pierwsza), wiersz drugi, kolumna pierwsza (to sie liczy kol 0,1 itd wiadomix

x,y = np.mgrid[0:5, 0:5]        #dwie macierze naraz robi, gdzie pierwsza zawsze jest 000,111 itd, a druga 012,012 itd
print(x)
print(y)

mat_diag_k = np.diag([a for a in range(5)], -1)             #macierz diagonalna
print(mat_diag_k)

z = np.fromiter(range(5), dtype = 'int32')                  #wektor
print(z)

znaki = b'abcdef'
zn1 = np.frombuffer(znaki, dtype='S1')
print(zn1)                                                  #ale buja
zn2 = np.frombuffer(znaki, dtype='S2')
print(zn2)

#zn = 'abcdef'
#zn3 = np.array(list(zn))
#zn4 = np.array(list(zn),dtype='S1')
#zn5 = np.array(list(b'abcdef'))                 #cos nie dziala;(
#zn6 = np.frombuffer(zn,dtype='S1')
#zn7 = np.array(zn,dtype='U1')



mat = np.ones((2,2))
mat_1 = np.ones((2,2))
mat = mat + mat_1
print(mat)
print(mat-mat_1)
print(mat*mat_1)
print(mat/mat_1)
mat_1 = np.array(([4,5], [6,3]))
print(mat*mat_1)
print(mat/mat_1)


#dwoch rzeczy nie zapisalam bo nie zdazylam xdxdxdxxdxxdxdxdxdxdxdx

a = np.arange(10)       #tablica z el od 0 do 9 (10-elementowa)
print(a)
s = slice(2,7,2)        #liczby parzyste od 2 do 7
print(a[s])
s = range(2,7,2)
print(a[s])
print(a[2:7:2])
print(a[1:])            # liczby od 1 a nie od 0
print(a[2:5])           #liczby od 2 do 4

mats = np.arange(25)
mats = mats.reshape((5,5))

print(mats[1:])
print(mats[:,1])        #jaciekrece
print(mats[:,-2:])
print(mats[2:6,1:3])
print(mats[:,range(2,6,2)])
print('')

ostx = np.array(([0,1,2],
                [3,4,5],
                [6,7,8],
                [9,10,11]))

print(ostx)
rows = np.array([[0,0],[3,3]])      #wycinanie kolumn i wierszy
cols = np.array([[0,2],[0,2]])
osty = ostx[rows,cols]
print(osty)

xd = np.loadtxt('liczby.txt',dtype=int)
print(xd)
print(xd.shape)
for i in range(xd.shape[0]):
    lis = []
    for j in range(xd.shape[1]):
        lis.append(xd[j][i])
    print(max(lis))

