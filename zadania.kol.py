import math
import random


def zad1():
    pkta = math.pow(math.exp(4)-math.log(34,2), -3)
    print(round(pkta,2))

    pktb = math.pow(math.log(20, 10)+math.cos(45)+math.e,-3)
    print(round(pktb,2))

    pktc = math.pow(math.log(20, 3)+math.sin(45)*(5/8), -4)
    print(round(pktc,2))

    pktd = (math.log(23,3) + math.pow(math.sin(34)+5,-3))
    print(round(pktd,2))

    pkte = math.pow(math.log(32, 2)+math.pi+math.sin(56), -4)
    print(round(pkte,2))

def zad2():
    height = int(input("Podaj wysokość wieży"))
    if height > 10:
        return 0
    else:
        for i in range(1, height+1):
            print("A"*i)

def zad3(height):

    if height > 10:
        return 0
    else:
        for i in range(height):
            for j in range(height-i-1):
                print(" ", end="")
            for j in range(i+1):
                print("A", end=" ")
            print()

def zad4():
    zm = random.randint(1, 100)
    print(zm)
    list = [22, "dwa", True, 0, -3]
    random_from_lista = random.choice(list)
    print(random_from_lista)


def main():
    #zad1()
    #zad2()
    height = int(input("Podaj wysokość wieży"))
    zad3(height)
    #zad4()
    # col = int(input("Podaj liczbę kolumn"))
    # row = int(input("Podaj liczbę wierszy"))
    # zad5(col, row)

main()