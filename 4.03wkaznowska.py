import sys

def zad1():
    zd = input("Podaj jakies zdanie: ")
    suma = 0
    for i in range(0, len(zd)):
        if(zd[i] == " "):
            suma = suma + 1
    print(suma)

#zad1()

def zad2():
    sys.stdout.write("Podaj pierwsza liczbe")
    a = float(sys.stdin.readline())

    sys.stdout.write("Podaj druga liczbe")
    b = float(sys.stdin.readline())

    sys.stdout.write("Podaj trzecia liczbe")
    c = float(sys.stdin.readline())


    print(pow(a,b)+c)

#zad2()

def zad3():
    tekst = input("Wprowadz tekst")
    i = 0
    wartosc = 0
    j = len(tekst)-1
    while(i<=j):
        if(tekst[i] != tekst[j]):
            print("nie jest palindromem")
            wartosc = 1
            break
        i += 1
        j -= 1

    if(wartosc == 0):
        print("jest palindromem")
#zad3()

def zad4():
    nr = int(input("Podaj liczbe do sprawdzenia: "))

    for i in range(2, nr-1):
        if(nr%i == 0):
            print("Nie jest to liczba pierwsza")
            break
    else:
        print("Jest liczba pierwsza")


#zad4()

def zad5():
    for i in range(2,1001):
        wr = 1
        for j in range(2,i-1):
            if(i%j==0):
                wr = wr + j
        if(i==wr):
            print(i)
#zad5()

def zad6():
    list = [1, 3.5, 14.5, 15.5, 20, 17.5]
    for i in range (0, len(list)):
        list[i] = pow(float(list[i]), 2)
    print(list)

#zad6()

def zad7():
    list = []
    i = 0
    while(i<10):
        z = int(input("Podaj liczbe"))
        i += 1
        if(z%2==0):
            list.append(z)

    print(list)

#zad7()

def zad8():
    list = [2, "ptak", 4.5, "XD",  2, 0, True]
    sl = {}
    for i in list:
        suma = 0
        for j in list:
            if i == j:
                suma += 1
        sl[i] = suma

    print(sl)
zad8()

