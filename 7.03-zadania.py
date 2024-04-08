import math

def zad1():
    a = [1-x for x in range(1,10)]
    b = [4**x for x in range(8)]
    c = [x for x in b if x%2 == 0]
    print(a)
    print(b)
    print(c)
def zad2():
    a = [2, 5, 9, 42, 33, 20, 11, 13, 18, 38]
    b = [x for x in a if x%2 == 0]
    print(b)

def zad3():
    lista = {"mleko": "l",  "mąka": "kg", "cukier": "kg", "masło": "g", "jajka": "szt" }
    szt = [produkt for produkt, jednostka in lista.items() if jednostka == "szt"]
    print(szt)
def zad4(a, b, c):
    if (a**2 + b**2 == c**2):
        return "Tak"
    else:
        return "Nie"


def zad5(a, b, h):
    pole= ((a+b) * h) / 2
    return pole



def zad6(a=1, b=4, ile=10):
    wartosc = a * b ** ile
    return wartosc



def zad7(a):
    try:
        wynik = math.sqrt(a)
        return wynik
    except:
        return "error"


def main():
    # zad1()
    # zad2()
    # zad3()
    # print(zad4(3, 6, 5))
    # print(zad5(3, 6, 5))
    # print(zad6(2, 5, 2))
    # print(zad7(2))
main()